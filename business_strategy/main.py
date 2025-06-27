#!/usr/bin/env python
import asyncio
import sys
import warnings


from business_strategy.crew import BusinessStrategy

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


async def run_async():
    """
    Run the crew asynchronously.
    """
    inputs = {
        "company_name": "OpenAI",
        "company_description": "OpenAI is a research lab that focuses on building safe and useful AI.",
        "industry": "AI",
    }

    try:
        await BusinessStrategy().crew().kickoff_async(inputs=inputs)
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
        "company_name": "OpenAI",
        "company_description": "OpenAI is a research lab that focuses on building safe and useful AI.",
        "industry": "AI",
    }
    try:
        BusinessStrategy().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BusinessStrategy().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "company_name": "OpenAI",
        "company_description": "OpenAI is a research lab that focuses on building safe and useful AI.",
        "industry": "AI",
    }

    try:
        BusinessStrategy().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    asyncio.run(run_async())
