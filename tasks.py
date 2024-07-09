import yaml
from crewai.task import Task

import os

def select_output_filename():
    while True:
        filename = input("Digite o nome do arquivo de saída (deve ser .md): ")
        if filename.endswith('.md'):
            return os.path.join('articles', filename)
        else:
            print("O nome do arquivo deve terminar com .md. Tente novamente.")

def create_tasks(tasks_file, analysis_specialist, structure_specialist, research_specialist, article_writer):
    with open(tasks_file, 'r') as f:
        tasks_data = yaml.safe_load(f)

    output_file_name = select_output_filename()  # Solicita o nome do arquivo de saída

    analyze = Task(
        description=tasks_data['analyze_text']['description'],
        expected_output=tasks_data['analyze_text']['expected_output'],
        agent=analysis_specialist
    )

    review = Task(
        description=tasks_data['review_planning']['description'],
        expected_output=tasks_data['review_planning']['expected_output'],
        agent=structure_specialist,
        context=[analyze]
    )

    reference_research = Task(
        description=tasks_data['research_sources_references']['description'],
        expected_output=tasks_data['research_sources_references']['expected_output'],
        agent=research_specialist,
        context=[review, analyze]
    )

    write_post = Task(
        description=tasks_data['write_complete_article']['description'],
        expected_output=tasks_data['write_complete_article']['expected_output'],
        agent=article_writer,
        context=[review, analyze, reference_research],
        output_file=output_file_name
    )

    return analyze, review, reference_research, write_post
