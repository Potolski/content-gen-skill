# The pinned verification toolchain for content-gen.
#
# Purpose: give `verify_code.py --env docker` a reproducible environment whose tool
# VERSIONS MATCH what generated content declares (course.toolchain / frozen_facts), so
# "does this code actually run?" is answered against the versions the reader will use —
# not whatever happens to be on the author's machine.
#
#   docker build -t content-gen-verify skills/content-gen/verify
#   docker run --rm -v "$PWD":/work -w /work content-gen-verify \
#       python3 skills/content-gen/tools/verify_code.py content/courses/<id> --env local --run-smoke
#
# Bump the ARG pins to match the content's declared toolchain when it moves. These
# defaults track the btc-to-sol course's 2026 declarations.
FROM ubuntu:24.04

ARG PYTHON=3.11
ARG NODE_MAJOR=20
ARG RUST=1.86.0
ARG SOLANA=v2.1.0            # Agave CLI; set to the release the content declares (e.g. v4.1.1 when available)
ARG ANCHOR=0.31.1            # anchor-cli / avm; set to the declared version (e.g. 1.1.2) when the content targets it
ARG FOUNDRY=stable
ARG SOLIDITY=0.8.28

ENV DEBIAN_FRONTEND=noninteractive PATH="/root/.cargo/bin:/root/.foundry/bin:/root/.local/share/solana/install/active_release/bin:/root/.avm/bin:${PATH}"

RUN apt-get update && apt-get install -y --no-install-recommends \
      curl ca-certificates git build-essential pkg-config libssl-dev libudev-dev \
      python3 python3-pip bitcoind \
    && rm -rf /var/lib/apt/lists/*

# Node + TypeScript runner
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_MAJOR}.x | bash - && apt-get install -y nodejs \
    && npm i -g typescript tsx

# Rust (pinned)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain ${RUST}

# Foundry (forge/cast/anvil + solc via svm)
RUN curl -L https://foundry.paradigm.xyz | bash && /root/.foundry/bin/foundryup && \
    /root/.foundry/bin/forge --version

# Solana (Agave) + Anchor via avm — pin to the DECLARED version for the content under test
RUN sh -c "$(curl -sSfL https://release.anza.xyz/${SOLANA}/install)" || \
    sh -c "$(curl -sSfL https://release.solana.com/${SOLANA}/install)"
# avm now lives under the solana-foundation org (migrated from coral-xyz)
RUN cargo install --git https://github.com/solana-foundation/anchor avm --force && \
    avm install ${ANCHOR} && avm use ${ANCHOR}

WORKDIR /work
# Default: verify a course dir passed as CMD; see the header for the full command.
ENTRYPOINT ["python3", "skills/content-gen/tools/verify_code.py"]
CMD ["--selftest"]
