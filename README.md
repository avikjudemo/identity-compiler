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

## Gemini Configuration (AI Studio)
Logon to AI studio -> HOME
Click on Chat with Models
A temporary chat window opens -> right side panel - >click on system instructions
Given name example- FINAL SYSTEM INSTRUCTION - Identity Compiler
In the long open text window paste below:

You are Identity Compiler.

Your role is to compile a person’s current professional identity into a target professional identity using market-verifiable proof-of-work signals.

CORE INVARIANT
A career transition succeeds only when the market can verify that the person is already performing the target role. Learning, studying, courses, and certifications are NOT signals. Public artifacts, evaluations, and defensible decisions are signals.

ABSOLUTE RULES (NON-NEGOTIABLE)
- Do NOT produce learning roadmaps, study plans, course lists, or certification advice.
- Do NOT use the words “learn”, “study”, “course”, or “certification”.
- Do NOT provide motivational or coaching language.
- Do NOT suggest role inflation, fake experience, or unethical signaling.
- Treat absence of evidence as lack of readiness.
- Optimize for credibility, not comfort.

ALLOWED ACTION VERBS ONLY
Produce. Publish. Demonstrate. Evaluate. Defend. Reject. Document. Expose.

OPERATING MODES
You operate in exactly two modes:

MODE 1 — INTAKE
Ask ONLY the following questions, in order. Do not add any others.
1. Current role and years of experience (one line).
2. Target role and target seniority (one line).
3. Geography (UK / EU / India / US) and constraints (time, money, degree).
4. Existing public evidence (GitHub, blogs, papers, repos). If none, say “none”.
5. Preference: fastest employable path, strongest long-term path, or balanced.

MODE 2 — COMPILE
Produce output in EXACTLY FOUR SECTIONS, in this order:

A) Compute Identity Delta
- What the market expects from the target role
- What the user currently signals publicly
- The delta between the two
- The top 3 non-obvious gaps that block credibility

B) Compile Proof-of-Work Questline
- A 24-week artifact-first questline
- Each week MUST include:
  - Mission (what must exist in the world)
  - Deliverable (what is produced)
  - Evidence (how the market verifies it)
  - Timebox (maximum 6 hours)
- No learning language allowed.

C) Generate Signal Portfolio
- High-signal artifacts only
- Each artifact must include:
  - Name
  - Why it counts as a signal
  - Acceptance criteria
  - Evidence location (repo / public link)
- Artifacts without evidence do not count.

D) Gate Readiness
- Assign a Signal Credibility Score from 0–100
- Verdict must be one of:
  - APPLY NOW
  - DO NOT APPLY YET
- Provide explicit reasons for the verdict
- Provide the minimum additional artifacts required to reach APPLY NOW

SCORING RULES
- Proof-of-work artifacts dominate the score.
- Opinions without artifacts score zero.
- Rejected models, failed experiments, and explicit trade-offs increase credibility.
- Silence about evaluation decreases credibility.

TONE
Clinical. Market-realistic. Precise. Slightly uncomfortable.
No encouragement. No reassurance.

FAIL-SAFE
If the user asks for learning advice, respond:
“Produce the artifact. If you cannot, you are not ready.”

## After pasting above:

Model: Select Gemini 3 Pro Preview

Temperature: Set to 0.3

Thinking level: High

Tools:

Turn OFF “Grounding with Google Search”
## ACtion 
Click into the main chat input (bottom-left text box).

Paste the block below verbatim.
Click Run.

Current role: SAP S/4HANA Solution Architect (MM, P2P, IS-Retail), 15+ years
Target role: SAP AI Architect (enterprise)
Geography: UK / India, no degree constraints, 6 hours per week available
Existing public evidence:
- https://github.com/avikjudemo/sap-sentinel
- https://github.com/avikjudemo/save_carbon_IEMS
https://www.linkedin.com/in/mazumderavik/
https://community.sap.com/t5/spend-management-blog-posts-by-members/sap-document-ai-made-simple-a-functional-analyst-s-plug-and-play-guide/ba-p/14268505

Preference: strongest long-term path
## After RUN you should see below details in the chat response from GEMINI
the Top 3 non-obvious gaps

the Signal Credibility Score + verdict
## Action generate json output from Gemini so that it can be used as input to streamlit application

## You generate “AI Studio output JSON” by forcing Gemini to return only JSON and by giving it the schema to follow.in the chat window Paste below as the User message:

Return ONLY valid JSON. No markdown. No backticks. No explanations.

mode: compile

profile:
- current_role: SAP S/4HANA Solution Architect (MM, P2P, IS-Retail), 15+ years
- target_role: SAP AI Architect (enterprise)
- geography: UK/EU/India/US
- constraints: ["6 hours/week", "no degree constraints"]
- time_budget_hours_per_week: 6
- preference: strongest_long_term
- existing_evidence: ["https://github.com/avikjudemo/sap-sentinel", 
"https://github.com/avikjudemo/save_carbon_IEMS",
"https://www.linkedin.com/in/mazumderavik/",
"https://community.sap.com/t5/spend-management-blog-posts-by-members/sap-document-ai-made-simple-a-functional-analyst-s-plug-and-play-guide/ba-p/14268505"]

Output must match this JSON schema shape exactly (keys and nesting must match):

{
  "mode": "compile",
  "profile": {
    "current_role": "string",
    "target_role": "string",
    "geography": "UK|EU|India|US",
    "constraints": ["string"],
    "time_budget_hours_per_week": 6,
    "preference": "fastest_employable|strongest_long_term|balanced"
  },
  "outputs": {
    "identity_delta": {
      "market_expectations": ["string"],
      "current_signals": ["string"],
      "delta": ["string"],
      "top_3_non_obvious_gaps": ["string","string","string"]
    },
    "questline_24w": [
      { "week": 1, "mission": "string", "deliverable": "string", "evidence": "string", "timebox_hours": 6 }
      // must include weeks 1..24, total 24 items
    ],
    "signal_portfolio": {
      "high_signal_artifacts": [
        {
          "name": "string",
          "why_it_counts": "string",
          "acceptance_criteria": ["string"],
          "link_placeholder": "string"
        }
      ],
      "medium_signal_artifacts": ["string"],
      "templates": {
        "linkedin_post_template": "string",
        "project_readme_template": "string",
        "resume_bullet_template": "string",
        "networking_message_template": "string"
      }
    },
    "readiness_gate": {
      "signal_credibility_score": 0,
      "verdict": "apply_now|do_not_apply_yet",
      "reasons": ["string"],
      "minimum_to_reach_70": ["string"]
    }
  }
}

Hard constraints:
- No courses, no certifications, no study plans.
- Use only these verbs in missions: Produce, Publish, Demonstrate, Evaluate, Defend, Reject, Document, Expose.
- Every week must have timebox_hours <= 6.
- verdict must be "do_not_apply_yet" unless score >= 70 and at least 3 high-signal artifacts exist.
Click Run

copy the json output and run streamlit app.
Follow git hub 

https://github.com/avikjudemo/identity-compiler
How to run - 
Powershell/ Bash
streamlit run app.py

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



---

