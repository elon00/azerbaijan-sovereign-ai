"""
x402 Bazaar Micropayment Protocol & Discovery Interface
Provides autonomous HTTP 402 micro-settlement for sovereign API calls.
"""
import hashlib
import time

class X402SovereignGateway:
    def __init__(self, nation_iso3: str):
        self.nation_iso3 = nation_iso3
        self.base_fee_sats = 402

    def generate_payment_challenge(self, resource_path: str) -> dict:
        nonce = hashlib.sha256(f"{resource_path}:{time.time()}".encode()).hexdigest()[:16]
        return {
            "status": 402,
            "header": "Payment Required",
            "protocol": "x402-v1",
            "resource": resource_path,
            "required_amount_sats": self.base_fee_sats,
            "recipient_nation": self.nation_iso3,
            "nonce": nonce
        }

    def verify_payment_proof(self, proof_hash: str) -> bool:
        return len(proof_hash) == 64 and all(c in "0123456789abcdef" for c in proof_hash.lower())
