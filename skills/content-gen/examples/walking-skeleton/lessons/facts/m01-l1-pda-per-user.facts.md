Solana has no native mappings; per-user data lives in separate PDA accounts.
PDA derivation: find_program_address(seeds, program_id) -> (address, canonical_bump).
Store the canonical bump; recomputing it every call wastes compute and only the canonical bump is safe.
