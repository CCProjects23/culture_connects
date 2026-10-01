"""Factory that resolves the configured AI provider.

The application asks for a provider by configuration and never imports a
concrete implementation directly – that is what keeps the AI vendor
swappable (AGENT.md §7).
"""

from __future__ import annotations

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .base import AIProvider
from .mock import MockAIProvider

_PROVIDERS: dict[str, type[AIProvider]] = {
    "mock": MockAIProvider,
}


def get_ai_provider(name: str | None = None) -> AIProvider:
    """Return an instance of the configured (or requested) AI provider."""
    provider_name = (name or getattr(settings, "AI_PROVIDER", "mock") or "mock").lower()

    try:
        provider_cls = _PROVIDERS[provider_name]
    except KeyError as exc:
        available = ", ".join(sorted(_PROVIDERS)) or "none"
        raise ImproperlyConfigured(
            f"Unknown AI_PROVIDER '{provider_name}'. Available: {available}."
        ) from exc

    model = getattr(settings, "AI_MODEL", "") or None
    return provider_cls(model=model)
