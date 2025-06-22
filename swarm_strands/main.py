"""Command line entry point for the swarm agents."""
from __future__ import annotations

import argparse

from config import strands_model_mini
from .core.orchestrator import Orchestrator
from .data import setup_data_dirs


def main() -> None:
    parser = argparse.ArgumentParser(description="Run swarm agents")
    parser.add_argument("query", help="User request to process")
    args = parser.parse_args()

    setup_data_dirs()

    orchestrator = Orchestrator(model=strands_model_mini)
    result = orchestrator.run(args.query)
    print(result)


if __name__ == "__main__":
    main()
