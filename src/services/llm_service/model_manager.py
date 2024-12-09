from typing import Optional
import torch

class ModelManager:
    def __init__(self):
        self.model = None
        self.tokenizer = None
    
    def load_model(self, model_name: str) -> None:
        """
        Load a model and tokenizer into memory
        """
        pass
    
    def generate(self, prompt: str) -> str:
        """
        Generate text based on the prompt
        """
        pass
