#!/usr/bin/env python
import sys
from crewai_tavily_tool_demo.crew import CrewaiTavilyToolDemoCrew
from dotenv import load_dotenv

load_dotenv()


def run():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        inputs = {
            "user_input": f"{user_input}",
        }

        response = CrewaiTavilyToolDemoCrew().crew().kickoff(inputs=inputs)

        print(f"Assistant: {response}")
