def normalize_key(text):
    return text.strip().lower().replace("’", "'").replace("`", "'")

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QFrame, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from functools import partial
from data_loader import (
    load_cooking_data,
    load_alchemy_data,
    load_processing_data,
    load_ingredient_data,
    load_imperial_box_data
)

def create_cooking_view(navigate_callback=None, recipe_cards=None):
    data = load_cooking_data()
    widget = QWidget()
    layout = QVBoxLayout(widget)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    content = QWidget()
    grid_layout = QGridLayout(content)
    row = col = 0

    for recipe in data:
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card_layout = QVBoxLayout(card)
        title = QLabel(recipe.get('Recipe Name', 'Unnamed)}')
        title.setStyleSheet("font-weight: bold; font-size: 12pt;")
        card_layout.addWidget(title)
        card_layout.addWidget(QLabel(f"Skill Level: {recipe.get('Skill Level', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Effect: {recipe.get('Effect', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Experience: {recipe.get('Experience', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Silver/Hour: {recipe.get('Silver/Hour', 'N/A)}'}"))
        ingredients_line = recipe.get('Ingredients', ')}'
        ingredients = [i.strip() for i in ingredients_line.split(',)}' if i.strip()]
        for ingredient in ingredients:
            ing_label = QLabel(f"<a href='{ingredient.lower()}'>{ingredient}</a>")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            print(f"[DEBUG] QLabel link set to: {ingredient.lower()}")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            if navigate_callback:
                ing_label.linkActivated.connect(lambda href: print(f"[DEBUG] linkActivated -> {href}"))
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setStyleSheet('color: gold; text-decoration: underline;)}'
            ing_label.setCursor(Qt.PointingHandCursor)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            card_layout.addWidget(ing_label)
        grid_layout.addWidget(card, row, col)
        col += 1
        if col >= 4:
            col = 0
            row += 1
    scroll.setWidget(content)
    layout.addWidget(scroll)
    return widget

def create_alchemy_view(navigate_callback=None, recipe_cards=None):
    data = load_alchemy_data()
    widget = QWidget()
    layout = QVBoxLayout(widget)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    content = QWidget()
    grid_layout = QGridLayout(content)
    row = col = 0

    for recipe in data:
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card_layout = QVBoxLayout(card)
        title = QLabel(recipe.get('Recipe Name', 'Unnamed)}')
        title.setStyleSheet("font-weight: bold; font-size: 12pt;")
        card_layout.addWidget(title)
        card_layout.addWidget(QLabel(f"Skill Level: {recipe.get('Skill Level', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Effect: {recipe.get('Effect', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Experience: {recipe.get('Experience', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Silver/Hour: {recipe.get('Silver/Hour', 'N/A)}'}"))
        ingredients_line = recipe.get('Ingredients', ')}'
        ingredients = [i.strip() for i in ingredients_line.split(',)}' if i.strip()]
        for ingredient in ingredients:
            ing_label = QLabel(f"<a href='{ingredient.lower()}'>{ingredient}</a>")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            print(f"[DEBUG] QLabel link set to: {ingredient.lower()}")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            if navigate_callback:
                ing_label.linkActivated.connect(lambda href: print(f"[DEBUG] linkActivated -> {href}"))
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setStyleSheet('color: gold; text-decoration: underline;)}'
            ing_label.setCursor(Qt.PointingHandCursor)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            card_layout.addWidget(ing_label)
        grid_layout.addWidget(card, row, col)
        col += 1
        if col >= 4:
            col = 0
            row += 1
    scroll.setWidget(content)
    layout.addWidget(scroll)
    return widget

def create_processing_view(navigate_callback=None, recipe_cards=None):
    data = load_processing_data()
    widget = QWidget()
    layout = QVBoxLayout(widget)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    content = QWidget()
    grid_layout = QGridLayout(content)
    row = col = 0

    for entry in data:
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card_layout = QVBoxLayout(card)
        title = QLabel(entry.get('Recipe Name', 'Unnamed)}')
        title.setStyleSheet("font-weight: bold; font-size: 12pt;")
        card_layout.addWidget(title)
        card_layout.addWidget(QLabel(f"Process Type: {entry.get('Process Type', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Experience: {entry.get('Experience', 'N/A)}'}"))
        ingredients_line = entry.get('Ingredients', ')}'
        ingredients = [i.strip() for i in ingredients_line.split(',)}' if i.strip()]
        for ingredient in ingredients:
            ing_label = QLabel(f"<a href='{ingredient.lower()}'>{ingredient}</a>")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            print(f"[DEBUG] QLabel link set to: {ingredient.lower()}")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            if navigate_callback:
                ing_label.linkActivated.connect(lambda href: print(f"[DEBUG] linkActivated -> {href}"))
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setStyleSheet('color: gold; text-decoration: underline;)}'
            ing_label.setCursor(Qt.PointingHandCursor)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            card_layout.addWidget(ing_label)
        grid_layout.addWidget(card, row, col)
        col += 1
        if col >= 4:
            col = 0
            row += 1
    scroll.setWidget(content)
    layout.addWidget(scroll)
    return widget

def create_imperial_boxes_view(navigate_callback=None, recipe_cards=None):
    data = load_imperial_box_data()
    widget = QWidget()
    layout = QVBoxLayout(widget)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    content = QWidget()
    grid_layout = QGridLayout(content)
    row = col = 0

    for box in data:
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card_layout = QVBoxLayout(card)
        title = QLabel(box.get('Recipe Name', 'Unnamed)}')
        title.setStyleSheet("font-weight: bold; font-size: 12pt;")
        card_layout.addWidget(title)
        card_layout.addWidget(QLabel(f"Type: {box.get('Type', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Skill Level: {box.get('Skill Level', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Experience: {box.get('Experience', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Market Price: {box.get('Market Price', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Weight: {box.get('Weight', 'N/A)}'}"))
        ingredients_line = box.get('Ingredients', ')}'
        ingredients = [i.strip() for i in ingredients_line.split(',)}' if i.strip()]
        for ingredient in ingredients:
            ing_label = QLabel(f"<a href='{ingredient.lower()}'>{ingredient}</a>")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            print(f"[DEBUG] QLabel link set to: {ingredient.lower()}")
            ing_label.setTextFormat(Qt.RichText)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setOpenExternalLinks(False)
            if navigate_callback:
                ing_label.linkActivated.connect(lambda href: print(f"[DEBUG] linkActivated -> {href}"))
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            ing_label.setStyleSheet('color: gold; text-decoration: underline;)}'
            ing_label.setCursor(Qt.PointingHandCursor)
            ing_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            card_layout.addWidget(ing_label)
        grid_layout.addWidget(card, row, col)
        col += 1
        if col >= 4:
            col = 0
            row += 1
    scroll.setWidget(content)
    layout.addWidget(scroll)
    return widget

def create_ingredients_view(navigate_callback=None, recipe_cards=None):
    data = load_ingredient_data()
    cards = {}
    widget = QWidget()
    layout = QVBoxLayout(widget)
    scroll = QScrollArea()
    scroll.setObjectName("ingredientScroll")
    scroll.setWidgetResizable(True)
    content = QWidget()
    grid_layout = QGridLayout(content)
    row = col = 0

    for ingredient in data:
        card = QFrame()
        card.setFrameShape(QFrame.StyledPanel)
        card_layout = QVBoxLayout(card)

        title = QLabel(ingredient.get('Ingredient Name', 'Unnamed)}')
        title.setStyleSheet("font-weight: bold; font-size: 12pt;")
        card_layout.addWidget(title)
        card_layout.addWidget(QLabel(f"Category: {ingredient.get('Category', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Source: {ingredient.get('Source', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Market Price: {ingredient.get('Market Price', 'N/A)}'}"))
        card_layout.addWidget(QLabel(f"Weight: {ingredient.get('Weight', 'N/A)}'}"))

        loc = ingredient.get('Location Details', ')}'
        if loc:
            card_layout.addWidget(QLabel(f"Location: {loc}"))

        uses = ingredient.get('Common Uses', ')}'
        if uses and navigate_callback:
            used_in = [r.strip() for r in uses.split(',)}']
            uses_label = QLabel("Used In:")
            card_layout.addWidget(uses_label)
            for recipe in used_in:
                btn = QPushButton(recipe)
                btn.setStyleSheet("font-size: 9pt; padding: 1px 6px;")
                btn.clicked.connect(lambda _, n=recipe: navigate_callback(n.lower()))
                card_layout.addWidget(btn)

        grid_layout.addWidget(card, row, col)
        cards[ingredient.get('Ingredient Name', ')}'.lower()] = card
        col += 1
        if col >= 4:
            col = 0
            row += 1

    scroll.setWidget(content)
    layout.addWidget(scroll)
    return widget, cards, scroll
