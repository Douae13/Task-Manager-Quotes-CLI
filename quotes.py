import requests

def get_quote():
    try:
        request = requests.get("https://api.quotable.io/random")
        data = request.json()
        return f"{data['content']} — {data['author']}"
    except:
        return "Stay consistent. Small progress daily."