from lib.inference import generate_text
from lib.get_dataset_question import get_random_math_question
from lib.generate_cot_solution import generate_cot_solution

async def main():
    # Get a random math question
    question, solution = get_random_math_question()
    
    # Generate chain-of-thought solution
    response = await generate_cot_solution(question)
    
    # Print the question and the response
    print(f"Question: {question}")
    print(f"GPT-4 Response: {response}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())








