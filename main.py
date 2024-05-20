'''
Name
    main.py

Author
    Written by Rip&Tear - CrewAI Discord Moderator .riptear
    
Date Sat 13th Apr 2024
    
Description
    This is a basic example of how to use the CrewAI library to create a simple research task. 
    The task is to research the topic of "70s and 80s British rock bands" and provide 5 paragraphs of information on the topic. 
    The task is assigned to a single agent (Researcher) who will use the ChatOllama model to generate the information. 
    The result of the task is written to a file called "research_result.txt".

Usage
    python main.py
    
Output
    The output of the task is written to a file called "research_result.txt".'''

# Import required libraries - make sure the crewai and langchain_community packages are installed via pip
import os
from crewai import Agent, Crew, Process, TAsk

os.environ['OPENAI_API_BASE']='http://localhost:11434/v1'
os.environ['OPENAI_API_KEY']='sk-111111111111111111111111111111111111111111111111'
os.environ['OPENAI_MODEL_NAME']='mistral:7b-instruct-q4_0'

# Create a function to log to a file with the date as the filename - this will be used as a callback function for the agent. this could be as complex as you like
def write_result_to_file(result):
    filename = 'raw_output.log'
    with open(filename, 'a') as file:
        file.write(str(result))

# Create the agent
researcher = Agent(
    role='Researcher', # Think of this as the job title
    goal='Research the topic', # This is the goal that the agent is trying to achieve
    backstory='As an expert in the field of {topic}, you will research the topic and provide the necessary information', # This is the backstory of the agent, this helps the agent to understand the context of the task
    max_iter=3, # This is the maximum number of iterations that the agent will use to generate the output
    max_rpm=100, # This is the maximum number of requests per minute that the agent can make to the language model
    verbose=True, # This is a flag that determines if the agent will print more output to the console 
    step_callback=write_result_to_file, # This is a callback function that will be called after each iteration of the agent
    Allow_Delegation=False, # This is a flag that determines if the agent can delegate the task to another agent. As we are only using one agent, we set this to False
)  

# Create the task
research_task = Task(
    description='Research the topic', # This is a description of the task
    agent=researcher, # This is the agent that will be assigned the task
    expected_output='5 paragpahs of information on the topic', # This is the expected output of the taskafter its completion
    verbose=True, # This is a flag that determines if the task will print more output to the console
    output_file='research_result.txt' # This is the file where the output of the task will be written to, in this case, it is "research_result.txt"
)           

# Create the crew  
crew = Crew(
  agents=[researcher], # This is a list of agents that will be part of the crew
  tasks=[research_task], # This is a list of tasks that the crew will be assigned
  process=Process.sequential, # This is the process that the crew will use to complete the tasks, in this case, we are using a sequential process
  verbose=True, # This is a flag that determines if the crew will print more output to the console
  memory=False, # This is a flag that determines if the crew will use memory to store information about the tasks in a vector database
  cache=False, # This is a flag that determines if the crew will use a cache. A cache is not needed in this example, so we set this to False
  max_rpm=100, # This is the maximum number of requests per minute that the crew can make to the language model 
)

# Starting start the crew
result = crew.kickoff(inputs={'topic': '70s, 80s and 90s Australian rock bands'}) # Change the topic to whatever you want to research
print(result)
