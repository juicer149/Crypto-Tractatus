# Crypto-Tractatus

The third stage of my classical cryptography experiments, developed in May 2025.

This project grew out of earlier work in `crypto_lab` and `crypto_proto_1`, but moved further toward mathematical modelling, semantic data types and composable cipher architecture.

It was developed alongside introductory linear algebra studies during an AI program, using classical cryptography as a practical playground for experimenting with:

- rotation matrices
- sequence transformations
- modular arithmetic
- semantic sequence types
- cipher specifications and registries
- ROT and classical Vigenère ciphers

## Verification

Run:

```bash
make check
```

This performs Python compilation checks and unit tests.

## Project lineage

1. `crypto_lab` — first cipher and CLI experiment
2. `crypto_proto_1` — sequence, alphabet and cipher architecture experiments
3. **Crypto-Tractatus** — matrix, specification and semantic-type experiments
4. `CryptoTractatusMVP` — simplified config-driven implementation focused on a usable CLI

## Historical restoration

The final historical snapshot contained a few incomplete refactor remnants. Small fixes were later made to restore the intended design without modernizing the project:

- repaired stale module imports
- renamed the internal `math` package to avoid collision with Python's standard library
- removed a circular import in the cipher specification system
- reconnected matrix transforms to the current sequence utilities
- fixed classical Vigenère decryption
- preserved repeated characters in Vigenère keywords
- added regression tests and a simple verification command

## Status

Historical project.
