"""Project-level views (health check, API root)."""

from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """Liveness/health endpoint used by Docker, CI and the frontend."""
    return Response(
        {
            "status": "ok",
            "service": "culture-connects-backend",
            "debug": settings.DEBUG,
        }
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request):
    """Minimal API index for the frontend to discover endpoints."""
    return Response(
        {
            "name": "Culture Connects API",
            "health": request.build_absolute_uri("health/"),
        }
    )
