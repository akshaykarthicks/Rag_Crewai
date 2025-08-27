from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool
from pathlib import Path
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

# Get script directory and sample.pdf path
script_dir = Path(__file__).parent
pdf_path = str(script_dir / "sample.pdf")

# Initialize PDFSearchTool
pdf_search_tool = PDFSearchTool(
    pdf=pdf_path,
    config=dict(
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001"
            )
        )
    )
)

@CrewBase
class RagCrew():
    """Crew for PDF reading and summarization"""

    agents_config_path = script_dir / "config/agents.yaml"
    tasks_config_path = script_dir / "config/tasks.yaml"

    @agent
    def Pdf_reader(self) -> Agent:
        return Agent(
            config=self.agents_config["Pdf_reader"],
            verbose=True,
            tools=[pdf_search_tool]
        )

    @agent
    def Pdf_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["Pdf_summarizer"],
            verbose=True
        )

    @task
    def pdf_reader_task(self) -> Task:
        return Task(
            config=self.tasks_config["pdf_reader_task"],
        )

    @task
    def pdf_summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config["pdf_summarizer_task"],
            output_file="summary.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the RagCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
