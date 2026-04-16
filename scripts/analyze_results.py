#!/usr/bin/env python3
"""
HalLing Benchmark Analysis Script
Analyzes model performance across linguistic phenomena
"""

import pandas as pd
import json
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

# Configuration
DATA_DIR = Path(__file__).parent.parent / "data"
RESULTS_DIR = DATA_DIR / "results"
BENCHMARK_DIR = DATA_DIR / "benchmark-test"

def load_excel_file(filepath):
    """Load an Excel file and return a DataFrame"""
    try:
        df = pd.read_excel(filepath)
        return df
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def analyze_model_results(model_name, model_dir):
    """Analyze all results for a specific model"""
    results = {
        'model': model_name,
        'total_questions': 0,
        'correct_answers': 0,
        'accuracy': 0.0,
        'by_phenomenon': {},
        'by_question_type': {'MCQ': {'total': 0, 'correct': 0}, 'OQ': {'total': 0, 'correct': 0}}
    }
    
    if not model_dir.exists():
        return results
    
    for file in model_dir.glob("*.xlsx"):
        df = load_excel_file(file)
        if df is None or df.empty:
            continue
        
        # Extract phenomenon and question type from filename
        filename = file.stem.lower()
        
        # Determine question type
        q_type = 'MCQ' if 'mcq' in filename else 'OQ' if 'oq' in filename else 'Unknown'
        
        # Determine phenomenon
        phenomenon = 'Unknown'
        if 'ambiguity' in filename:
            phenomenon = 'Ambiguity'
        elif 'ana' in filename:
            phenomenon = 'Anaphora'
        elif 'ce' in filename or 'center' in filename:
            phenomenon = 'Center Embedding'
        elif 'gp' in filename or 'garden' in filename:
            phenomenon = 'Garden Path'
        elif 'fol' in filename or 'quantifier' in filename:
            phenomenon = 'Quantifier'
        
        # Count results
        total = len(df)
        
        # Try to find correctness column
        correct_col = None
        for col in df.columns:
            if col.lower() in ['correct', 'is_correct', 'accuracy', 'result']:
                correct_col = col
                break
        
        if correct_col:
            correct = df[correct_col].sum() if df[correct_col].dtype in ['int64', 'float64', 'bool'] else 0
        else:
            correct = 0
        
        # Update results
        results['total_questions'] += total
        results['correct_answers'] += correct
        
        if q_type in results['by_question_type']:
            results['by_question_type'][q_type]['total'] += total
            results['by_question_type'][q_type]['correct'] += correct
        
        if phenomenon not in results['by_phenomenon']:
            results['by_phenomenon'][phenomenon] = {'total': 0, 'correct': 0}
        results['by_phenomenon'][phenomenon]['total'] += total
        results['by_phenomenon'][phenomenon]['correct'] += correct
    
    # Calculate overall accuracy
    if results['total_questions'] > 0:
        results['accuracy'] = results['correct_answers'] / results['total_questions']
    
    # Calculate per-phenomenon accuracy
    for pheno in results['by_phenomenon']:
        pheno_data = results['by_phenomenon'][pheno]
        if pheno_data['total'] > 0:
            pheno_data['accuracy'] = pheno_data['correct'] / pheno_data['total']
    
    # Calculate per-question-type accuracy
    for q_type in results['by_question_type']:
        qt_data = results['by_question_type'][q_type]
        if qt_data['total'] > 0:
            qt_data['accuracy'] = qt_data['correct'] / qt_data['total']
    
    return results

def compare_models():
    """Compare all models and generate summary"""
    models = ['llama', 'mistral', 'qwen', 'glm4']
    all_results = {}
    
    print("=" * 60)
    print("HalLing Benchmark - Model Performance Analysis")
    print("=" * 60)
    
    for model in models:
        model_dir = RESULTS_DIR / model
        if model_dir.exists() and any(model_dir.iterdir()):
            results = analyze_model_results(model, model_dir)
            all_results[model] = results
            
            print(f"\n📊 {model.upper()}")
            print(f"   Total Questions: {results['total_questions']}")
            print(f"   Correct Answers: {results['correct_answers']}")
            print(f"   Overall Accuracy: {results['accuracy']:.2%}")
            
            print(f"\n   By Question Type:")
            for q_type, data in results['by_question_type'].items():
                if data['total'] > 0:
                    print(f"      {q_type}: {data['accuracy']:.2%} ({data['correct']}/{data['total']})")
            
            print(f"\n   By Phenomenon:")
            for pheno, data in results['by_phenomenon'].items():
                if data['total'] > 0:
                    print(f"      {pheno}: {data.get('accuracy', 0):.2%} ({data['correct']}/{data['total']})")
    
    # Save results to JSON
    output_file = Path(__file__).parent.parent / "analysis_results.json"
    with open(output_file, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\n💾 Results saved to {output_file}")
    
    return all_results

def generate_visualizations(results):
    """Generate comparison charts"""
    if not results:
        return
    
    # Prepare data
    models = list(results.keys())
    accuracies = [results[m]['accuracy'] for m in models]
    
    # Overall accuracy comparison
    plt.figure(figsize=(10, 6))
    plt.bar(models, accuracies)
    plt.title('HalLing Benchmark - Overall Model Accuracy')
    plt.xlabel('Model')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)
    for i, v in enumerate(accuracies):
        plt.text(i, v + 0.02, f'{v:.2%}', ha='center')
    plt.tight_layout()
    plt.savefig(Path(__file__).parent.parent / 'accuracy_comparison.png')
    print("📈 Chart saved: accuracy_comparison.png")

if __name__ == "__main__":
    results = compare_models()
    
    # Try to generate visualizations if matplotlib is available
    try:
        generate_visualizations(results)
    except Exception as e:
        print(f"\n⚠️  Could not generate visualizations: {e}")
        print("   Install matplotlib: pip install matplotlib")
