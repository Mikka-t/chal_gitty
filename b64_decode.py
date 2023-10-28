import base64

def b64_decode():
    b64_text = input("Enter the base64 text: ")

    try:
        decoded_bytes = base64.b64decode(b64_text)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        return f"An error occurred: {e}"
