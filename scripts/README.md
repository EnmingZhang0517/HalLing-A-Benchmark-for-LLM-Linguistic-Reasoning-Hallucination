# HalLing Analysis Scripts

This directory contains scripts for analyzing HalLing benchmark results.

## Setup

```bash
pip install -r requirements.txt
```

## Scripts

### `analyze_results.py`

Main analysis script that:
- Calculates overall accuracy for each model
- Breaks down performance by linguistic phenomenon
- Compares MCQ vs OQ performance
- Generates comparison charts
- Exports results to JSON

**Usage:**
```bash
python scripts/analyze_results.py
```

**Output:**
- Console summary of all models
- `analysis_results.json` - Detailed results
- `accuracy_comparison.png` - Bar chart (if matplotlib available)

## Adding Custom Analysis

Create new scripts following this pattern:

```python
from scripts.analyze_results import load_excel_file, DATA_DIR
import pandas as pd

# Load specific file
df = load_excel_file(DATA_DIR / "results" / "llama" / "Llama_MCQ_Ambiguity(done).xlsx")

# Your analysis here
```
