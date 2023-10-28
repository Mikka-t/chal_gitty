import urllib.parse

def url_decode():
    encoded_string = input("Enter the encoded string: ")
    try:
        decoded_string = urllib.parse.unquote(encoded_string)
    except Exception as e:
        return f"Error: {e}"
    return decoded_string