import os

from crewai import Crew,LLM

from tasks.analyse_task import get_stock_analysis
from tasks.trade_task import trade_decision
from agents.analyst_agent import analyst_agent
from agents.trader_agent import trader_agent

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key = os.getenv("GROQ_API_KEY"),
    temperature=0.0
)


stock_crew = Crew(
    agents=[analyst_agent, trader_agent],
    tasks=[get_stock_analysis, trade_decision],
    llm=llm,
    verbose=True
)
