import streamlit as st

# Ensure results exist
if "results" not in st.session_state or not st.session_state["results"]:
    st.error("No results found. Please go back and submit a new comparison.")
    if st.button("Back to Home"):
        st.switch_page("app.py")
    st.stop()

st.title("📊 Results & Analysis")
results = st.session_state["results"]

# Display results
st.success("Analysis done")

st.write(results['education']['suggestion'])

st.header("🛠 Skills Analysis")
st.write("✅ Matched Skills:", ", ".join(results["skills"]["analysis"]["matched_skills"]))
st.write("❌ Missing Skills:", ", ".join(results["skills"]["analysis"]["missing_skills"]))
st.write(results['skills']['suggestion'])


st.header("📈 Experience")
st.write(results["experience"]["suggestion"])

st.header("📝 Responsibilities Match")
st.write("Similarity Score:", results["responsibilities"]["similarity_score"])
st.write(results["responsibilities"]["suggestion"])


# Option to go back and compare again
if st.button("🔄 Try Another Comparison"):
    st.session_state.phase = "input"
    st.session_state["results"] = None
    st.switch_page("app.py")
