from dotenv import load_dotenv
import crewai.llms.cache as crew_cache
crew_cache.mark_cache_breakpoint = lambda msg: msg
from crew import stock_crew


load_dotenv()

def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print(result)


if __name__ == "__main__":
    # run("TESLA")
    run("Wipro")
