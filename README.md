# lanAi - Seu Assistente de IA Local e Inteligente

**lanAi** é um assistente de IA generativa construído em Python, projetado para ser executado localmente. Ele pode aprender com seus documentos (PDFs) e outras fontes de dados para fornecer respostas inteligentes e contextualizadas, garantindo total privacidade e controle sobre suas informações.

O nome **lanAi** vem da combinação de **LAN** (Local Area Network) e **AI** (Inteligência Artificial), refletindo sua capacidade de operar em um ambiente local. Curiosamente, "lanai" é também uma palavra havaiana que significa uma varanda coberta ou pátio aberto - um espaço entre o técnico e o prático - assim como este assistente.

---

## ✨ Funcionalidades Principais

- **Aprendizado Local:** Extrai texto de arquivos PDF em um diretório local para construir sua base de conhecimento.
- **Base de Conhecimento Expansível:** Permite a inserção manual de informações, além do aprendizado automático de documentos.
- **Interface de Linha de Comando (CLI):** Um menu interativo e fácil de usar para gerenciar a base de conhecimento e interagir com a IA.
- **Privacidade em Primeiro Lugar:** Como é executado localmente, seus dados nunca saem do seu computador.
- **Modular e Extensível:** O código é organizado em módulos, facilitando a adição de novas funcionalidades e fontes de dados.

---

## 🚀 Como Começar

### Pré-requisitos

- Python 3.x
- As bibliotecas listadas no arquivo `requirements.txt`

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/njfw50/lanAi.git
   cd lanAi
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Coloque os arquivos PDF que você deseja que o lanAi aprenda na pasta `pdfs`.

### Execução

Para iniciar o assistente, execute o script principal:

```bash
python lanAi.py
```

Você será recebido com uma mensagem de boas-vindas e o menu principal, onde poderá escolher entre extrair texto de PDFs, inserir informações manualmente, pesquisar na base de conhecimento ou conversar com a IA.

---

## 🔧 Estrutura do Projeto

- `lanAi.py`: O ponto de entrada principal do aplicativo, contendo o menu e a lógica de interação com o usuário.
- `lanai_core.py`: O "cérebro" do assistente, responsável por processar as perguntas e gerar respostas usando a base de conhecimento.
- `lanAi_storage.py`: Gerencia o banco de dados SQLite onde todo o conhecimento é armazenado.
- `pdfs/`: Diretório onde você deve colocar seus arquivos PDF para aprendizado.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* para relatar bugs ou sugerir novas funcionalidades. Se você quiser contribuir com código, por favor, abra um *pull request*.
