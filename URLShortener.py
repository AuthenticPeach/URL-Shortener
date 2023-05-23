import hashlib

class URLShortener:
    def __init__(self):
        self.database = {}
    
    def shorten_url(self, long_url):
        hash_value = self._hash_url(long_url)
        short_url = hash_value[:8]  # Use the first 8 characters of the hash value as the short URL
        self.database[short_url] = long_url
        return short_url
    
    def expand_url(self, short_url):
        if short_url in self.database:
            return self.database[short_url]
        else:
            return "Invalid short URL"
    
    def _hash_url(self, long_url):
        hash_object = hashlib.sha256(long_url.encode())
        return hash_object.hexdigest()

# Example usage
shortener = URLShortener()

while True:
    long_url = input("Enter the URL to shorten (or 'exit' to quit): ")
    
    if long_url.lower() == "exit":
        break
    
    short_url = shortener.shorten_url(long_url)
    print(f"Short URL: {short_url}")

    expanded_url = shortener.expand_url(short_url)
    print(f"Expanded URL: {expanded_url}")
