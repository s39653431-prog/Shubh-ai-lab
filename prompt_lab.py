print("=== SHUBH AI PROMPT LAB v3.1 ===")
print()

print("1. Study")
print("2. Coding")
print("3. Business")
print("4. Content Creation")

choice = input("\nChoose your category: ")

if choice not in ["1", "2", "3", "4"]:
    print("\n❌ Invalid category. Please choose 1, 2, 3, or 4.")
else:
    topic = input("Enter your topic: ").strip()
    level = input("Enter your level: ").strip()
    language = input("Enter your preferred language: ").strip()

    if not topic or not level or not language:
        print("\n❌ Topic, level and language cannot be empty.")
    else:
        print("\n=== GENERATED PROMPT ===")

        if choice == "1":
            prompt = f"""
Act as an expert teacher.

Teach me about: {topic}

Student level: {level}
Preferred language: {language}

Explain the topic step by step in simple language.
Use clear examples and important points.
If there are formulas, explain what they mean and when to use them.
"""

        elif choice == "2":
            prompt = f"""
Act as an expert programming mentor.

Programming topic: {topic}

Student level: {level}
Preferred language: {language}

Explain the concept step by step.
Give a simple example and explain the code clearly.
Also mention common mistakes beginners make.
"""

        elif choice == "3":
            prompt = f"""
Act as a startup and business mentor.

Business topic: {topic}

Experience level: {level}
Preferred language: {language}

Analyze the idea practically.
Explain target customers, competition, advantages,
risks, possible improvements and a simple action plan.
"""

        else:
            prompt = f"""
Act as an expert content strategist.

Content topic: {topic}

Creator level: {level}
Preferred language: {language}

Create a practical content plan with:
- Strong hook
- Main idea
- Structure
- Audience
- Call to action
"""

        print(prompt)
        print("\n[Prompt generated successfully]")
