#!/bin/bash

# Enable debug mode if the first argument is --debug
DEBUG=0
if [ "$1" == "--debug" ]; then
  DEBUG=1
fi

function debug_log {
  if [ "$DEBUG" -eq 1 ]; then
    # Direct debug messages to stderr to not mix with flag output
    echo "Debug: $1" >&2
  fi
}

# Configuration for netcat
HOST="94.237.63.93"
PORT="40248"

# Initialize the index and the flag
index=0
flag=""

# Use a loop to fetch each character of the flag
while :; do
  debug_log "Requesting character at index: $index"
  
  # Use timeout to ensure the command exits, with adjustments for immediate output
  response=$(echo $index | timeout 1 nc $HOST $PORT | tr -d '\0' | grep -oP "Character at Index $index: \K.")
  
  debug_log "Received response: '$response'"
  
  # Check if response is empty or not what we expected
  if [ -z "$response" ]; then
    debug_log "No more characters received or unexpected response, ending loop."
    break
  fi
  
  # Append the received character to the flag
  flag+="$response"
  
  # Print the cumulative characters of the flag in a pyramid-like structure
  for ((i=1; i<=index; i++)); do
    printf "%s" "${flag:i-1:1}"
  done
  printf "\n" # Move to the next line for the next iteration
  
  ((index++)) # Increment the index for the next character
done

# Ensure there's a newline after printing the pyramid
echo "Complete flag: $flag"