import os
import streamlit as st
from pydantic import ValidationError

from scripts import (
    safe_load_json,
    validate_compiler_response,
    normalize_verdict,
)

st.set_page_config(page_title="Identity Compiler", layout="wide")

st.title("Identity Compiler")
st.caption("Not education. Proof-of-work enforcement. Evidence-gated readiness.")

# Sidebar controls
st.sidebar.header("Run Mode")
mode = st.sidebar.radio(
    "Choose how to drive the demo",
    options=["Paste JSON from AI Studio (recommended)", "Call Gemini API (requires key)"],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.subheader("Hard Rules (demo-visible)")
st.sidebar.write("• No courses, no certifications, no study plans")
st.sidebar.write("• Only: Produce, Publish, Demonstrate, Evaluate")
st.sidebar.write("• Gate: refuses premature applying")

# Intake (Screen 1)
st.markdown("## 1) Intake")
with st.form("intake_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    with col1:
        current_role = st.text_input("Current role", value="SAP S/4HANA Solution Architect (MM, P2P, IS-Retail)")
        years = st.text_input("Years of experience", value="15+")
        geography = st.selectbox("Geography", ["UK", "EU", "India", "US"], index=0)
    with col2:
        target_role = st.text_input("Target role", value="SAP AI Architect (enterprise)")
        time_budget = st.selectbox("Time budget per week (fixed for this hackathon)", ["6 hours/week"], index=0)
        evidence_links = st.text_area(
            "Existing public evidence (links)",
            value="https://github.com/avikjudemo/sap-sentinel\nhttps://github.com/avikjudemo",
            height=90,
        )

    preference = st.selectbox("Preference", ["strongest_long_term", "balanced", "fastest_employable"], index=0)
    compile_clicked = st.form_submit_button("Compile Identity")

st.markdown("---")

# Get compiler output JSON
compiler_json_text = None
if mode == "Paste JSON from AI Studio (recommended)":
    st.markdown("## Provide Gemini Output (JSON)")
    st.info(
        "Run the prompt in AI Studio, copy the JSON output, and paste it here. "
        "This avoids billing/API risk and is ideal for hackathon demos."
    )
    compiler_json_text = st.text_area("Paste JSON here", height=240)
else:
    st.markdown("## Call Gemini API (requires key + billing)")
    st.warning(
        "Only use this if you have an API key configured. For hackathons, pasting JSON is safer."
    )
    api_key = st.text_input("GEMINI_API_KEY", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    st.caption("If you want: set GEMINI_API_KEY as an environment variable and restart Streamlit.")
    # Keeping API call out of this first pass to avoid toolchain surprises during demo.
    st.error("API call mode not enabled in this template. Use paste-JSON mode for demo reliability.")

# Parse + render
if compiler_json_text and compile_clicked:
    try:
        raw = safe_load_json(compiler_json_text)
        resp = validate_compiler_response(raw)
        outputs = resp.outputs

        # Normalize verdict for display
        gate = outputs.readiness_gate
        gate.verdict = normalize_verdict(gate.verdict)

        # Screen 2: Identity Delta
        st.markdown("## 2) Compute Identity Delta")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Market expects")
            for x in outputs.identity_delta.market_expectations:
                st.write(f"- {x}")
        with c2:
            st.subheader("You currently signal")
            for x in outputs.identity_delta.current_signals:
                st.write(f"- {x}")

        st.subheader("Top 3 non-obvious gaps (blocking credibility)")
        for i, g in enumerate(outputs.identity_delta.top_3_non_obvious_gaps, start=1):
            st.write(f"{i}. {g}")

        st.markdown("---")

        # Screen 3: Questline
        st.markdown("## 3) Proof-of-Work Questline (24 weeks)")
        st.caption("Only Week 1–2 expanded in demo. Rest stays collapsed.")
        for w in outputs.questline_24w:
            title = f"Week {w.week}: {w.mission}"
            if w.week in (1, 2):
                with st.expander(title, expanded=True):
                    st.write(f"**Mission:** {w.mission}")
                    st.write(f"**Deliverable:** {w.deliverable}")
                    st.write(f"**Evidence:** {w.evidence}")
                    st.write(f"**Timebox:** {w.timebox_hours} hours")
            else:
                with st.expander(title, expanded=False):
                    st.write(f"**Deliverable:** {w.deliverable}")
                    st.write(f"**Evidence:** {w.evidence}")
                    st.write(f"**Timebox:** {w.timebox_hours} hours")

        st.markdown("---")

        # Screen 4: Portfolio + Gate
        st.markdown("## 4) Signal Portfolio + Readiness Gate")
        left, right = st.columns([2, 1])

        with left:
            st.subheader("High-signal artifacts")
            for a in outputs.signal_portfolio.high_signal_artifacts:
                st.markdown(f"### {a.name}")
                st.write(f"**Why it counts:** {a.why_it_counts}")
                st.write("**Acceptance criteria:**")
                for ac in a.acceptance_criteria:
                    st.write(f"- {ac}")
                st.write(f"**Evidence link:** {a.link_placeholder}")
                st.markdown("---")

        with right:
            st.subheader("Readiness Gate")
            st.metric("Signal Credibility Score", f"{gate.signal_credibility_score} / 100")
            if gate.verdict == "apply_now":
                st.success("VERDICT: APPLY NOW")
            else:
                st.error("VERDICT: DO NOT APPLY YET")

            st.write("**Reasons:**")
            for r in gate.reasons:
                st.write(f"- {r}")

            st.write("**Minimum to reach APPLY NOW:**")
            for m in gate.minimum_to_reach_70:
                st.write(f"- {m}")

        st.caption("Rule: artifacts without public evidence do not count. This is not an education tool.")
    except ValidationError as ve:
        st.error("JSON parsed, but schema validation failed. Your pasted output is missing required fields.")
        st.code(str(ve))
    except Exception as e:
        st.error("Failed to parse/validate JSON. Ensure you pasted valid JSON.")
        st.code(str(e))
else:
    st.markdown("### Demo tip")
    st.write(
        "To demo without API billing risk: run in AI Studio, copy JSON output, paste it above, then click **Compile Identity**."
    )