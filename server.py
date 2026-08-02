from flask import Flask, request, jsonify
import torch
from model import GPT, GPTConfig
import tiktoken

enc = tiktoken.get_encoding("gpt2")

def encode(text):
    return enc.encode(text)

def decode(tokens):
    return enc.decode(tokens)

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"

ckpt = torch.load("model/ckpt.pt", map_location=device)

model = GPT(GPTConfig(**ckpt["model_args"]))
model.load_state_dict(ckpt["model"])
model.to(device)
model.eval()


@app.post("/ai")
def ai():
    text = request.json["text"]

    tokens = torch.tensor([encode(text)]).to(device)

    with torch.no_grad():
        out = model.generate(tokens, max_new_tokens=100)

    response = decode(out[0].tolist())

    return jsonify({"response": response})


app.run(host="127.0.1.1", port=5000)
