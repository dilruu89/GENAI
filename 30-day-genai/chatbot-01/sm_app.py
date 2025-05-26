# Make sure to import and set your OpenAI key
import openai
import sm_action as smf
import streamlit as st
import os

st.write(
    "Has environment variables been set:",
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
)
openai.api_key = st.secrets["OPENAI_API_KEY"]

sample_transcript = """
Thanks everyone for joining. First off, John gave an update on the Q3 marketing campaign—it's 70% complete but running behind due to resource constraints. Lisa mentioned the design team is waiting on final copy before they can proceed.

Tom raised a concern about overlapping responsibilities with the sales team and suggested a joint sync next week. We agreed to have a draft timeline ready by Friday. Emily will follow up on the email comms plan and share it by Thursday.

Meeting ended with a quick look at next week's priorities, focusing on conversion tracking and onboarding improvements.
"""

# result = smf.get_meeting_insights(sample_transcript)
# print(result)


st.set_page_config(page_title="SmartMinutes", layout="centered")
st.title("🧠 SmartMinutes - Meeting Insights")

user_input = st.text_area("Paste your meeting transcript or notes here:")

if st.button("Analyze Meeting"):
    with st.spinner("Thinking..."):
        result = smf.get_meeting_insights(user_input)
        
        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("📋 Summary")
            st.write(result["summary"])

            st.subheader("✅ Action Items")
            for item in result["action_items"]:
                st.write(f"- {item}")

            st.subheader("📌 Themes")
            for theme in result["themes"]:
                st.write(f"- {theme}")

            st.subheader("😊 Overall Sentiment")
            st.write(result["sentiment"])
