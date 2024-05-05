 Configure your OpenAI API key
openai.api_key = 'ENTER_YOUR_KEY'
# Function to generate images, save them, and write data to a CSV file
def generate_images(prompt, n=100, per_minute=5):
    delay = 60 / per_minute  # Throttle requests to no more than 10 per minute

    with open('image_data2.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['iteration','revised_prompt', 'image_url'])

        for i in range(n):
            try:
                # Generate the image
                response = openai.Image.create(prompt=prompt, n=1, size="1024x1024",  model="dall-e-3",   quality="standard",)

                image_url = response['data'][0]['url']
                # Download and save the image
                image_data = requests.get(image_url).content
                with open(f'image{i}.jpg', 'wb') as img_file:
                    img_file.write(image_data)
                # Write the image data to CSV
                print (response)
                csv_writer.writerow([i, response['data'][0]['revised_prompt'],image_url])
                print(f"Image {i} saved.")
            except Exception as e:
                print(f"An error occurred: {e}")
            time.sleep(delay)  # Delay between requests to avoid rate limits

# Example prompt - replace with your desired prompt
prompt_text = " "

# Call the function to generate and save images and data
generate_images(prompt_text)
