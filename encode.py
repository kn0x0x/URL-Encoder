import urllib.parse

# input
text = ""

# encode
encoded_text = ''.join(f'%{hex(ord(c))[2:].zfill(2)}' for c in text)

print(encoded_text)
