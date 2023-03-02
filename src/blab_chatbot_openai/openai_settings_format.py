"""This module defines the expected format of the configuration file.

See the file `settings_openai_TEMPLATE.py` for a template.
"""

from typing import Literal, Protocol, TypedDict, runtime_checkable

from blab_chatbot_bot_client.settings_format import BlabBotClientSettings


# noinspection SpellCheckingInspection
class OpenAICompletionCreateArgs(TypedDict):
    """Contains arguments used to create an instance of Completion/ChatCompletion.

    The field "prompt" or "messages" is included automatically and should not
    be in the settings file.

    See the documentation:
    https://platform.openai.com/docs/api-reference/completions/create?lang=python
    and
    https://platform.openai.com/docs/api-reference/chat/create?lang=python
    """

    # see:

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
    """Contains parameters related to the OpenAI service."""

    API_KEY: str

    COMPLETION_CREATE_ARGS: OpenAICompletionCreateArgs

    COMPLETION_CLASS: Literal["openai.Completion", "openai.ChatCompletion"]


@runtime_checkable
class BlabOpenAIClientSettings(BlabBotClientSettings, Protocol):
    """This protocol should be implemented by the configuration file.

    It extends the parent protocol (`BlabBotClientSettings`)
    with the inclusion of the `OpenAISettings` field.
    """

    OPENAI_SETTINGS: OpenAISettings
