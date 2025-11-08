"""
CP1404/CP5632 Practical - languages question.
Estimated time: 18 min
Start time: 12:48
Actual time: 20 min
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programing_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
for language in programing_languages:
    if language.is_dynamic():
        print(language.name)
