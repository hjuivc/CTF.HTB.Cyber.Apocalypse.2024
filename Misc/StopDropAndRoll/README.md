# Stop Drop and Roll

The game started like this so I decided to create a script for solving it:
```sh
┌──(kali㉿kali)-[~/Documents/HTB/CyberApocalypse/StopDropAndRoll]
└─$ nc 94.237.55.163 30925
===== THE FRAY: THE VIDEO GAME =====
Welcome!
This video game is very simple
You are a competitor in The Fray, running the GAUNTLET
I will give you one of three scenarios: GORGE, PHREAK or FIRE
You have to tell me if I need to STOP, DROP or ROLL
If I tell you there's a GORGE, you send back STOP
If I tell you there's a PHREAK, you send back DROP
If I tell you there's a FIRE, you send back ROLL
Sometimes, I will send back more than one! Like this: 
GORGE, FIRE, PHREAK
In this case, you need to send back STOP-ROLL-DROP!
Are you ready? (y/n) y
Ok then! Let's go!
GORGE, FIRE, GORGE, GORGE, GORGE
What do you do? STOP-ROLL-STOP-STOP-STOP
GORGE, GORGE
What do you do? STOP-STOP
FIRE, PHREAK
What do you do? ROLL-DROP
PHREAK, GORGE, GORGE, PHREAK
What do you do? DROP-STOP-STOP-DROP
PHREAK, FIRE, PHREAK, GORGE
What do you do? DROP-ROLL-DROP-STOP
GORGE, GORGE, GORGE, FIRE, FIRE
What do you do? STOP-STOP-STOP-ROLL-ROLL
PHREAK, FIRE
What do you do? DROP-ROLL
GORGE, FIRE

```

Since I did create a BASH script last time, did I decide to create the script in Python this time:
```python
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
```

```sh
Sending response: ROLL-STOP-DROP-ROLL
Sending response: ROLL-STOP-DROP-ROLL

Received: FIRE

Received: What do you do? 
FIRE
What do you do? 
Sending response: ROLL
Sending response: ROLL

Received: FIRE, GORGE, FIRE, FIRE

Received: What do you do? 
FIRE, GORGE, FIRE, FIRE
What do you do? 
Sending response: ROLL-STOP-ROLL-ROLL
Sending response: ROLL-STOP-ROLL-ROLL

Received: GORGE, PHREAK, GORGE, PHREAK, PHREAK
What do you do? 
GORGE, PHREAK, GORGE, PHREAK, PHREAK
What do you do? 
Sending response: STOP-DROP-STOP-DROP-DROP
Sending response: STOP-DROP-STOP-DROP-DROP

Received: PHREAK, PHREAK, GORGE
What do you do? 
PHREAK, PHREAK, GORGE
What do you do? 
Sending response: DROP-DROP-STOP
Sending response: DROP-DROP-STOP

Received: FIRE, GORGE

Received: What do you do? 
FIRE, GORGE
What do you do? 
Sending response: ROLL-STOP
Sending response: ROLL-STOP

Received: Fantastic work! The flag is HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}


Timeout waiting for response.
Fantastic work! The flag is HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}

Game over or unexpected data received.

Timeout waiting for response.
No more data received. Exiting.
Trying 'ls' command...
Sending response: ls


Timeout waiting for response.

```