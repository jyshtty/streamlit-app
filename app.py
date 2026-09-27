import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="🚀",
    layout="wide"
)

# Title and description
st.title("🚀 Simple Streamlit Demo Application")
st.markdown("Welcome! This demo showcases various Streamlit features.")

# Sidebar
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Your Name", "Guest")
st.sidebar.write(f"Hello, {user_name}! 👋")

# Create tabs
tab1, tab2, tab3 = st.tabs(["📊 Data Visualization", "🎮 Interactive Widgets", "📝 Text & Media"])

# Tab 1: Data Visualization
with tab1:
    st.header("Data Visualization")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Line Chart")
        # Generate sample data
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        st.line_chart(chart_data)

    with col2:
        st.subheader("Area Chart")
        area_data = pd.DataFrame(
            np.random.randn(20, 3).cumsum(axis=0),
            columns=['Series 1', 'Series 2', 'Series 3']
        )
        st.area_chart(area_data)

    # Data table
    st.subheader("Sample Data Table")
    df = pd.DataFrame({
        'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
        'Sales': [150, 230, 180, 290],
        'Revenue': [15000, 23000, 18000, 29000],
        'Region': ['North', 'South', 'East', 'West']
    })
    st.dataframe(df, use_container_width=True)

# Tab 2: Interactive Widgets
with tab2:
    st.header("Interactive Widgets")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Controls")

        # Slider
        age = st.slider("Select your age", 0, 100, 25)
        st.write(f"You selected: {age} years")

        # Select box
        option = st.selectbox(
            "Choose your favorite color",
            ["Red", "Green", "Blue", "Yellow", "Purple"]
        )
        st.write(f"Your favorite color: {option}")

        # Checkbox
        if st.checkbox("Show additional info"):
            st.info("This is additional information that was hidden!")

    with col2:
        st.subheader("More Controls")

        # Radio buttons
        choice = st.radio(
            "Select a programming language",
            ["Python", "JavaScript", "Java", "C++"]
        )
        st.write(f"You chose: {choice}")

        # Multi-select
        options = st.multiselect(
            "Select your hobbies",
            ["Reading", "Sports", "Music", "Travel", "Gaming", "Cooking"],
            default=["Reading"]
        )
        st.write(f"Your hobbies: {', '.join(options)}")

        # Date input
        date = st.date_input("Select a date", datetime.now())
        st.write(f"Selected date: {date}")

# Tab 3: Text & Media
with tab3:
    st.header("Text & Media Examples")

    # Different text styles
    st.subheader("Text Formatting")
    st.markdown("**Bold text** and *italic text*")
    st.code("print('Hello, Streamlit!')", language="python")

    # Info boxes
    col1, col2 = st.columns(2)
    with col1:
        st.success("This is a success message!")
        st.info("This is an info message!")
    with col2:
        st.warning("This is a warning message!")
        st.error("This is an error message!")

    # Metrics
    st.subheader("Metrics Display")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "25°C", "+2°C")
    col2.metric("Revenue", "$12,345", "+8%")
    col3.metric("Users", "1,234", "-5")

# Footer
st.divider()
st.markdown("---")
st.caption(f"Demo app built with Streamlit | Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
