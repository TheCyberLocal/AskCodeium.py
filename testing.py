import pytest
from fastapi.testclient import TestClient
from AskCodeium.main import app

client = TestClient(app)

@pytest.fixture
def thread_id():
    response = client.post("/createChat")
    assert response.status_code == 200
    return response.json()["thread_id"]

def test_create_chat(thread_id):
    assert thread_id is not None

def test_chat_interaction(thread_id):
    # Send a query to the chat thread
    query = "What is the python programming language?"
    response = client.post(f"/chat/{thread_id}", json={"query": query})
    print(response.json()["response"])

    # Ask about the previous question
    query = "What did I previously ask you about?"
    response = client.post(f"/chat/{thread_id}", json={"query": query})
    print(response.json()["response"])

def test_clear_history(thread_id):
    # Send a query to the chat thread
    query = "What is the python programming language?"
    response = client.post(f"/chat/{thread_id}", json={"query": query})
    print(response.json()["response"])

    # Clear the chat history
    response = client.post(f"/chat/{thread_id}/clearHistory")
    assert response.status_code == 200
    assert response.json()["status"] == "History cleared"

    # Send a query again to ensure history is cleared
    query = "What is the python programming language?"
    response = client.post(f"/chat/{thread_id}", json={"query": query})
    print(response.json()["response"])

if __name__ == "__main__":
    pytest.main()
