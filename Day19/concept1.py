from langchain_core.chat_history import InMemoryChatMessageHistory

# create memory
history = InMemoryChatMessageHistory()

# add messages
history.add_user_message("What is RAG?")
history.add_ai_message("RAG stands for Retrieval Augmented Generation.")
history.add_user_message("Give me an example.")
history.add_ai_message("Imagine uploading a PDF and asking questions about it.")

# view all messages

print("="*50+"\n")
print(type(history))
print("="*50+"\n")

print(history)
print("="*50+"\n")
print(type(history.messages))
print("="*50+"\n")

for msg in history.messages:
    print(f"{msg.type.upper()}: {msg.content}")

print(f"\nTotal messages: {len(history.messages)}")