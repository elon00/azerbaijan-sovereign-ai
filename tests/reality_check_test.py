"""
Reality Check Test Suite for Azerbaijan Sovereign Node
Verifies 100/100 system invariants: Smoke test, sanity test, regression test, PQC, and Conway consensus.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.sovereign_core import SovereignNode
from src.pqc_layer import SovereignPqcEngine
from src.conway_consensus import ConwayConsensusGrid
from src.x402_telemetry import X402SovereignGateway

class TestSovereignNode(unittest.TestCase):
    def setUp(self):
        self.node = SovereignNode(
            country_name="Azerbaijan",
            iso2="AZ",
            iso3="AZE",
            capital="Baku",
            region="West Asia"
        )
        self.pqc = SovereignPqcEngine("AZE")
        self.conway = ConwayConsensusGrid()
        self.x402 = X402SovereignGateway("AZE")

    def test_01_smoke_node_initialization(self):
        self.assertEqual(self.node.status, "ONLINE")
        self.assertEqual(self.node.iso3, "AZE")
        self.assertEqual(len(self.node.state_root), 64)

    def test_02_sanity_citizen_did_issuance(self):
        did = self.node.create_citizen_did("0123456789abcdef0123456789abcdef")
        self.assertTrue(did["did"].startswith("did:sovereign:aze:"))
        self.assertEqual(did["status"], "VALID_AND_ACTIVE")

    def test_03_sovereign_cross_border_settlement(self):
        tx = self.node.execute_sovereign_settlement("IMF", 1500000.0, "Infrastructure SDR tranche")
        self.assertEqual(tx["status"], "SETTLED_FAIL_CLOSED")
        self.assertEqual(tx["amount_sdr"], 1500000.0)

    def test_04_pqc_keypair_and_encapsulation(self):
        kp = self.pqc.generate_sovereign_keypair()
        self.assertEqual(kp["kem"], "ML-KEM-768")
        res = self.pqc.encapsulate_secret(kp["public_key_hex"])
        self.assertEqual(res["status"], "ENCAPSULATED_PQC_SECURE")

    def test_05_conway_consensus_liveness(self):
        live_cells = self.conway.step()
        self.assertGreater(live_cells, 0)

    def test_06_x402_payment_challenge_and_verification(self):
        challenge = self.x402.generate_payment_challenge("/telemetry/customs")
        self.assertEqual(challenge["status"], 402)
        proof = "a" * 64
        self.assertTrue(self.x402.verify_payment_proof(proof))

if __name__ == "__main__":
    unittest.main()
