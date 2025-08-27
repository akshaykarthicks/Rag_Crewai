#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from rag_crew.crew import RagCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    user_input = input("Enter the query you want to research: ")    
    inputs = {
        'topic': user_input,
        'current_year': str(datetime.now().year)
    }
    
    print(inputs)
    print("--------------------------------")
    result = RagCrew().crew().kickoff(inputs=inputs)
    print(result)
    print("--------------------------------")



