import random
import string

url_mapping = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(long_url):
    short_code = generate_short_code()
    url_mapping[short_code] = long_url
    return short_code

def redirect_to_url(short_code):
    return url_mapping.get(short_code, "URL not found")

def go_home():
    return "Redirecting to: https://www.amazon.in/"  ##Add the home directory here

if __name__ == '__main__':
    while True:
        action = input("Enter 'shorten' to shorten a URL or 'redirect' to visit a URL: ")
        if action == 'shorten':
            long_url = input("Enter the long URL: ")
            short_code = shorten_url(long_url)
            print(f"Shortened URL: http://authentica.ly/{short_code}")
        elif action == 'redirect':
            short_code = input("Enter the short URL code: ")
            print(f"Redirecting to: {redirect_to_url(short_code)}")
        elif action == 'home':
            print(go_home())
        else:
            print("Invalid action. Try again.")
