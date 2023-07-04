import openai
import speech_recognition as sr

openai.api_key = "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"

def chat_with_gpt(question):
    model = "gpt-3.5-turbo"
    user_message = {"role": "user", "content": question}
    response = openai.ChatCompletion.create(
        model=model,
        messages=[user_message]
    )
    reply = response.choices[0].message.get('content')
    return reply

print("ChatGPT: Hello! How can I assist you today?")

while True:
    user_input = input("User (type 'audio' for voice command): ")

    if user_input.lower() == "exit":
        print("ChatGPT: Goodbye!")
        break

    if user_input.lower() == "audio":

        recognizer = sr.Recognizer()


        with sr.Microphone() as source:
            print("Listening...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        try:
            print("Recognizing...")

            command = recognizer.recognize_google(audio)
            print(f"Command: {command}")


            chatbot_response = chat_with_gpt(command)
            print("ChatGPT:", chatbot_response)
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print(f"Error: {e}")
    else:

        chatbot_response = chat_with_gpt(user_input)
        print("ChatGPT:", chatbot_response)