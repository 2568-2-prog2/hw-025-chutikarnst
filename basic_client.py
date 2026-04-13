import requests

def call_api(base_url, payload):
    try:
        # Use POST for sending JSON bodies
        response = requests.post(base_url, json=payload)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        # If the server sent a 400, try to print the server's error message
        if hasattr(e, 'response') and e.response is not None:
            print(f"Server says: {e.response.text}")
        return None

if __name__ == "__main__":
    url = "http://127.0.0.1:8081/roll_dice"
    data = {
        "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],
        "number_of_random": 10 
    }
    result = call_api(url, data)
    
    # FIX: Only loop if result is not None
    if result is not None:
        print("Success! Results:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("Failed to get results from the API.")