import openai

from overrides import overrides

from blab_chatbot_bot_client.conversation_websocket import (
    WebSocketBotClientConversation,
)
from blab_chatbot_bot_client.data_structures import (
    OutgoingMessage,
    MessageType,
    Message,
)

from blab_chatbot_openai.gpt3_settings_format import BlabOpenAIClientSettings


class GPT3WebSocketBotClientConversation(WebSocketBotClientConversation):

    settings: BlabOpenAIClientSettings

    @overrides
    def on_connect(self):
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
        openai.api_key = self.settings.OPENAI_SETTINGS['API_KEY']
        gpt3_answer = openai.Completion.create(
            prompt=message.text,
            **self.settings.OPENAI_SETTINGS['COMPLETION_CREATE_ARGS']
        )
        return [OutgoingMessage(
            type=MessageType.TEXT,
            text=gpt3_answer['choices'][0]['text'],
            local_id=self.generate_local_id(),
        )]
