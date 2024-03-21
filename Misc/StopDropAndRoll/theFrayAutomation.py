import socket
import select
import time

# Define the host and port to connect to
HOST = '94.237.48.219'
PORT = 48298

# Mapping of game scenarios to responses
responses = {
    'GORGE': 'STOP',
    'PHREAK': 'DROP',
    'FIRE': 'ROLL'
}

# Additional variable to keep track of repeated patterns or challenge count
challenge_history = []

# Create a socket object and connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(0)  # Set socket to non-blocking mode

def send_message(message):
    try:
        print(f"Sending response: {message}")  # Log sending message
        s.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending message: {e}")

def receive_with_timeout(timeout=2):
    total_data = []
    end_time = time.time() + timeout
    while True:
        # Adjust to check against the end_time to ensure proper timeout handling
        remaining_time = end_time - time.time()
        if remaining_time <= 0:
            print("\nTimeout waiting for response.")
            break

        ready = select.select([s], [], [], remaining_time)
        if ready[0]:
            try:
                data = s.recv(1024).decode('utf-8')
                if data:
                    print(f"Received: {data}")  # Log received data
                    total_data.append(data)
                    if "What do you do?" in data:
                        break
            except Exception as e:
                print(f"Error receiving data: {e}")
                break
    return ''.join(total_data)

print(receive_with_timeout())
send_message("y\n")

try:
    while True:
        data = receive_with_timeout()

        if not data:
            print("No more data received. Exiting.")
            break

        print(data)

        if "What do you do?" in data:
            challenge = data.strip().split('\n')[-2]
            challenge_history.append(challenge)  # Track each challenge

            actions = [responses.get(scenario, 'UNKNOWN') for scenario in challenge.split(', ')]
            response = '-'.join(actions)
            print(f"Sending response: {response}")
            send_message(response + '\n')
        else:
            print("Game over or unexpected data received.")

    # After the game loop ends, try sending an 'ls' command
    print("Trying 'ls' command...")
    send_message("ls\n")
    # Wait a bit for any response
    print(receive_with_timeout(timeout=5))
except KeyboardInterrupt:
    print("Interrupted by user. Exiting.")
finally:
    s.close()