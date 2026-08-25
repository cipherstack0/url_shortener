from functions import convert_to_base62, encode, decode

def test_convert_to_base62():
    assert convert_to_base62(1) == "b"
    assert convert_to_base62(61) == "9"
    assert convert_to_base62(62) == "ba"
    assert convert_to_base62(63) == "bb"
    
def test_convert_to_base62_larger_number():
    assert convert_to_base62(3844) == "baa"
    
def test_encode():
    result = encode("https://example.com")

    assert result.startswith("http://localhost:5000/")
    assert len(result) > len("http://localhost:5000/")
    
    

def test_decode():
    result = encode("https://example.com")
    original_url = decode(result)
    assert original_url == "https://example.com"
    
def test_fail_non_existent_decode():
    result = decode("http://localhost:5000/random")
    assert result == "URL not found"
    
def test_encode_adds_https():
    short_url = encode("example.com")

    assert decode(short_url) == "https://example.com"