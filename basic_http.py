import socket
import json
from dice import BiasedDice

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Prevents "Address already in use"
server_socket.bind(('localhost', 8081))
server_socket.listen(1)
print("Server is listening on port 8081...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(4096).decode('utf-8')

    if not request:
        client_socket.close()
        continue

    parts = request.split('\r\n\r\n')
    header = parts[0]
    body = parts[1] if len(parts) > 1 else ""

    if "/roll_dice" in header:
        try:
            if not body:
                raise ValueError("No JSON body received")
                
            data = json.loads(body)
            dice = BiasedDice(data['probabilities'])
            results = dice.roll(data['number_of_random'])
            
            response_json = json.dumps({"status": "success", "results": results})
            response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{response_json}"
        except Exception as e:
            # Send back the specific error as JSON
            error_json = json.dumps({"status": "error", "message": str(e)})
            response = f"HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n\r\n{error_json}"

    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()