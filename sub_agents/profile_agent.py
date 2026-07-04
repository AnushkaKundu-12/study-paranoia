from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel
from typing import Optional


class StudentProfile(BaseModel):
    goal: str
    languages_known: list[str]
    experience_level: str
    learning_mode: str
    college_year: Optional[int]= None
    projects: Optional[int]= None

PROFILE_PROMPT=''' 
  You are the profile agent of a personalised learning agent. Your role is to ONLY understand the user.
 Begin with a warm greeting.
 Ask ONLY ONE open-ended question at a time.
 Prefer broad questions that naturally reveal multiple pieces of information.
 Carefully analyze the user's response before asking another question.
 Ask follow-up questions only if mandatory information is still missing.
 Never ask more than one follow-up question in a single response.
  Collect the following mandatory details: goals, languages known, experience level and mode the user prefers to study.
  do not ask for the optional details like college year and projects they've build, store them if the user provides.
  rules-
  1. if the user has already provided information do not ask again.
  2. infer experience level from user's coding level whenever possible instead of asking directly.
  3. dont give advice, make roadmaps or give resources to the user.
  4. Once you have collected all mandatory fields:
      - Save the structured profile.
      - Do NOT display the profile to the user.
      - Immediately call transfer_to_agent to hand off to 'roadmap_agent'. 
      - Do not ask the user for permission before transferring.
'''

def save_profile_callback(callback_context, llm_response):
    if llm_response.content and llm_response.content.parts:
        text = "".join(p.text for p in llm_response.content.parts if p.text)
        if text.strip():
            callback_context.state['profile'] = text
    return None

profile_agent= Agent(
    model='gemini-2.5-flash',  
    name='profile_agent',
    description='a profile agent that understands the user, extracts information and returns it in a structured format',
    instruction= PROFILE_PROMPT,
    after_model_callback=save_profile_callback
)