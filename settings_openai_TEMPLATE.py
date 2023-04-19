"""A module that contains settings for OpenAI."""

from __future__ import annotations

from typing import Any

# fmt: off


BLAB_CONNECTION_SETTINGS: dict[str, str | int] = {

    # Address of the local HTTP server that the controller will connect to:
    "BOT_HTTP_SERVER_HOSTNAME": "127.0.0.1",

    # Port of the aforementioned server:
    "BOT_HTTP_SERVER_PORT": 25223,

    # BLAB Controller address for WebSocket connections:
    "BLAB_CONTROLLER_WS_URL": "ws://localhost:8000",

}


OPENAI_SETTINGS: dict[str, Any] = {

    # OpenAI API key (possibly dynamically obtained from a safe storage location):
    "API_KEY": "...........",

    # "openai.ChatCompletion" or "openai.Completion", depending on the model:
    "COMPLETION_CLASS": "openai.ChatCompletion",

    # Number of previous messages to send to the server (only for ChatCompletion):
    "HISTORY_SIZE": 10,

    # Arguments to create the completion instance (see documentation at:
    # <https://platform.openai.com/docs/api-reference/completions/create?lang=python>
    # and
    # <https://platform.openai.com/docs/api-reference/chat/create?lang=python>):
    "COMPLETION_CREATE_ARGS": {
        "model": "text-davinci-003",
        "max_tokens": 25,
    },

}
