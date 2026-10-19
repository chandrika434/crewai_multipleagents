
import os
import streamlit as st
from dotenv import load_dotenv
import crewai.llms.cache as crew_cache
crew_cache.mark_cache_breakpoint = lambda msg: msg

from crew import stock_crew

load_dotenv()

st.set_page_config(
    page_title="CrewAI Stock Analysis",
    page_icon="📈",
    layout="wide",
)

st.title("📈 CrewAI Stock Analysis Agent")
st.write(
    "Analyze a stock using your existing CrewAI agents."
)

st.info(
    "Enter a stock symbol or company name, "
    "for example WIPRO, INFY, AAPL or Tesla."
)

with st.form("stock_form"):
    stock = st.text_input(
        "Stock symbol or company",
        placeholder="e.g. WIPRO",
    ).strip()

    submitted = st.form_submit_button(
        "Analyze Stock",
        type="primary",
    )

if submitted:
    if not stock:
        st.warning("Please enter a stock symbol or company name.")

    elif not os.getenv("GROQ_API_KEY"):
        st.error("GROQ_API_KEY is not configured.")

    else:
        with st.spinner(
            f"Analyzing {stock.upper()}... Please wait."
        ):
            try:
                result = stock_crew.kickoff(
                    inputs={"stock": stock.upper()}
                )

                st.success("Analysis completed!")
                st.subheader(f"Analysis: {stock.upper()}")
                st.markdown(str(result))

            except Exception as e:
                st.error("The stock analysis failed.")
                st.exception(e)

st.divider()
st.caption(
    "Powered by CrewAI and Groq. "
    "AI-generated analysis is not a guarantee of future stock prices."
)
