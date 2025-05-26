from openai import OpenAI
import streamlit as st
import OS
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# client = OpenAI()
# openai.api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_meeting_insights(transcript, model = "gpt-3.5-turbo"):
    """
    Takes in a meeting transcript and returns structured meeting insights.
    
    Args:
        transcript (str): Raw meeting notes or transcript.
        model (str): OpenAI model to use ("gpt-3.5-turbo" or "gpt-4").
    
    Returns:
        dict: Dictionary with summary, action_items, themes, and sentiment.
    """
    
    prompt = f"""
You are SmartMinutes, an AI assistant that summarizes meeting transcripts.

Given a meeting transcript or raw notes, your task is to:
1. Provide a clear and concise summary.
2. Extract key action items as bullet points (include who is responsible if mentioned).
3. List main themes or topics discussed.
4. Assess the overall sentiment of the meeting as one of: Positive, Neutral, or Negative.

Please format your response like this:

**Summary:**
<Your summary here>

**Action Items:**
- <Action item 1>
- <Action item 2>

**Main Themes:**
- <Theme 1>
- <Theme 2>

**Overall Sentiment:** <Positive/Neutral/Negative>

Here is the transcript:
\"\"\"
{transcript}
\"\"\"
    """.strip()

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=400
        )

        # content = response['choices'][0]['message']['content']
        content = response.choices[0].message.content

        # Optional: simple parsing into sections
        output = {
            "summary": "",
            "action_items": [],
            "themes": [],
            "sentiment": ""
        }

        lines = content.splitlines()
        current_section = None

        for line in lines:
            line = line.strip()
            if line.startswith("**Summary:**"):
                current_section = "summary"
                output["summary"] = line.replace("**Summary:**", "").strip()
            elif line.startswith("**Action Items:**"):
                current_section = "action_items"
            elif line.startswith("**Main Themes:**"):
                current_section = "themes"
            elif line.startswith("**Overall Sentiment:**"):
                current_section = "sentiment"
                output["sentiment"] = line.replace("**Overall Sentiment:**", "").strip()
            elif current_section == "action_items" and line.startswith("- "):
                output["action_items"].append(line[2:].strip())
            elif current_section == "themes" and line.startswith("- "):
                output["themes"].append(line[2:].strip())
            elif current_section == "summary" and line:
                output["summary"] += " " + line

        return output

    except Exception as e:
        return {"error": str(e)}
    


