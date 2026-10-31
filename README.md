# Azerbaijan Cryptocurrency Token Project

Independent Azerbaijan-themed cryptocurrency/token and blockchain application prototype, maintained by elon00.

## Project identity

This project targets tokens on existing blockchain networks. The repository name is a historical identifier; asset definitions, supported chains and deployed addresses must be established from the actual implementation and verified release records.

| Item | Status |
|---|---|
| Product stage | Prototype; production readiness requires evidence |
| Asset type | Blockchain token; chain-specific standard to be selected |
| Token name, symbol and decimals | Pending project specification |
| Initial supply and emission policy | Pending tokenomics review |
| Mint, upgrade and treasury authorities | Pending role and custody design |
| Canonical chain and network identifier | Pending compatibility review |
| Testnet contract/program/asset identifier | Pending verified release evidence |
| Mainnet contract/program/asset identifier | Pending approved release evidence |

## Cryptocurrency and blockchain scope

- Implement a useful token and its application on a compatible blockchain.
- Define utility, finite issuance transactions, lifetime supply policy, emission limits, vesting, governance and treasury controls.
- Use the selected chain's token standard, wallet signing flow, transaction format, fees and finality rules.
- Integrate wallet connections, balances, transaction previews and validated payment QR payloads.
- Use authenticated RPC access and chain identity checks; configure QuickNode where the selected network supports it.
- Add x402 paid API access and Bazaar discovery only when the product has a real paid resource and supported settlement path.

EVM contracts, Solana programs, Move modules, Algorand assets, TON contracts and ICP canisters require appropriate implementations and verification. A TVL ranking does not establish cross-chain compatibility.

## Implementation and verification

Existing research or simulation modules must be evaluated separately from working token contracts, cryptographic verification and confirmed payments. A local hash, a formatted proof string, a module name or a passing CI badge does not establish those capabilities.

Before a release, record:

1. The exact source commit and reproducible build artifact.
2. Meaningful unit, regression, smoke, dependency, secret and applicable CodeQL/static-analysis results.
3. Token supply invariants, access control, unauthorized mint rejection and wallet/signature replay tests.
4. Correct chain identity, real testnet transactions, public explorer links and source-to-deployment verification.
5. Operational monitoring, recovery tests, fee budget, authorized signer and release approval.

PQC features require genuine reviewed algorithms and published-vector/negative tests. Conway B3/S23 can serve as a simulation component; its presence alone does not establish network consensus.

## Development

Review the repository's actual package manifests, dependencies and CI configuration before running its code. For the Python prototype suite, where present:

```sh
python -m unittest discover -s tests -p "*_test.py"
```

Test output must describe the checks actually executed. A perfect readiness score is earned through current evidence.

## Portfolio coordination

Use [bountyhunter-os](https://github.com/elon00/bountyhunter-os) for repository-specific repair profiles, source-bound test evidence and release blocker tracking. Keep this product's source, token configuration and deployment history in this repository.
