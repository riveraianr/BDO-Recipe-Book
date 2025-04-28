
from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QTabWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import app_config
from app_logic import create_cooking_view, create_ingredients_view, create_alchemy_view, create_processing_view, create_imperial_boxes_view

class RecipeBookUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app_config.APP_TITLE)
        self.setWindowIcon(QIcon(app_config.APP_ICON_PATH))
        self.setGeometry(100, 100, 1200, 800)

        self.ingredient_cards = {}  # name (lowercase) -> widget
        self.recipe_cards = {}      # recipe name (lowercase) -> card widget
        self.ingredient_scroll_area = None

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        top_bar = QHBoxLayout()
        top_bar.setAlignment(Qt.AlignRight)
        self.theme_toggle = QPushButton("Toggle Theme")
        self.theme_toggle.setFixedWidth(120)
        self.theme_toggle.clicked.connect(self.toggle_theme)
        top_bar.addWidget(self.theme_toggle)
        main_layout.addLayout(top_bar)

        self.tabs = QTabWidget()

        cooking_view = create_cooking_view(self.navigate_to_ingredient, self.recipe_cards)
        ingredients_view, self.ingredient_cards, self.ingredient_scroll_area = create_ingredients_view(self.navigate_to_ingredient)
        alchemy_view = create_alchemy_view(self.navigate_to_ingredient, self.recipe_cards)

        self.tabs.addTab(cooking_view, "Cooking")
        self.tabs.addTab(alchemy_view, "Alchemy")
        self.tabs.addTab(create_processing_view(self.navigate_to_ingredient), "Processing")
        self.tabs.addTab(create_imperial_boxes_view(self.navigate_to_ingredient), "Imperial Boxes")
        self.tabs.addTab(ingredients_view, "Ingredients")

        main_layout.addWidget(self.tabs)

        self.current_theme = "dark"
        self.apply_theme()

    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.apply_theme()

    def apply_theme(self):
        from app_config import get_dark_palette, get_light_palette
        QApplication.setStyle("Fusion")
        self.setPalette(get_dark_palette() if self.current_theme == "dark" else get_light_palette())

    def navigate_to_ingredient(self, name):
        name = name.lower().strip()

        if name in self.ingredient_cards:
            self.tabs.setCurrentIndex(4)
            def scroll_to_ingredient():
                card = self.ingredient_cards[name]
                bar = self.ingredient_scroll_area.verticalScrollBar()
                bar.setValue(card.y() - 20)
                card.setStyleSheet(card.styleSheet() + "border: 2px solid gold;")
                QTimer.singleShot(1500, lambda: card.setStyleSheet(card.styleSheet().replace("border: 2px solid gold;", "")))
            QTimer.singleShot(300, scroll_to_ingredient)
            return

        if name in self.recipe_cards:
            target_card = self.recipe_cards[name]
            tab_index = target_card.property("tab_index")
            scroll_area = target_card.property("scroll_area")
            if tab_index is not None and scroll_area:
                self.tabs.setCurrentIndex(tab_index)
                def scroll_to_recipe():
                    bar = scroll_area.verticalScrollBar()
                    bar.setValue(target_card.y() - 20)
                    target_card.setStyleSheet(target_card.styleSheet() + "border: 2px solid gold;")
                    QTimer.singleShot(1500, lambda: target_card.setStyleSheet(target_card.styleSheet().replace("border: 2px solid gold;", "")))
                QTimer.singleShot(300, scroll_to_recipe)
