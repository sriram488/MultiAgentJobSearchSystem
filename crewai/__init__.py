from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Iterable, Optional


class Process(str, Enum):
    sequential = "sequential"


@dataclass
class Agent:
    role: str
    goal: str
    backstory: str
    llm: Any
    verbose: bool = False


@dataclass
class Task:
    description: str
    expected_output: str
    agent: Agent
    output_file: Optional[str] = None
    output: Any = None


@dataclass
class Crew:
    agents: list[Agent]
    tasks: list[Task]
    process: Process = Process.sequential
    verbose: bool = False

    def kickoff(self) -> str:
        outputs: list[str] = []
        for task in self.tasks:
            agent = task.agent
            llm = agent.llm

            # LangChain chat models typically support `.invoke(...)`.
            if hasattr(llm, "invoke"):
                result = llm.invoke(task.description)
            elif callable(llm):
                result = llm(task.description)
            else:
                raise TypeError("Agent.llm must be callable or have .invoke()")

            task.output = result
            outputs.append(str(result))

            if task.output_file:
                try:
                    with open(task.output_file, "w", encoding="utf-8") as f:
                        f.write(str(result))
                except OSError:
                    # Best-effort file output.
                    pass

        return "\n\n".join(outputs)

