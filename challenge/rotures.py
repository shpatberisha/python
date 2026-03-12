from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.recipe import Recipe

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/recipes")
def add_recipe(name: str, ingredients: str, instructions: str, category_id: int, db: Session = Depends(get_db)):
    recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions,
        category_id=category_id
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


@router.get("/recipes")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.recipe import Recipe

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/recipes")
def add_recipe(name: str, ingredients: str, instructions: str, category_id: int, db: Session = Depends(get_db)):
    recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions,
        category_id=category_id
    )
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe


@router.get("/recipes")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()