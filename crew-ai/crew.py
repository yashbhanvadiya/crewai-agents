from crewai import Crew, Process
from agents import blog_researcher, blog_writter
from tasks import research_task, writting_task


## Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents = [blog_researcher, blog_writter],
    tasks = [research_task, writting_task],
    process = Process.sequential,  ## Options: sequential task execution is defalt
    memory = True,
    verbose = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

## Start the task execution precess with the enhanced feedback
result = crew.kickoff(inputs={"topic": "Latest Trends in AI and Data Science"})
print(result)