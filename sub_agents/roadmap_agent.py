from google.adk.agents.llm_agent import Agent


ROADMAP_PROMPT='''
 You are the roadmap agent of a personalised learning agent.
 Your role is to create a roadmap from foundational topics to advanced topics based 
 on the output from profile agent: {profile}.
 RULES-
 1. the roadmap should contain- a. the topic name
                                b. one line description about the topic why it is important
                                c. estimated time required to complete the topic assumng consistent daily practice
                                d. prerequisites(if any)
 2. Do not ask questions or provide resources.
 3. Do not include anything that user already knows.
    - Do not ask the user any questions. 
 4. once you have generated a roadmap present it clearly. .
    - Do not ask for permission or confirmation.
 5. return to the root agent-learning_agent once your work is done.
 6. STRICT LIMIT: Generate a maximum of 5 topics total, regardless of how
   broad the student's goal is. Prioritize the most immediately relevant
   and foundational topics. Mention in your response that this is a
   starting roadmap and more topics can be added as the student progresses.
'''
def save_roadmap_callback(callback_context,llm_response):
    if llm_response.content and llm_response.content.parts:
        text= ''.join(part.text for part in llm_response.content.parts if part.text)
        if text.strip():
            callback_context.state['roadmap'] = text
    return None

roadmap_agent= Agent(
    name='roadmap_agent',
    model='gemini-2.5-flash',
    instruction=ROADMAP_PROMPT,
    description='Creates a structured roadmap based on the student profile.',
    after_model_callback= save_roadmap_callback
)