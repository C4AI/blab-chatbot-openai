"""This module interacts with the APIs of OpenAI and BLAB Controller."""

from collections import deque
from typing import Any

import openai
from blab_chatbot_bot_client.conversation_websocket import (
    WebSocketBotClientConversation,
)
from blab_chatbot_bot_client.data_structures import (
    Message,
    MessageType,
    OutgoingMessage,
)
from overrides import overrides

from blab_chatbot_openai.openai_settings_format import BlabOpenAIClientSettings


class OpenAIWebSocketBotClientConversation(
    WebSocketBotClientConversation[BlabOpenAIClientSettings]
):
    """Performs the communication between OpenAI and BLAB Controller."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Create an instance. The history deque is initialized as empty."""
        super().__init__(*args, **kwargs)
        self.last_messages: deque[dict[str, Any]] = deque(
            maxlen=max(1, self.settings.OPENAI_SETTINGS["HISTORY_SIZE"])
        )

    @overrides
    def on_connect(self) -> None:
        greeting = OutgoingMessage(
            type=MessageType.TEXT,
            text="Hello!",
            local_id=self.generate_local_id(),
        )
        self.enqueue_message(greeting)

    @overrides
    def on_receive_message(self, message: Message) -> None:
        if message.sent_by_human and message.type == MessageType.TEXT:
            for answer in self.generate_answer(message):
                self.enqueue_message(answer)

    @overrides
    def generate_answer(self, message: Message) -> list[OutgoingMessage]:
        self.last_messages.append(
            {
                "role": "user",
                "content": message.text,
            }
        )
        openai.api_key = self.settings.OPENAI_SETTINGS["API_KEY"]
        match self.settings.OPENAI_SETTINGS["COMPLETION_CLASS"]:
            case "openai.ChatCompletion":
                r = openai.ChatCompletion.create(
                    messages=[*self.last_messages],
                    **self.settings.OPENAI_SETTINGS["COMPLETION_CREATE_ARGS"],
                )
                generated_answer = r["choices"][0]["message"]["content"]
            case "openai.Completion":
                r = openai.Completion.create(
                    prompt=message.text,
                    **self.settings.OPENAI_SETTINGS["COMPLETION_CREATE_ARGS"],
                )
                generated_answer = r["choices"][0]["text"]
            case _:
                raise ValueError("Invalid value for COMPLETION_CLASS")
        self.last_messages.append(
            {
                "role": "assistant",
                "content": generated_answer,
            }
        )
        return [
            OutgoingMessage(
                type=MessageType.TEXT,
                text=generated_answer,
                local_id=self.generate_local_id(),
                quoted_message_id=message.id,
            )
        ]
