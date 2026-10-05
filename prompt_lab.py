print("=== SHUBH AI PROMPT LAB ===")
print()

print("1. Study")
print("2. Coding")
print("3. Business")
print("4. Content Creation")

choice = input("\nChoose your category: ")

if choice == "1":
    print("\nStudy Prompt:")
    print("Explain this topic simply, step by step, with examples.")

elif choice == "2":
    print("\nCoding Prompt:")
    print("Act as a coding mentor. Explain the problem, solution, and code step by step.")

elif choice == "3":
    print("\nBusiness Prompt:")
    print("Analyze this business idea, its customers, competition, risks, and opportunities.")

elif choice == "4":
    print("\nContent Prompt:")
    print("Create an engaging content idea with a strong hook, structure, and call to action.")

else:
    print("\nInvalid choice. Please select 1, 2, 3, or 4.")
