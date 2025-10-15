from manim import *
from sympy import Symbol

class SwapLetters(Scene):
    def construct(self):
        # Определим символы
        x = Symbol('x')
        y = Symbol('y') 
        
        # Создаем исходный текст
        text = MathTex("x^2+y^2")
        self.add(text)
        
        # Новый порядок символов
        swapped_text = MathTex("y^2+x^2")  # Преобразуем формулу в новый вид
        
        # Перемещаем новую надпись туда же, куда была старая
        swapped_text.move_to(text.get_center())
        
        # Анимация замены текста
        self.play(TransformMatchingShapes(text, swapped_text))
        self.wait()