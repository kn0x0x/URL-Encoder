URL Encoding & Decoding for CTF Challenges

This repository contains two Python scripts, encode.py and decode.py, designed for encoding and decoding text using URL encoding. These scripts are useful for CTF (Capture The Flag) challenges that involve URL encoding techniques.

Files

encode.py: Converts a given text into URL-encoded format.

decode.py: Decodes a given URL-encoded string back to its original text.

Usage

Encoding a string

python3 encode.py "your_text_here"

Example:

python3 encode.py "alpaca"
# Output: %61%6c%70%61%63%61

Decoding a string

python3 decode.py "%61%6c%70%61%63%61"

Example:

python3 decode.py "%61%6c%70%61%63%61"
# Output: alpaca

Purpose

These scripts are created for CTF challenges where URL encoding is required to bypass filters, encode payloads, or solve encoding-related tasks.

Feel free to modify and use them for learning purposes!

License

This project is open-source under the MIT License.
