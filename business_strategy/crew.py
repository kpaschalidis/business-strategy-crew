from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool,
    FileReadTool,
    FileWriterTool,
)


@CrewBase
class BusinessStrategy:
    """BusinessStrategy crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def market_intelligence_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["market_intelligence_agent"],
            verbose=True,
            tools=[
                SerperDevTool(),
                WebsiteSearchTool(),
                ScrapeWebsiteTool(),
            ],
        )

    @agent
    def business_strategy_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["business_strategy_agent"],
            verbose=True,
            tools=[
                SerperDevTool(),
                WebsiteSearchTool(),
                ScrapeWebsiteTool(),
            ],
        )

    @agent
    def financial_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_analysis_agent"],
            verbose=True,
            tools=[
                SerperDevTool(),
                WebsiteSearchTool(),
                ScrapeWebsiteTool(),
            ],
        )

    @agent
    def synthesis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["synthesis_agent"],
            verbose=True,
            tools=[FileReadTool(), FileWriterTool()],
        )

    @task
    def analyze_competitors_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_competitors_task"],
            output_file="reports/competitors_analysis.md",
        )

    @task
    def develop_business_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["develop_business_strategy_task"],
            output_file="reports/business_strategy.md",
            context=[
                self.tasks_config["analyze_competitors_task"],
            ],
        )

    @task
    def analyze_business_financials_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_business_financials_task"],
            output_file="reports/business_financials.md",
            context=[
                self.tasks_config["analyze_competitors_task"],
                self.tasks_config["develop_business_strategy_task"],
            ],
        )

    @task
    def synthesis_task(self) -> Task:
        return Task(
            config=self.tasks_config["synthesis_task"],
            output_file="reports/executive_summary.md",
            context=[
                self.tasks_config["analyze_competitors_task"],
                self.tasks_config["develop_business_strategy_task"],
                self.tasks_config["analyze_business_financials_task"],
            ],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BusinessStrategy crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
