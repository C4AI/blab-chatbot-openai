from sys import argv

from blab_chatbot_bot_client.cli import BlabBotClientArgParser

from blab_chatbot_openai.conversation_openai import GPT3WebSocketBotClientConversation

BlabBotClientArgParser(GPT3WebSocketBotClientConversation).parse_and_run(argv[1:])
