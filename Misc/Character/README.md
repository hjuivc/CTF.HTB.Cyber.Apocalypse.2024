# Character

After I pressed the initial command I did see that I did return one character for each index. So I did create a bash script for automating the process:
```sh
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
```

After running the script I did get the flag:
```sh
──(kali㉿kali)-[~/Documents/HTB/CyberApocalypse/Character]
└─$ ./getCharacter.sh       



H

HT

HTB

HTB{

HTB{t

HTB{tH

HTB{tH1

HTB{tH15

HTB{tH15_

HTB{tH15_1

HTB{tH15_1s                                                                                                                                                   
                                                                                                                                                              
HTB{tH15_1s_                                                                                                                                                  
                                                                                                                                                              
HTB{tH15_1s_4

HTB{tH15_1s_4_                                                                                                                                                
                                                                                                                                                              
HTB{tH15_1s_4_r                                                                                                                                               

HTB{tH15_1s_4_r3

HTB{tH15_1s_4_r3a

HTB{tH15_1s_4_r3aL

HTB{tH15_1s_4_r3aLl

HTB{tH15_1s_4_r3aLly

HTB{tH15_1s_4_r3aLly_

HTB{tH15_1s_4_r3aLly_l

HTB{tH15_1s_4_r3aLly_l0

HTB{tH15_1s_4_r3aLly_l0n

HTB{tH15_1s_4_r3aLly_l0nG

HTB{tH15_1s_4_r3aLly_l0nG_

HTB{tH15_1s_4_r3aLly_l0nG_f

HTB{tH15_1s_4_r3aLly_l0nG_fL

HTB{tH15_1s_4_r3aLly_l0nG_fL4

HTB{tH15_1s_4_r3aLly_l0nG_fL4g

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0U

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_t

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_s

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sC

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1p

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pT

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTE

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_t

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_o

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_e

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_el

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_i

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0o

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_q

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0n

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!

HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!

Complete flag: HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}

```
