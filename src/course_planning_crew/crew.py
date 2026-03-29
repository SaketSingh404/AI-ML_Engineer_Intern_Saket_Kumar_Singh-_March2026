from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from course_planning_crew.tools.custom_tool import FAISSRetrievalTool

@CrewBase
class CollegePlanningCrew():
    """CollegePlanningCrew for Agentic RAG Assessment"""

    # Path to your YAML files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        # Initialize your custom tool with the path to your FAISS index [cite: 83]
        self.retrieval_tool = FAISSRetrievalTool(
            folder_path='vector_database'
        )

    @agent
    def intake_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['intake_agent'],
            verbose=True,
            allow_delegation=False # Keeps the agent focused on student profile normalization [cite: 91]
        )

    @agent
    def catalog_retriever_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['catalog_retriever_agent'],
            tools=[self.retrieval_tool], # Links Phase 2 tool to Phase 3 agents [cite: 79]
            verbose=True
        )

    @agent
    def planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planner_agent'],
            verbose=True
        )

    @agent
    def verifier_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['verifier_agent'],
            tools=[self.retrieval_tool], # Used to double-check claims against the knowledge base [cite: 93]
            verbose=True
        )

    @task
    def intake_task(self) -> Task:
        return Task(
            config=self.tasks_config['intake_task']
        )

    @task
    def retrieval_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieval_task'],
            context=[self.intake_task()] # Passes student info to the searcher [cite: 91]
        )

    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task'],
            context=[self.intake_task(), self.retrieval_task()] # Handles $A \rightarrow B \rightarrow C$ logic [cite: 21, 92]
        )

    @task
    def verification_task(self) -> Task:
        return Task(
            config=self.tasks_config['verification_task'],
            context=[self.retrieval_task(), self.planning_task()] # Final grounding check [cite: 16, 93]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CollegePlanning crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential, # Ensures agents work in the correct order [cite: 94]
            verbose=True
        )