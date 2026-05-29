from crewai import Agent, LLM
from tools import yt_tool
from dotenv import load_dotenv
import os
load_dotenv()

llm = LLM(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

## Create a senior blog content researcher
blog_researcher = Agent(
    role = "Blog Researcher from Youtube Videos",
    goal = "Get the relevent video content for the topic {topic} from YT channel",
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning, and Gen AI and providing suggestion."
    ),
    tools = [yt_tool],
    llm = llm,
    allow_delegation = True
)

## Create a senir blog writter agent with YT tool
blog_writter = Agent(
    role = "Blog Writter",
    goal = "Narrate compiling tech stories about the video {topic} from YT channel",
    verbose = True,
    memory = True,
    backstory = (
        "With a fair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools = [yt_tool],
    llm = llm,
    allow_delegation = False
)