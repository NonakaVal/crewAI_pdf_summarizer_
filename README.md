# PDF Analysis and Agent Creation Project


powered by [crewAI](https://crewai.com) project.

## Overview
This project is designed to facilitate the analysis of PDF documents using a team of specialized agents. The agents leverage various tools and an AI language model to perform tasks such as text analysis, planning, structure, source referencing, and article writing.

## Features
- Dynamic PDF selection from a specified folder.
- Creation of agents with specialized roles and goals.
- Integration of multiple tools, including PDF search, web search, and text analysis.
- Utilization of a GPT-3.5 language model for enhanced text processing and analysis.


## Project Structure
```
pdf_summarizer/
├── articles/
│   └── output.md
├── config/
│   └── agents.yaml
│   └── tasks.yaml 
├── documents/
│   └── your-pdfs.pdf
├── tools/
│   ├── browser_tools.py
│   ├── search_tools.py
│   └── ...
├── agents.py
├── main.py
├── tasks.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Setup and Usage

### Prerequisites
- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- An [OpenAI](https://platform.openai.com) API key
- A [Serper](https://serper.dev/) API key
- A [Browserless](https://www.browserless.io/) API key

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pdf_summarizer.git
    cd pdf_summarizer
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

3. Create a `.env` file in the root directory and add your API keys:
    ```env
    SERPER_API_KEY=your_serper_api_key
    OPENAI_API_KEY=your_openai_api_key
    BROWSERLESS_API_KEY=your_browserless_api_key
    ```
    

### Usage
1. Place your PDF files in the `documents/` folder.

2. Update the `agents.json` and `tasks.json` files in the `config/` folder to define your agents and tasks.

3. Run the main script:
    ```sh
    poetry run python main.py
    ```

4. The output will be saved in the `articles/`.

## CrewAI Support and Documentations 
For support, questions, or feedback regarding the SelfDevelopment Crew or crewAI:
- [documentation](https://docs.crewai.com)
- [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)


<a href="https://www.crewai.com/">
    <img src="https://i.imgur.com/0FllxzQ.png" alt="Image" width="15%" style="display: block; margin: 0 auto;">
</a>

