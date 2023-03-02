"""This module contains settings for Haystack."""

from __future__ import annotations

from typing import Any

OPENAI_SETTINGS: dict[str, Any] = {
    # OpenAI API key
    "API_KEY": "...........",
    #
    # "openai.ChatCompletion" or "openai.Completion", depending on the model
    "COMPLETION_CLASS": "",
    #
    # arguments to create the completion instance - see documentation:
    # https://platform.openai.com/docs/api-reference/completions/create?lang=python
    # and
    # https://platform.openai.com/docs/api-reference/chat/create?lang=python
    "COMPLETION_CREATE_ARGS": {
        "model": "text-davinci-003",
        "max_tokens": 25,
    },
}

BLAB_CONNECTION_SETTINGS: dict[str, str | int] = {
    "BOT_HTTP_SERVER_HOSTNAME": "localhost",
    "BOT_HTTP_SERVER_PORT": 25223,
    "BLAB_CONTROLLER_WS_URL": "ws://localhost:8000",
}
