HTTP/1.1 200 OK

Server: Werkzeug/3.0.1 Python/3.11.8

Date: Sun, 10 Mar 2024 17:16:55 GMT

Content-Type: application/json

Content-Length: 637

Connection: close

Under "Target" on Burp i found api/options and here is the options:
```json
{
  "allPossibleCommands": {
    "1": [
      "HEAD NORTH",
      "HEAD WEST",
      "HEAD EAST",
      "HEAD SOUTH"
    ],
    "2": [
      "GO DEEPER INTO THE FOREST",
      "FOLLOW A MYSTERIOUS PATH",
      "CLIMB A TREE",
      "TURN BACK"
    ],
    "3": [
      "EXPLORE A CAVE",
      "CROSS A RICKETY BRIDGE",
      "FOLLOW A GLOWING BUTTERFLY",
      "SET UP CAMP"
    ],
    "4": [
      "ENTER A MAGICAL PORTAL",
      "SWIM ACROSS A MYSTERIOUS LAKE",
      "FOLLOW A SINGING SQUIRREL",
      "BUILD A RAFT AND SAIL DOWNSTREAM"
    ],
    "secret": [
      "Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"
    ]
  }
}
```

I did run input in the browser while intercepting the traffic in Burp and found a POST request to:
```
POST /api/monitor HTTP/1.1

Host: 83.136.250.12:46079

Content-Length: 68

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36

Content-Type: application/json

Accept: */*

Origin: http://83.136.250.12:46079

Referer: http://83.136.250.12:46079/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Connection: close



{"command":"start"}
```

So then I just sent this request to repeater and started to test with the options and with the "secret" it revealed the flag:
```request
POST /api/monitor HTTP/1.1

Host: 83.136.250.12:46079

Content-Length: 68

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36

Content-Type: application/json

Accept: */*

Origin: http://83.136.250.12:46079

Referer: http://83.136.250.12:46079/

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9

Connection: close



{"command":"Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"}
```

```response
HTTP/1.1 200 OK

Server: Werkzeug/3.0.1 Python/3.11.8

Date: Sun, 10 Mar 2024 17:21:06 GMT

Content-Type: application/json

Content-Length: 67

Connection: close



{
  "message": "HTB{D3v3l0p3r_t00l5_4r3_b35t_wh4t_y0u_Th1nk??!}"
}

```