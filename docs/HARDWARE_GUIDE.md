# Hardware Requirements for Running Local Coding LLMs

A sizing guide for developers choosing GPUs, RAM, and quantization formats to run open-weight coding models privately on local hardware.

| Model Size | Quantization | Minimum VRAM / Unified RAM | Recommended GPU | Typical Tokens/Sec |
| :--- | :---: | :---: | :--- | :---: |
| **0.5B - 1.5B** | FP16 / Q8 | 2 GB - 4 GB | Any modern laptop (CPU/GPU) | 60 - 120 |
| **7B** | Q4_K_M | 6 GB | RTX 3060 / 4060 (8GB) | 35 - 55 |
| **7B** | Q8_0 | 10 GB | RTX 3080 / 4070 (12GB) | 30 - 45 |
| **14B** | Q4_K_M | 10 GB - 12 GB | RTX 3080 / 4070 / Apple M2 (16GB) | 25 - 40 |
| **14B** | FP16 | 30 GB | RTX 3090 / 4090 / Apple M2 Max | 20 - 35 |
| **32B** | Q4_K_M | 20 GB - 24 GB | RTX 3090 / 4090 (24GB) or Mac (32GB+) | 15 - 28 |
| **32B** | Q8_0 | 36 GB | 2x RTX 3090 / Mac Studio (64GB) | 12 - 22 |

### Recommendations by Budget:
- **Budget ($0):** Run `qwen2.5-coder:7b` via Ollama on existing 8GB/16GB laptop RAM (CPU inference at 8-15 tok/s).
- **Pro Developer ($1,000 - $1,800):** Single RTX 4070 Ti Super (16GB) or Apple M3 Mac (36GB) running `qwen2.5-coder:14b` at blazing interactive speeds.
- **Research / High Throughput:** Dual RTX 3090 (48GB total VRAM) or Apple M2 Ultra (64GB-128GB) running unquantized 32B models.
