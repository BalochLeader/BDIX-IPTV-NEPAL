
import requests
import json

def generate_m3u_playlist(channels_data):
    m3u_content = "#EXTM3U\n"
    for channel in channels_data["channels"]:
        name = channel.get("name", "Unknown Channel")
        url = channel.get("url", "")
        if url:
            m3u_content += f"#EXTINF:-1 tvg-name=\"{name}\",{name}\n{url}\n"
    return m3u_content

def fetch_channels_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching channels data: {e}")
        return None

if __name__ == "__main__":
    # URL to the raw Channels_data.json in the reference repository
    json_url = "https://raw.githubusercontent.com/abusaeeidx/Mrgify-BDIX-IPTV/main/Channels_data.json"
    
    channels_data = fetch_channels_data(json_url)
    
    if channels_data:
        m3u_playlist = generate_m3u_playlist(channels_data)
        with open("playlist.m3u", "w") as f:
            f.write(m3u_playlist)
        print("M3U playlist generated successfully!")
    else:
        print("Failed to generate M3U playlist.")
