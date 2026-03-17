from fastapi import APIRouter
import pandas as pd
import plotly.express as px
from database import engine

router = APIRouter()

@router.get("/analytics/recipes-per-category")
def recipes_per_category():

    df = pd.read_sql("""
        SELECT categories.name as category, COUNT(recipes.id) as total
        FROM recipes
        JOIN categories
        ON recipes.category_id = categories.id
        GROUP BY categories.name
    """, engine)

    fig = px.bar(df, x="category", y="total", title="Recipes per Category")

    return fig.to_json()


