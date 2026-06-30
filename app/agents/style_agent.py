from app.state.image_state import ImageState
from app.llm.client import get_llm
from app.prompts.prompt_templates import STYLE_SELECTION_TEMPLATE


def style_agent(state: ImageState) -> ImageState:
    """
    Select the best image style using the LLM.
    """

    print("\n🎨 Style Agent Started...")

    llm = get_llm()

    prompt = STYLE_SELECTION_TEMPLATE.format(
        prompt=state.optimized_prompt
    )

    response = llm.invoke(prompt)

    state.style = response.content.strip()

    print(f"Selected Style: {state.style}")

    return state