import streamlit as st

# Sample recipe data (you can later replace with API or database)
recipes = [
    {
        "name": "Spaghetti Carbonara",
        "ingredients": [
            "200g spaghetti",
            "100g pancetta",
            "2 eggs",
            "50g parmesan cheese",
            "Black pepper"
        ],
        "steps": [
            "Cook spaghetti",
            "Fry pancetta",
            "Mix eggs and cheese",
            "Combine everything",
            "Serve with pepper"
        ],
        "image": "https://images.unsplash.com/photo-1588013273468-315fd88ea34c"
    },
    {
        "name": "Pancakes",
        "ingredients": [
            "1 cup flour",
            "1 egg",
            "1 cup milk",
            "2 tbsp sugar",
            "Butter"
        ],
        "steps": [
            "Mix ingredients",
            "Heat pan",
            "Pour batter",
            "Flip pancake",
            "Serve warm"
        ],
        "image": "https://images.unsplash.com/photo-1587734195503-904fca47e0b9"
    }
]

st.set_page_config(page_title="Recipe App", layout="wide")

st.title("🍳 Recipe App")

# Search bar
search = st.text_input("Search recipes")

# Filter recipes
filtered_recipes = [
    r for r in recipes if search.lower() in r["name"].lower()
] if search else recipes

# Sidebar list
st.sidebar.title("Recipes")
recipe_names = [r["name"] for r in filtered_recipes]

selected_recipe = st.sidebar.selectbox(
    "Choose a recipe",
    recipe_names
)

# Display selected recipe
recipe = next(r for r in filtered_recipes if r["name"] == selected_recipe)

st.header(recipe["name"])

# Image
if recipe.get("image"):
    st.image(recipe["image"], use_column_width=True)

# Ingredients
st.subheader("🧂 Ingredients")
for ing in recipe["ingredients"]:
    st.write(f"- {ing}")

# Steps
st.subheader("👨‍🍳 Instructions")
for i, step in enumerate(recipe["steps"], 1):
    st.write(f"{i}. {step}")