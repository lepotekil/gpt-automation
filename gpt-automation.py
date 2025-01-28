import argparse
import openai
import os

client = openai.OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


if __name__ == '__main__':
    print("Starting GPT Automation...")

    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--role', help='The role of the user', choices=['user', 'developer', 'assistant'], type=str, required=True)
    parser.add_argument('-m', '--model', help='The model to use for OpenAI', type=str, required=True)
    parser.add_argument('-p', '--prompt', help='The filename containing the prompt to use for OpenAI', type=str, required=True)
    parser.add_argument('-i', '--input', help='The filename containing the data to process with OpenAI', type=str, required=True)
    parser.add_argument('-o', '--output', help='The filename to save the output to', type=str, required=True)

    args = parser.parse_args()

    with open(args.prompt, 'r') as prompt_file:
        prompt_content = prompt_file.read()


    with open(args.input, 'r') as input_file:
        input_content = input_file.read()

    content = f"{prompt_content}\n\n\n{input_content}"

    completion = client.chat.completions.create(
        model=args.model,
        messages=[{"role": args.role, "content": content}],
        response_format={"type": "text"}
    )

    with open(args.output, 'w') as output_file:
        output_file.write(completion.choices[0].message.content)

    print("Ending GPT Automation...")    