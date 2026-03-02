from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.exceptions import (
    ValidationError,
    AuthenticationFailed,
    NotAuthenticated,
    PermissionDenied
)


def custom_exception_handler(exc, context):
    """
    Global exception handler for DRF
    """

    response = exception_handler(exc, context)

    # Handle known DRF / Django exceptions
    if isinstance(exc, ValidationError):
        return Response(
            {
                "success": False,
                "message": "Validation error",
                "errors": response.data if response else None
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        return Response(
            {
                "success": False,
                "message": "Authentication credentials were not provided or invalid",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    if isinstance(exc, PermissionDenied):
        return Response(
            {
                "success": False,
                "message": "You do not have permission to perform this action",
            },
            status=status.HTTP_403_FORBIDDEN
        )

    if isinstance(exc, Http404):
        return Response(
            {
                "success": False,
                "message": "Resource not found",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    # Fallback for unhandled exceptions (500)
    if response is None:
        return Response(
            {
                "success": False,
                "message": "Internal server error",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response