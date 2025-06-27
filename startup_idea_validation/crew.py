from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool,
)


@CrewBase
class StartupIdeaValidation:
    """StartupIdeaValidation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def startup_validation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["startup_validation_agent"],
            verbose=True,
            tools=[
                SerperDevTool(),
                WebsiteSearchTool(),
                ScrapeWebsiteTool(),
            ],
        )

    @task
    def validate_startup_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config["validate_startup_idea_task"],
            output_file="reports/startup_idea_validation.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StartupIdeaValidation crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
