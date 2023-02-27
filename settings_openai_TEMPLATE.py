"""This module contains settings for Haystack."""

from __future__ import annotations

from typing import Any

OPENAI_SETTINGS: dict[str, Any] = {
    'API_KEY': '...........',
    "COMPLETION_CREATE_ARGS": {
        # see: https://platform.openai.com/docs/api-reference/completions/create?lang=python
        "model": "text-davinci-003",
        "max_tokens": 25,
    }
}

BLAB_CONNECTION_SETTINGS: dict[str, str | int] = {
    "BOT_HTTP_SERVER_HOSTNAME": "localhost",
    "BOT_HTTP_SERVER_PORT": 25223,
    "BLAB_CONTROLLER_WS_URL": "ws://localhost:8000",
}
