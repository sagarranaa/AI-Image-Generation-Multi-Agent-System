from app.state.image_state import ImageState
from app.agents.safety_agent import safety_agent
from app.agents.prompt_agent import prompt_agent
from app.agents.style_agent import style_agent
from app.agents.image_agent import image_agent




def main():

    state = ImageState(
        prompt="geneate Dog images"
    )

    state = prompt_agent(state)
    state = safety_agent(state)
    if not state.is_safe:
        print("unsafe prompt")
        return
    state=style_agent(state)
    state=image_agent(state)

    print("\n========== FINAL STATE ==========")
    print(state)


if __name__ == "__main__":
    main()