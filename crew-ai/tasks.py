from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writter
from datetime import datetime
import os


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = os.path.join("crew-ai", "tasks", f"blog_post_{timestamp}.txt")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

## Research Task
research_task = Task(
    description = (
        "Identify the video {topic}. "
        "Get detailed information about the video content from the YT channel"
    ),
    expected_output = "A comprahensive 3 paragraphs long report based on the {topic} video content from the YT channel",
    tools = [yt_tool],
    agent = blog_researcher
)

## Writing Task
writting_task = Task(
    description = (
        "Narrate the blog content about the video {topic}. "
        "Get detailed information about the video content from the YT channel"
    ),
    expected_output = "A comprahensive 3 paragraphs long blog post based on the {topic} video content from the YT channel",
    tools = [yt_tool],
    agent = blog_writter,
    async_execution = False,
    output_file = output_path
)