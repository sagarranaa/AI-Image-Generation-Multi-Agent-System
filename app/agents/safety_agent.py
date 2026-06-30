from app.state.image_state import ImageState
from app.llm.client import get_llm
from app.prompts.prompt_templates import SAFETY_CHECK_TEMPLATE


def safety_agent(state: ImageState) -> ImageState:
    """
    Checks whether the optimized prompt is safe.
    """

    print("\n Safety Agent Started...")

    llm = get_llm()

    prompt = SAFETY_CHECK_TEMPLATE.format(
        prompt=state.optimized_prompt
    )

    response = llm.invoke(prompt)

    answer = response.content.strip().upper()

    state.is_safe = answer == "SAFE"

    if state.is_safe:
        print("✅ Prompt is SAFE")
    else:
        print("❌ Prompt is UNSAFE")

    return state