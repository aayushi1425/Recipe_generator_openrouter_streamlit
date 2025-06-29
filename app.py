import streamlit as st
from src.generator import generate_recipe

st.set_page_config(page_title="AI Recipe Generator", layout="centered")

st.title("🍳 AI Recipe Generator")
st.markdown("Powered by Gemini via OpenRouter")

ingredients_input = st.text_input("Enter ingredients (comma separated):")

if st.button("Generate Recipe"):
    if ingredients_input:
        ingredients = [i.strip() for i in ingredients_input.split(",")]
        with st.spinner("Generating recipe..."):
            recipe = generate_recipe(ingredients)
        st.markdown("### 🍽️ Here's your recipe:")
        st.text_area(label="Generated Recipe", value=recipe, height=300, label_visibility="collapsed")

    else:
        st.warning("Please enter some ingredients.")
