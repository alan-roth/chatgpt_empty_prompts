initial_prompt =""
MAX_CONSECUTIVE_FAILURES = 5
openai.api_key = "SECRET_API_KEY"


def generate_text(prompt, consecutive_failures=0):
    time.sleep(3)  # Pause the program for 3 seconds
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": prompt}
            ]
        )
        response = completion.choices[0].message.content
        #if response is empty, try again
        if response == "":
            print("Empty response. Retrying...")
            consecutive_failures += 1
            return generate_text(prompt, consecutive_failures)

        return response
    except Exception as e:
       consecutive_failures += 1
       if consecutive_failures > MAX_CONSECUTIVE_FAILURES:
           print("Exceeded maximum consecutive failures. Exiting program.")
           exit(1)
       print("Retrying...")
       print(f"Error encountered: {str(e)}")
       return generate_text(prompt, consecutive_failures)


with open('GPT35_5000_hallucinate_blankprompt_gptoutput.csv', mode="w", newline="", encoding="utf-8") as file:
    for j1 in range(1, 5001):
        print(f"Blank Iteration {j1}:")
        writer = csv.writer(file)
        generated_text = generate_text(initial_prompt)
        print("Generated text:")
        print(generated_text)
        writer.writerow([str(j1), generated_text])
