from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tavily_tool_demo.tools.tavily_search import TavilySearchTool

tavily_search = TavilySearchTool()


@CrewBase
class CrewaiTavilyToolDemoCrew:
    """CrewaiTavilyToolDemo crew"""

    @agent
    def assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["assistant"],
            tools=[tavily_search],
            verbose=True,
            llm="groq/llama3-8b-8192",
        )

    @task
    def assistant_task(self) -> Task:
        return Task(
            config=self.tasks_config["assistant_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiTavilyToolDemo crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
