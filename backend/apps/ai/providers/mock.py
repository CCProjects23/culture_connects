"""Deterministic mock AI provider.

Returns a structured, neutral analysis without calling any external
service. Used as the default in the MVP, in tests and as a safe
fallback (see ROADMAP.md M0 / M5).
"""

from __future__ import annotations

from .base import AIProvider, DebateAnalysis, DebateAnalysisRequest


class MockAIProvider(AIProvider):
    name = "mock"

    def __init__(self, model: str | None = None) -> None:
        self.model = model or "mock-analysis-v1"

    def analyze_debate(self, request: DebateAnalysisRequest) -> DebateAnalysis:
        positions = sorted({turn.position for turn in request.turns if turn.position})
        turn_count = len(request.turns)
        parties = " and ".join(positions) if positions else "both participants"

        return DebateAnalysis(
            summary=(
                f"Mock analysis of {turn_count} contribution(s) on "
                f'"{request.topic}". This is placeholder output – no real '
                "AI was consulted, and it does not judge who is right."
            ),
            commonalities=[
                f"{parties} engaged with the topic in a structured exchange.",
            ],
            differences=[
                "Participants approached the topic from different positions.",
            ],
            misunderstandings=[],
            new_perspectives=[
                "Each side was exposed to the other's reasoning.",
            ],
            open_questions=[
                "Which points would benefit from further clarification?",
            ],
            provider=self.name,
            model=self.model,
        )
