# 🎓 Personalised Learning Agent

An AI-powered, multi-agent system that builds a personalised programming
learning path for students instead of the generic, one-size-fits-all
roadmaps most learning platforms offer.

## 💡 Why this exists

Most learning resources are built for an average learner, not a specific
one. They don't know what you already know, how you prefer to learn, or
where you tend to get stuck.

This project grew out of a personal version of that problem, repeatedly
starting and abandoning learning tracks (Python, JavaScript, Java/DSA) at
the first genuinely confusing concept, simply because nothing around me
adjusted to what I actually needed at that moment.

This system tries to fix that: understand the learner first, then build
a roadmap and find resources around *them* and follow up over time,
instead of handing over a static list of links.

## ⚙️ How it works

One orchestrator agent coordinates four specialised sub-agents, delegating
based on where the conversation currently is:
```mermaid
flowchart TD
    U[User] --> O[Orchestrator Agent]

    O --> P[Profile Agent]
    O --> R[Roadmap Agent]
    O --> RA[Resource Agent]
    O --> PR[Progress Agent]

    RA --> S[Search Agent (Tool)]
```
### 🔹 Profile Agent
- Collects information about the learner
- Understands:
  - Career goals
  - Known programming languages
  - Experience level
  - Preferred learning style (hands-on, videos, docs, etc.)
- Uses natural conversation instead of fixed forms
- Infers details like experience level where possible, rather than asking everything directly

---

### 🔹 Roadmap Agent
- Creates a personalized, prerequisite-ordered learning roadmap
- Adapts recommendations based on:
  - Student goals
  - Experience level
  - Existing programming knowledge
- Skips topics the student has already mastered

---

### 🔹 Resource Agent
- Recommends real, current learning resources for every roadmap topic
- Uses a dedicated search agent (live web search) to find results, rather than relying on hardcoded links
- Weighs resource types based on the student's preferred learning mode
- Supports:
  - Documentation
  - YouTube tutorials
  - Interactive coding platforms
  - Practice websites

---

### 🔹 Progress Agent
- Tracks completed topics
- Suggests the next topic to move to
- Revisits weak concepts the student struggled with
- Monitors learning progress
- Helps maintain consistency throughout the learning journey

## 📁 Project Structure

```
study-paranoia/
├── learning_agent/
│   ├── agent.py              # Root orchestrator agent
│   ├── requirements.txt
│   └── .env.example
└── sub_agents/
    ├── profile_agent.py
    ├── roadmap_agent.py
    ├── resource_agent.py
    ├── search_agent.py       # Search tool used by resource_agent
    └── progress_agent.py
```

## 🛠️ Tech stack

- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Pydantic
- Google Search grounding

## 🚀 Setup

```bash
git clone https://github.com/AnushkaKundu-12/study-paranoia.git
cd study-paranoia
pip install -r requirements.txt
cp .env.example .env
```
Add your Gemini API key to `.env`:
GOOGLE_API_KEY=your_api_key_here
Then run:
```bash
adk web
```

## 📌 Current Status

🚧 Under Development
The project is actively being built, with new features and improvements added incrementally.

## 🔭 Roadmap

- Persistent memory across sessions
- GitHub profile analysis for real skill inference
- AI-generated quizzes
- Adaptive roadmap updates
- Learning analytics dashboard

## 👩‍💻 Author

**Anushka Kundu** 
<br>
 B.Tech CSE, KIIT University