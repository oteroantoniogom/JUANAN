"""Base classes and interfaces for Strands agents."""
from __future__ import annotations

from typing import Callable, Iterable, List

from strands import Agent


class BaseAgent:
    """Wrapper around :class:`strands.Agent` with a simple synchronous interface."""

    def __init__(
        self,
        model: object,
        tools: Iterable[Callable] | None = None,
        system_prompt: str = "",
    ) -> None:
        self.agent = Agent(model=model, tools=list(tools or []), system_prompt=system_prompt)

    def run(self, query: str) -> str:
        """Execute the underlying agent with the provided query."""
        return self.agent(query)
