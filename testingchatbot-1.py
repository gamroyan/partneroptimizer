import requests
import json

def send_to_openai(messages):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    payload = {
        "model": "gpt-4",
        "messages": messages
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

OPENAI_API_KEY = "<open ai key>"

def chat():
    print("Welcome to the AI assistant!")
    user_name = input("What's your name? ")
    company_name = input("What's your companys name? ")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": f"Hello {user_name} from {company_name}! \nHow can I help you today?"}
    ]
    
    print(f"\n{messages[-1]['content']}")

    while True:
        user_input = input(f"\n{user_name}: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Thank you for chatting. Goodbye!")
            break
        
        messages.append({"role": "user", "content": user_input})
        
        openai_response = send_to_openai(messages)
        
        if openai_response and 'choices' in openai_response and len(openai_response['choices']) > 0:
            ai_message = openai_response['choices'][0]['message']['content']
            print(f"\n{ai_message}")
            messages.append({"role": "assistant", "content": ai_message})
        else:
            print("Sorry, I couldn't generate a response.")

    # print summary after the chat ends
    print("\n----- Raw Messages Data -----")
    print(json.dumps(messages, indent=2))

if __name__ == "__main__":
    chat()

