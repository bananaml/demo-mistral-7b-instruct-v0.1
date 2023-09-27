from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer

def download_model() -> tuple:
    """Download the model and tokenizer."""
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
    return model, tokenizer

if __name__ == "__main__":
    download_model()