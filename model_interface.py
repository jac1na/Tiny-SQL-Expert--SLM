from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"

print("Loading model... (this may take 20–40 seconds)")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto",   # chooses GPU or CPU automatically
    low_cpu_mem_usage=True
)

def run_model(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    output = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.3,
        do_sample=True
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)
