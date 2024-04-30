# Welcome to the Basic Crew AI Example
Thsi example demonstrates how to use CrewAI to build one agent and one task. This is to help those who have 0 cdoing experience to try and make the transition to some of the basics around setting up your virtual env, using git etc and running a very basic CrewAI example. I will say that until a GUI is released, you will need to be comfortable with the command line and have some basic understadning of Python. I suggest that you have a look at Python tutorials on YouTube or other platforms to get a basic understanding of Python.

# Prerequisites
    Install Python 3.10 or later. You can download Python from the official website: https://www.python.org/downloads/
    Install Git. You can install via:
        Linux: apt-get install git
        Windows: https://git-scm.com/download/win
        Mac: brew install git
    Install a code editor. You can use any code editor of your choice. Some popular code editors are:
        Visual Studio Code: https://code.visualstudio.com/
        Sublime Text: https://www.sublimetext.com/
        PyCharm: https://www.jetbrains.com/pycharm/
    Install Ollama 
        Download the latest version of Ollama from the official website: https://www.ollama.com/
    Start Ollama
        click the new Ollama icon on your desktop to start the application or the Ollama icon in your applications folder.
    Pull the LLM model the LLM model using the CLI
        ollama pull mistral:7b-instruct-q4_0
       
# Setup environment with virtualenv
Using the terminal, navigate to the directory where you want to create the project. Then, run the following command to create a new project:
```bash
python3 -m venv basic_crewai
```
# Next, activate the virtual environment by running the following command:
```bash
source basic_crewai/bin/activate
```
# Clone the CrewAI Basic Example repository into the project directory
```bash
cd basic_crewai
git clone https://github.com/theCyberTech/crewai_basic_example.git
```
# Install the required dependencies
```bash
cd  crewai_basic_example
pip install -r requirements.txt
```
# Update the main.py file with your topic
```python
### result = crew.kickoff(inputs={'topic': '70s and 80s Australan rock bands'})
```
# Run the agent
```bash
python main.py
```

