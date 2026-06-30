from app.state.image_state import ImageState
from app.llm.client import get_llm
from app.prompts.prompt_templates import PROMPT_ENHANCER_TEMPLATE


def prompt_agent(state: ImageState) -> ImageState:
    """
    Enhances the user's image prompt using Groq.
    """

    print("\n📝 Prompt Agent Started...")

    llm = get_llm()

    prompt = PROMPT_ENHANCER_TEMPLATE.format(
        user_prompt=state.prompt
    )

    response = llm.invoke(prompt)

    state.optimized_prompt = response.content.strip()

    print("Optimized Prompt:")
    print(state.optimized_prompt)

    return state