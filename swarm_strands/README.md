# Swarm Strands

Refactored project extracted from `swarm_strands.ipynb`. The notebook has been
split into modular Python files so the system can be run from the command line.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m swarm_strands.main "<peticion del usuario>"
```

The configuration in `config.yaml` defines the model used by the agents. Ensure
your `OPENAI_API_KEY` environment variable is set before running.
