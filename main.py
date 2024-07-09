import os
from dotenv import load_dotenv
import yaml
from agents import create_agents
from tasks import create_tasks
from crewai import Crew
from crewai_tools import TXTSearchTool
from langchain_openai import ChatOpenAI
import openai

# Load environment variables from .env file
load_dotenv()

# Configure API keys
# serper_api_key = os.getenv('SERPER_API_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')
os.environ["BROWSERLESS_API_KEY"] = os.getenv('BROWSERLESS_API_KEY')

# Initialize language model
llm = ChatOpenAI(model='gpt-3.5-turbo')

# YAML files
agents_file = './config/agents.yaml'
tasks_file = './config/tasks.yaml'


# Create agents from YAML
analysis_specialist, structure_specialist, research_specialist, article_writer = create_agents(agents_file)

# Create tasks from YAML
analyze_text, review_planning, research_sources_references, write_complete_article = create_tasks(tasks_file, analysis_specialist, structure_specialist, research_specialist, article_writer)

# Assemble the crew
crew = Crew(
    agents=[analysis_specialist, structure_specialist, research_specialist, article_writer],
    tasks=[analyze_text, review_planning, research_sources_references, write_complete_article],
    verbose=2,
    manager_llm=llm
)

# Execute the tasks
crew.kickoff()
