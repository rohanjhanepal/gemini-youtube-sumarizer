import gemini
from urllib.parse import urlparse, ParseResult

youtube_variants = ["www.youtu.be.com" , "https://www.youtu.be.com" , "youtu.be.com","youtu.be",
                    "www.youtube.com" , "https://www.youtube.com" , "youtube.com"]

def is_valid_url(url):
    """Checks if the given text is a valid URL.

    Args:
        url (str): The text to be checked.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    parsed_url = urlparse(url)
    # Validate URL structure and required components
    return all([parsed_url.scheme, parsed_url.netloc, parsed_url.path])

def is_youtube_video_url(url):
    """Checks if the given URL is a YouTube video URL.

    Args:
        url (str): The URL to be checked.

    Returns:
        bool: True if the URL is a YouTube video, False otherwise.
    """
    parsed_url = urlparse(url)
    print(parsed_url.netloc)
    
    return (parsed_url.netloc in youtube_variants)

while True:
    prompt = input(">> ")

    if is_valid_url(prompt):
        if is_youtube_video_url(prompt):
            print(prompt)
            print(gemini.generate_summary(prompt))
        else:
            print(f"Error summarizing: Not a youtube video link")
    else:
        print("Invalid URL")
