@@ -6,6 +6,7 @@


def button_bot(text: str, text_2=None, text_3=None):
    """Кнопки для бота на 3 параметра"""
    if text_2 is None:
        button = VkKeyboard(one_time=False, inline=True)
        button.add_button(text, COLOR_PRIMARY)
@@ -27,6 +28,7 @@ def button_bot(text: str, text_2=None, text_3=None):


def button_bot_age(text_1: str, text_2: str, text_3: str, text_4: str, text_5: str):
    """Кнопки для бота выведи возвраст"""
    button = VkKeyboard(one_time=False, inline=True)
    button.add_button(text_1, COLOR_PRIMARY)
    button.add_button(text_2, COLOR_POSITIVE)
@@ -39,6 +41,7 @@ def button_bot_age(text_1: str, text_2: str, text_3: str, text_4: str, text_5: s


def button_bot_status(text_1: str, text_2: str, text_3: str, text_4: str):
    """Кнопки для бота выведи статус"""
    button = VkKeyboard(one_time=False, inline=True)
    button.add_button(text_1, COLOR_PRIMARY)
    button.add_line()
