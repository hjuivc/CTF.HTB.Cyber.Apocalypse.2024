# Box Cutter

![Photo](20240311200826.png)

md5: be3a30fbe34816c324288f0bdb3a0dbd
sha256: c08975de9d50b6e44e7e12296ba44fd51d31d5a6fb6a7fb5b904b0bfc33cb955
crc32: 32a9db57

```python
encrypted_bytes = [
    0x54, 0x03, 0x45, 0x43, 0x4C, 0x75, 0x63, 0x7f,
    0x45, 0xf4, 0x36, 0x85, 0x05, 0x90, 0x6, 0x68,
    0x37, 0x4a, 0x02, 0x5b, 0x5b, 0x03, 0x54
]

# Reverse the byte array before XOR operation
encrypted_bytes = encrypted_bytes[::-1]

filename = ''.join(chr(b ^ 0x37) for b in encrypted_bytes)
print(f'Decrypted filename: {filename}')

```