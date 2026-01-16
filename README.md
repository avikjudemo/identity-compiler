# Identity Compiler

**Compile yourself into your next role.**

Identity Compiler is a Gemini-powered product that enforces career readiness using **proof-of-work**, not courses, certifications, or learning roadmaps.

Hiring markets do not hire effort.  
They hire **evidence**.

---

## Problem

Career transitions fail for a simple reason:

- People *learn privately*
- But apply publicly with profiles that still signal their old identity

Most career tools encourage learning and optimism, but they never answer the hard question:

> **Would the market actually believe I’m ready?**

---

## Solution

**Identity Compiler** removes learning advice entirely and replaces it with an evidence-first system that:

1. Infers what the market expects for a target role
2. Compares it against what the user currently signals publicly
3. Generates artifact-first proof-of-work missions
4. **Refuses to allow applications** until sufficient public evidence exists

The refusal is intentional.  
The gate *is* the product.

---

## How It Works

### Input
- Current role
- Target role
- Geography and constraints
- Existing public evidence (if any)

### Core Logic (Powered by Gemini)
Gemini is used to:
- Infer **market expectations** for a role and seniority
- Identify **non-obvious gaps** blocking credibility
- Compile **artifact-first missions** that emit real signals

### Output (Four Fixed Screens)

1. **Compute Identity Delta**  
   Market expectations vs current public signals

2. **Proof-of-Work Questline**  
   Weekly missions that produce public artifacts  
   *(No learning tasks, no courses)*

3. **Signal Portfolio**  
   High-signal artifacts with acceptance criteria

4. **Readiness Gate**  
   A credibility score and a hard verdict:
   - `APPLY NOW`
   - `DO NOT APPLY YET`

Artifacts without public evidence do not count.

---

## Demo Personas

### Persona 1 (Founder Use Case)
- **SAP S/4HANA Solution Architect → SAP AI Architect**
- Demonstrates enterprise-scale transition and architectural rigor
- The founder is the first user of the product

### Persona 2 (Generality Proof)
- **Junior Tester → Senior SDET**
- Demonstrates that the same compiler logic works across domains

Both personas use the same system with different outputs.

---

## Why Gemini Is Essential

The hardest part of career readiness is not generating tasks —  
it is **inferring what the market actually expects** for a given role.

That inference cannot be hardcoded.

Gemini enables:
- Market expectation inference
- Gap detection without resume parsing
- Artifact-first planning grounded in real-world signals

Remove Gemini, and the compiler collapses.

---

## Implementation

- **Google AI Studio**
  - Used to design and test the Identity Compiler system instruction
  - Gemini model configured with strict rules:
    - No learning advice
    - No courses or certifications
    - Evidence-only outputs

- **Python + Streamlit**
  - Lightweight consumer-grade UI
  - Renders the four screens clearly
  - Demo runs in deterministic mode by pasting Gemini-generated JSON

This avoids API and billing risk yet preserving full transparency.

---

