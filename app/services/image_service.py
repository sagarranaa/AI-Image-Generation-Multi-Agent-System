import requests
from urllib.parse import quote


def generate_image(prompt: str) -> bytes:
    """
    Generate image using Pollinations AI.
    Returns image bytes.
    """

    print("\n🖼️ Calling Pollinations AI...")

    url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    response = requests.get(url, timeout=300)

    if response.status_code != 200:
        raise Exception(
            f"Image Generation Failed\n"
            f"{response.status_code}\n"
            f"{response.text}"
        )

    print("✅ Image Generated Successfully")

    return response.content