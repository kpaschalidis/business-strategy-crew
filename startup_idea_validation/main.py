#!/usr/bin/env python
import asyncio
import sys
import warnings


from startup_idea_validation.crew import StartupIdeaValidation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


async def run_async():
    """
    Run the crew asynchronously.
    """
    inputs = {
        "idea_name": "MealGenie",
        "idea_description": "AI-powered meal planning app that creates personalized meal plans based on dietary preferences, budget, and local grocery store availability",
        "target_market": "Busy professionals and families who want healthy, convenient meal planning",
    }

    try:
        await StartupIdeaValidation().crew().kickoff_async(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def run():
    """
    Synchronous wrapper for running the crew (used by script entry points).
    """
    asyncio.run(run_async())


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "idea_name": "MealGenie",
        "idea_description": "AI-powered meal planning app that creates personalized meal plans based on dietary preferences, budget, and local grocery store availability",
        "target_market": "Busy professionals and families who want healthy, convenient meal planning",
    }
    try:
        StartupIdeaValidation().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        StartupIdeaValidation().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "idea_name": "MealGenie",
        "idea_description": "AI-powered meal planning app that creates personalized meal plans based on dietary preferences, budget, and local grocery store availability",
        "target_market": "Busy professionals and families who want healthy, convenient meal planning",
    }

    try:
        StartupIdeaValidation().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    asyncio.run(run_async())
