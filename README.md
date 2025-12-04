This repository contains HalLing, a benchmark designed to evaluate how language models handle linguistic-reasoning tasks that commonly trigger hallucinations.
The benchmark targets failure modes such as:

Misinterpreting syntactic structure

Incorrect inferencing under ambiguity

Fabricated paraphrases

Logical contradictions introduced during reasoning

The goal is to provide diagnostic test sets, evaluation scripts, and model comparison results to support reproducible research.

Benchmark Categories
A. Anaphora

Ambiguous pronominal reference

Reflexive pronouns (valid)

Ungrammatical reflexives

Tests:

Binding Theory (Principle A)

Clause locality

C-command

Agreement features

B. Syntactic Ambiguity

PP attachment

Centre-embedded relative clauses

Garden-path sentences

Tests:

Correct parse recovery

Maintaining multiple structural hypotheses

Role assignment (agent/theme)

C. Semantic Reasoning

First-order logic (FOL) representations

Quantifier scope

Logical entailment

Tests:

Mapping sentences to ∀ / ∃

Reading ambiguity from surface structure

Distinguishing truth-conditionally distinct forms

4. Tasks & Evaluation

HalLing contains two task formats:

1. Multiple-Choice Questions

Models must choose between:

Correct analyses

Plausible-but-wrong distractors

Illogical/hallucinated interpretations

Ambiguity-identification options

This isolates structural reasoning failures.

2. Open-Ended Questions

Models must:

Explain structure

Provide formal logic

Identify ambiguity

Assign thematic roles

Refuse with “I don’t know” when appropriate

Evaluation categories:

Correct / non-hallucination

False / hallucination

Conceding with reason

Conceding with falsehood

Open-ended evaluation follows a rubric grounded in syntactic and semantic theory.

Example Models Evaluated
Model	Hallucination Rate	Notes
GLM-4-9B-Chat	1.3%	Strong baseline
Mistral-7B-Instruct	9.5%	Fluent but inconsistent
Llama-2-13B-Chat	10.5%	Structural errors
Qwen2.5-0.5B	25.2%	High hallucination rate

License: MIT
