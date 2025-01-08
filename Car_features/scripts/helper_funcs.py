import chardet

def get_encoding(loc):
    """Reads encoding from given file."""
    with open(loc, "rb") as f:
        result = chardet.detect(f.read())
        return result["encoding"]