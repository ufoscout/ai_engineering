# How to use

1. Pull a model Locally
   `ollama pull qwen2:7b`

2. Start Ollama in the background
   `ollama serve`

If you run into the error “listen tcp 127.0.0.1:11434: bind: address already in use”, you can use command sudo lsof -i :11434 to identify the process ID (PID) that is currently using this port. If the process is ollama, it is likely that the installation script above has started ollama service, so you can skip this command to start Ollama.

To use LiteLLMModel instead of InferenceClientModel, module in smolagents, you may run pip command to install the module:
`pip install 'smolagents[litellm]'`

From Python:

```python
from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)
```
