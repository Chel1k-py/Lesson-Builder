import random


def cut(text, length):
    if len(text) <= length:
        return text

    text = text[:length].rsplit(" ", 1)[0]

    return text + "..."


def generates(data):
    theme = data.get("theme")
    audience = data.get("audience")
    duration = data.get("duration")
    tools = data.getlist("tools")

    theme = cut(theme, 20)

    starts = [
        "Начать с загадки по теме",
        "Показать короткое видео",
        "Задать неожиданный вопрос классу"
    ]

    mains = [
        "Работа в группах с обсуждением",
        "Интерактивная викторина",
        "Творческое задание (рисунок или мини-проект)"
    ]

    reflections = [
        "Облако слов",
        "Мини-опрос",
        "Обсуждение: что было самым интересным"
    ]

    return {
        "title": f"{theme}",
        "audience": audience,
        "goal": f"Познакомить учащихся с темой: {theme}",
        "start": random.choice(starts),
        "main": random.choice(mains) + f" с использованием: {', '.join(tools)}",
        "reflection": random.choice(reflections),
        "conclusion": "Культура народов России разнообразна и уникальна"
    }

