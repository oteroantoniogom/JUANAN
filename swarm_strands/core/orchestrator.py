"""Main orchestrator coordinating all agents."""
from __future__ import annotations

from typing import Iterable, Callable

from ..agents.base_agent import BaseAgent
from .pipeline import Pipeline


class Orchestrator:
    """Coordinates the planner, pipeline and other agents."""

    def __init__(self, model: object, agents: Iterable[BaseAgent] | None = None) -> None:
        self.pipeline = Pipeline(model=model, extra_agents=agents)

    def run(self, query: str) -> str:
        """Run the orchestrator for the provided query."""
        return self.pipeline.run(query)
