"""High level pipeline driving the swarm execution."""
from __future__ import annotations

from typing import Iterable, Callable

from ..agents.planner_agent import PlannerAgent
from ..agents.validator_agent import ReportValidatorAgent
from ..agents.base_agent import BaseAgent


class Pipeline:
    """Simple pipeline that plans and executes a sequence of agents."""

    def __init__(self, model: object, extra_agents: Iterable[Callable] | None = None) -> None:
        self.planner = PlannerAgent(model=model)
        self.validator = ReportValidatorAgent(model=model)
        self.extra_agents = list(extra_agents or [])

    def run(self, query: str) -> str:
        """Plan and run the swarm for a user query."""
        plan = self.planner.plan(query)
        # Placeholder for executing the plan with the rest of agents
        # In a real system this would parse the plan and invoke tools accordingly.
        for agent in self.extra_agents:
            if isinstance(agent, BaseAgent):
                agent.run(query)
        validation = self.validator.validate("reportes/latest.md")
        return f"PLAN:\n{plan}\nVALIDATION:\n{validation}"
