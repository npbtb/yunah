import requests
from bs4 import BeautifulSoup

def get_playlist_videos(playlist_url):
    # Get the page content
    response = requests.get(playlist_url)
    if response.status_code != 200:
        print("Failed to fetch playlist. Check the URL and try again.")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract video titles and links
    videos = []
    for video in soup.find_all('a', {'id': 'video-title'}):
        title = video.text.strip()
        video_url = "https://www.youtube.com" + video['href']
        videos.append((title, video_url))

    return videos

def create_html_gallery(videos, output_file="gallery.html"):
    # Basic HTML structure
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>YouTube Playlist Gallery</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f9f9f9; text-align: center; }
            .container { width: 80%; margin: auto; }
            .video { margin: 20px 0; }
            iframe { width: 560px; height: 315px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>YouTube Playlist Gallery</h1>
    """

    # Add each video to the HTML
    for title, video_url in videos:
        video_id = video_url.split('v=')[1].split('&')[0]
        html_content += f"""
            <div class="video">
                <h2>{title}</h2>
                <iframe src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
            </div>
        """

    # Close the HTML structure
    html_content += """
        </div>
    </body>
    </html>
    """

    # Save to a file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Gallery saved to {output_file}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    videos = get_playlist_videos(playlist_url)
    if videos:
        create_html_gallery(videos)
