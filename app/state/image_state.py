from typing import Optional
from pydantic import BaseModel

class ImageState(BaseModel):
      """
      Shared state used by all LangGraph agents.
      """
      #user input
      prompt:str
      # prompt after prompt agent
      optimized_prompt: Optional[str] = None
      #style selected by style agent
      style: Optional[str] = None
      #Safety check result
      is_safe: Optional[bool] = None
      # Generated image URL
      image_url: Optional[str] = None
      # Quality score (1-10)
      quality_score: Optional[float] = None
      # Number of retries
      retry_count:int=0