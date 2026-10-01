"""Tests for the AI provider adapter and the mock implementation."""

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase, override_settings

from apps.ai.providers import (
    AIProvider,
    DebateAnalysis,
    DebateAnalysisRequest,
    DebateTurn,
    MockAIProvider,
    get_ai_provider,
)


def _sample_request() -> DebateAnalysisRequest:
    return DebateAnalysisRequest(
        topic="Should cities ban private cars?",
        turns=[
            DebateTurn(author="alpha", position="A", content="Yes, for clean air."),
            DebateTurn(author="beta", position="B", content="No, mobility matters."),
        ],
    )


class MockAIProviderTests(TestCase):
    def test_is_an_ai_provider(self):
        self.assertIsInstance(MockAIProvider(), AIProvider)

    def test_analyze_returns_structured_analysis(self):
        analysis = MockAIProvider().analyze_debate(_sample_request())
        self.assertIsInstance(analysis, DebateAnalysis)
        self.assertEqual(analysis.provider, "mock")
        self.assertTrue(analysis.summary)

    def test_analysis_declares_no_winner(self):
        analysis = MockAIProvider().analyze_debate(_sample_request())
        blob = " ".join(
            [analysis.summary, *analysis.commonalities, *analysis.differences]
        ).lower()
        self.assertNotIn("winner", blob)
        self.assertNotIn("wins", blob)

    def test_is_deterministic(self):
        request = _sample_request()
        self.assertEqual(
            MockAIProvider().analyze_debate(request),
            MockAIProvider().analyze_debate(request),
        )


class FactoryTests(TestCase):
    @override_settings(AI_PROVIDER="mock")
    def test_returns_mock_by_default(self):
        self.assertIsInstance(get_ai_provider(), MockAIProvider)

    def test_explicit_name_overrides_settings(self):
        self.assertIsInstance(get_ai_provider("mock"), MockAIProvider)

    @override_settings(AI_PROVIDER="does-not-exist")
    def test_unknown_provider_raises(self):
        with self.assertRaises(ImproperlyConfigured):
            get_ai_provider()

    @override_settings(AI_PROVIDER="mock", AI_MODEL="custom-model")
    def test_model_from_settings_is_applied(self):
        provider = get_ai_provider()
        self.assertEqual(provider.model, "custom-model")
