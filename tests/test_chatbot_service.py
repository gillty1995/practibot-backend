from services.chatbot_service import truncate_conversation, reset_conversation

def test_truncate_conversation():
    global conversation_history
    conversation_history = [{"role": "system", "content": "You are a helpful music coach offering practice tips."}]
    for i in range(10):
        conversation_history.append({"role": "user", "content": f"Message {i}"})
    truncate_conversation(max_messages=5)
    assert len(conversation_history) == 5
    assert conversation_history[0]["role"] == "system"

def test_reset_conversation():
    global conversation_history
    conversation_history.append({"role": "user", "content": "Test message"})
    reset_conversation()
    assert len(conversation_history) == 1
    assert conversation_history[0]["role"] == "system"