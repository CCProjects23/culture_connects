"""Provider-agnostic contracts for AI debate analysis."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(frozen=True)
class DebateTurn:
    """A single contribution within a debate."""

    author: str
    position: str  # e.g. "A" or "B"
    content: str


@dataclass(frozen=True)
class DebateAnalysisRequest:
    """Minimal, structured context handed to a provider.

    Deliberately small (see AGENT.md §20 – AI cost control): only what the
    analysis needs, never whole database records.
    """

    topic: str
    turns: list[DebateTurn]
    language: str = "en"


@dataclass(frozen=True)
class DebateAnalysis:
    """Neutral reflection of a debate – a tool, not a judge.

    Never contains a winner or a "who is right" verdict (ROADMAP.md M5).
    """

    summary: str
    commonalities: list[str] = field(default_factory=list)
    differences: list[str] = field(default_factory=list)
    misunderstandings: list[str] = field(default_factory=list)
    new_perspectives: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)
    provider: str = ""
    model: str | None = None


class AIProvider(ABC):
    """Interface every AI provider implementation must fulfil."""

    name: str = "base"

    @abstractmethod
    def analyze_debate(self, request: DebateAnalysisRequest) -> DebateAnalysis:
        """Produce a neutral analysis for a completed debate."""
        raise NotImplementedError
