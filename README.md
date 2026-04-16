# HalLing: A Benchmark for LLM Linguistic Reasoning Hallucination

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

HalLing is a benchmark specifically designed to assess Large Language Models' (LLMs) susceptibility to hallucination when fed with linguistically complex information. Unlike traditional benchmarks that focus on factual retrieval, HalLing identifies model limitations through their ability to interpret, resolve, and reason about linguistically challenging input.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Linguistic Phenomena Covered](#linguistic-phenomena-covered)
- [Models Evaluated](#models-evaluated)
- [Data Format](#data-format)
- [Usage](#usage)
- [Citation](#citation)

## 🎯 Overview

HalLing evaluates LLMs on six core linguistic phenomena that require sophisticated reasoning beyond simple pattern matching. The benchmark tests whether models can:
- Correctly interpret ambiguous sentences
- Resolve anaphoric references
- Process center-embedded structures
- Navigate garden path sentences
- Handle quantifier scope ambiguities
- Reason with first-order logic extensions

## 📁 Repository Structure

```
HalLing/
├── README.md                 # This file
├── Benchmark-test/           # Core benchmark datasets
│   ├── Ambiguity.xlsx
│   ├── Anaphoric.xlsx
│   ├── Anaphoric extended.xlsx
│   ├── Anaphoric_faulty.xlsx
│   ├── Center embedding.xlsx
│   ├── Garden path.xlsx
│   ├── Quantifier.xlsx
│   └── Quantifier_extend.xlsx
├── Llama/                    # Llama model results
├── Mistral/                  # Mistral model results
├── Qwen/                     # Qwen model results
└── GLM4/                     # GLM-4 model results
```

> **Note:** Each model branch contains results for that specific model across different linguistic phenomena and question types (MCQ = Multiple Choice Questions, OQ = Open Questions).

## 🗣️ Linguistic Phenomena Covered

| Phenomenon | Description | Files |
|------------|-------------|-------|
| **Ambiguity** | Sentences with multiple valid interpretations | `Ambiguity.xlsx` |
| **Anaphora** | Pronoun resolution and coreference | `Anaphoric.xlsx`, `Anaphoric extended.xlsx`, `Anaphoric_faulty.xlsx` |
| **Center Embedding** | Nested clause structures | `Center embedding.xlsx` |
| **Garden Path** | Sentences that lead to misinterpretation | `Garden path.xlsx` |
| **Quantifier Scope** | Ambiguities in quantifier interpretation | `Quantifier.xlsx`, `Quantifier_extend.xlsx` |

## 🤖 Models Evaluated

- **Llama** (Meta)
- **Mistral** (Mistral AI)
- **Qwen** (Alibaba Cloud)
- **GLM-4** (Zhipu AI)

Each model was tested on both multiple-choice questions (MCQ) and open-ended questions (OQ) across all linguistic phenomena.

## 📊 Data Format

Excel files (`.xlsx`) contain the following columns:
- **ID**: Unique identifier for each test case
- **Phenomenon**: Linguistic phenomenon being tested
- **Input**: The test sentence or context
- **Question**: The specific question asked
- **Expected Answer**: Ground truth
- **Model Response**: The model's generated response
- **Correct**: Binary indicator of correctness

## 🚀 Usage

### Accessing Data by Branch

Each model's results are stored in separate branches:

```bash
# Clone the repository
git clone https://github.com/EnmingZhang0517/HalLing-A-Benchmark-for-LLM-Linguistic-Reasoning-Hallucination.git
cd HalLing-A-Benchmark-for-LLM-Linguistic-Reasoning-Hallucination

# Switch to a specific model branch
git checkout Llama      # For Llama results
git checkout Mistral    # For Mistral results
git checkout Qwen       # For Qwen results
git checkout GLM4       # For GLM-4 results

# Core benchmark data
git checkout Benchmark-test
```

### Analyzing Results

```python
import pandas as pd

# Load a specific phenomenon
df = pd.read_excel('Llama_MCQ_Ambiguity(done).xlsx')

# Calculate accuracy
accuracy = df['Correct'].mean()
print(f"Accuracy: {accuracy:.2%}")
```

## 📚 Citation

If you use HalLing in your research, please cite:

```bibtex
@misc{zhang2025halling,
  title={HalLing: A Benchmark for LLM Linguistic Reasoning Hallucination},
  author={Enming Zhang},
  year={2025},
  howpublished={\url{https://github.com/EnmingZhang0517/HalLing-A-Benchmark-for-LLM-Linguistic-Reasoning-Hallucination}}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note:** This repository contains the dataset and evaluation results from a master's thesis project on LLM linguistic reasoning capabilities.
