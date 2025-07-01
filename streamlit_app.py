import streamlit as st
import json

st.set_page_config(page_title="Soumik's Project Timeline", layout="wide")
st.title("💍 Project 0: The One to Rule Them All")
st.subheader("A Timeline of Projects That Shaped My AI + EdTech Journey")

# Load project data
with open("projects_data.json", "r") as f:
    projects = json.load(f)

for project in projects:
    with st.expander(f"{project['title']} ({project['period']})"):
        st.markdown(f"**Description:** {project['description']}")
        st.markdown(f"**Tech Stack:** {', '.join(project['tech_stack'])}")
        st.markdown(f"**Context:** {project['context']}")
        st.markdown(f"[🔗 View GitHub Repo]({project['github_link']})")

st.markdown("---")
st.markdown("_Made with ❤️ using Python + Streamlit_")
