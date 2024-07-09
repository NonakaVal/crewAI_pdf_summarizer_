import yaml
import os
from crewai.agent import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool, TXTSearchTool, PDFSearchTool
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain_openai import ChatOpenAI


def select_pdf():
    pdf_folder = 'documents/'  # Assuming PDFs are stored in 'pdfs/' folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado na pasta 'pdfs/'. Verifique o caminho e tente novamente.")
        return None
    
    print("PDFs disponíveis:")
    for i, pdf_file in enumerate(pdf_files, start=1):
        print(f"{i}. {pdf_file}")
    
    while True:
        try:
            choice = int(input(f"Digite o número do PDF que deseja usar (1-{len(pdf_files)}): "))
            if 1 <= choice <= len(pdf_files):
                selected_pdf = pdf_files[choice - 1]
                return os.path.join(pdf_folder, selected_pdf)
            else:
                print("Por favor, digite um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


def create_agents(agents_file):
    llm = ChatOpenAI(model='gpt-3.5-turbo')
    
    selected_pdf_path = select_pdf()  # Dynamically select PDF
    if not selected_pdf_path:
        return None  # Handle case where no PDF is selected or found
    
    PDFTool = PDFSearchTool(pdf=selected_pdf_path)

    with open(agents_file, 'r') as f:
        agents_data = yaml.safe_load(f)

    analysis_specialist = Agent(
        role=agents_data['senior_text_analysis_specialist']['role'],
        goal=agents_data['senior_text_analysis_specialist']['goal'],
        backstory=agents_data['senior_text_analysis_specialist']['backstory'],
        tools=[PDFTool, SerperDevTool(), WebsiteSearchTool()],
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

    structure_specialist = Agent(
        role=agents_data['senior_planning_structure_specialist']['role'],
        goal=agents_data['senior_planning_structure_specialist']['goal'],
        backstory=agents_data['senior_planning_structure_specialist']['backstory'],
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm=llm,
        verbose=True
    )

    research_specialist = Agent(
        role=agents_data['senior_source_reference_research_specialist']['role'],
        goal=agents_data['senior_source_reference_research_specialist']['goal'],
        backstory=agents_data['senior_source_reference_research_specialist']['backstory'],
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm=llm,
        verbose=True,
        allow_delegation=True
    )

    article_writer = Agent(
        role=agents_data['senior_article_writer']['role'],
        goal=agents_data['senior_article_writer']['goal'],
        backstory=agents_data['senior_article_writer']['backstory'],
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    return analysis_specialist, structure_specialist, research_specialist, article_writer




