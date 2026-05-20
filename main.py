import sys
from dotenv import load_dotenv
load_dotenv()

from src.crew import crew

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "the future of quantum computing"
    result = crew.kickoff(inputs={"topic": topic})
    print(result)
