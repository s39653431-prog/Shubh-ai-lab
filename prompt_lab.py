print("=== SHUBH AI PROMPT LAB v2 ===")
print()

print("1. Study")
print("2. Coding")
print("3. Business")
print("4. Content Creation")

choice = input("\nChoose your category: ")
topic = input("Enter your topic: ")

if choice == "1":
    print("\nStudy Prompt:")
    print(f"Explain {topic} to a student in simple language, step by step, with examples.")

elif choice == "2":
    print("\nCoding Prompt:")
    print(f"Act as a coding mentor. Explain {topic}, provide a solution, and explain the code step by step.")

elif choice == "3":
    print("\nBusiness Prompt:")
    print(f"Analyze the business idea '{topic}', including customers, competition, risks, and opportunities.")

elif choice == "4":
    print("\nContent Prompt:")
    print(f"Create an engaging content plan about '{topic}' with a strong hook, structure, and call to action.")

else:
    print("\nInvalid choice. Please select 1, 2, 3, or 4.")

print("\n[Prompt generated successfully]")
