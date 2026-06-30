import os
from datetime import datetime

from app.state.image_state import ImageState
from app.services.image_service import generate_image

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def image_agent(state: ImageState) -> ImageState:

    print("\n🖼️ Image Agent Started...")

    final_prompt = (
        f"{state.optimized_prompt}, "
        f"Style: {state.style}"
    )

    image_bytes = generate_image(final_prompt)

    filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

    image_path = os.path.join(
        OUTPUT_DIR,
        filename
    )

    with open(image_path, "wb") as f:
        f.write(image_bytes)

    state.image_url = image_path

    print(f"✅ Image Saved: {image_path}")

    return state