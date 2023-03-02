"""This module is called from the command-line."""

from sys import argv

from blab_chatbot_bot_client.cli import BlabBotClientArgParser

from blab_chatbot_openai.conversation_openai import OpenAIWebSocketBotClientConversation

BlabBotClientArgParser(OpenAIWebSocketBotClientConversation).parse_and_run(argv[1:])
