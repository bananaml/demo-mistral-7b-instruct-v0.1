from potassium import Potassium, Request, Response
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Potassium("mistral-7b-instruct-v0.1")

@app.init
def init() -> dict:
    """Initialize the application with the model and tokenizer."""
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
    context = {
        "model": model,
        "tokenizer": tokenizer
    }
    return context

@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    """Handle a request to generate text from a prompt."""
    model = context.get("model")
    tokenizer = context.get("tokenizer")
    max_new_tokens = request.json.get("max_new_tokens", 512)
    prompt = request.json.get("prompt")
    device = "cuda"
    text = prompt
    encodeds = tokenizer(text, return_tensors="pt", add_special_tokens=False)
    model_inputs = encodeds.to(device)
    model.to(device)
    generated_ids = model.generate(**model_inputs, max_new_tokens=max_new_tokens, do_sample=True)
    decoded = tokenizer.batch_decode(generated_ids)
    result = decoded[0]
    return Response(json={"outputs": result}, status=200)

if __name__ == "__main__":
    app.serve()