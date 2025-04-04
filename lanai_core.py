import sys
import os
import subprocess
import re

def run_lanai_core(prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "⚠️ No prompt provided."

    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "models", "mistral-7b-instruct-v0.1.Q4_K_M.gguf")
    executable = os.path.join(base_dir, "llama_runtime", "llama-run.exe")

    full_prompt = f"<|im_start|>user\n{prompt.strip()}\n<|im_end|>\n<|im_start|>assistant"

    command = [executable, model_path, full_prompt]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        output = ""
        for line in process.stdout:
            output += line

        return clean_output(output)

    except Exception as e:
        return f"\n❌ Error while running the model: {e}"

def clean_output(text: str) -> str:
    # Remove tags como <|im_start|> e <|im_end|>
    cleaned = re.sub(r"<\|.*?\|>", "", text)
    # Remove múltiplas quebras de linha iniciais e finais
    cleaned = cleaned.strip()
    return cleaned

# Execução direta via terminal
if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]).strip()
    result = run_lanai_core(prompt)
    print(result)
