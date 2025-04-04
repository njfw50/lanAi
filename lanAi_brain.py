from llama_cpp import Llama

# Caminho do modelo com nome exato
llm = Llama(model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

# Faça uma pergunta de teste
response = llm("Q: What is LibertyM?\nA:", max_tokens=150)

print("\n🧠 LanAI Response:\n")
print(response["choices"][0]["text"])
