from typing import Protocol, TypedDict, runtime_checkable

from blab_chatbot_bot_client.settings_format import BlabBotClientSettings


# noinspection SpellCheckingInspection
class OpenAICompletionCreateArgs(TypedDict):
    # see: https://platform.openai.com/docs/api-reference/completions/create?lang=python

    model: str
    max_tokens: int
    temperature: float
    top_p: float
    n: int
    stream: bool
    logprobs: int
    stop: str | list[str]
    presence_penalty: float
    frequency_penalty: float
    best_of: int
    logit_bias: dict[str, float]
    user: str


class OpenAISettings(TypedDict):

    API_KEY: str

    COMPLETION_CREATE_ARGS: OpenAICompletionCreateArgs


@runtime_checkable
class BlabOpenAIClientSettings(BlabBotClientSettings, Protocol):
    OPENAI_SETTINGS: OpenAISettings
