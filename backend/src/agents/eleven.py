import os
import sys
import signal
import logging

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# añade logger
logger = logging.getLogger(__name__)

def main():
    AGENT_ID = os.environ.get('AGENT_ID')
    API_KEY = os.environ.get('ELEVEN_API_KEY')

    if not AGENT_ID:
        sys.stderr.write("AGENT_ID environment variable must be set\n")
        sys.exit(1)

    if not API_KEY:
        sys.stderr.write("ELEVEN_API_KEY not set, assuming the agent is public\n")

    client = ElevenLabs(api_key=API_KEY)
    conversation = Conversation(
        client,
        AGENT_ID,
        requires_auth=bool(API_KEY),
        audio_interface=DefaultAudioInterface(),
        callback_agent_response=lambda response: (
            print(f"Agent: {response}"),
            logger.info(f"🗣️ Agent (audio): {response}")
        ),
        callback_agent_response_correction=lambda original, corrected: (
            print(f"Agent: {original} -> {corrected}"),
            logger.info(f"🗣️ Agent corrected: {original} -> {corrected}")
        ),
        callback_user_transcript=lambda transcript: (
            print(f"User: {transcript}"),
            logger.info(f"👤 User said: {transcript}")
        ),
    )
    conversation.start_session()

    signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())

    conversation_id = conversation.wait_for_session_end()
    print(f"Conversation ID: {conversation_id}")
    logger.info(f"🗣️ Conversation ID ended: {conversation_id}")

if __name__ == '__main__':
    main()
