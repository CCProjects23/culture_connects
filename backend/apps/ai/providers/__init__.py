"""AI provider adapter.

AI functionality is isolated behind this boundary so the rest of the
application never calls an AI vendor directly. This enables provider
swaps, testing with mocks, cost control and future local models
(see AGENT.md §7 and ROADMAP.md M5).
"""

from .base import (
    AIProvider,
    DebateAnalysis,
    DebateAnalysisRequest,
    DebateTurn,
)
from .factory import get_ai_provider
from .mock import MockAIProvider

__all__ = [
    "AIProvider",
    "DebateAnalysis",
    "DebateAnalysisRequest",
    "DebateTurn",
    "MockAIProvider",
    "get_ai_provider",
]
