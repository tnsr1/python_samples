from manim import *

class SwapLetters(Scene):
    def construct(self):
        # Исходный текст
        text = Text("Hello World")
        self.play(Write(text))
        self.wait(1)
        
        # Анимация перестановки букв
        swapped_text = Text("World Hello")
        swapped_text.move_to(text)
        self.play(Transform(text, swapped_text))
        self.wait(1)
