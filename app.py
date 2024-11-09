# app.py
import streamlit as st
from main import main
import importlib
from agents import industry_research_agent
importlib.reload(industry_research_agent)


st.title("AI Use Case Generator for Industries")
industry = st.text_input("Enter the industry (e.g., Retail)")

if st.button("Generate Use Cases"):
    st.write("Generating use cases, please wait...")
    main(industry)  # Call the main function with the industry argument
    st.write("Process completed. Check the outputs.")
