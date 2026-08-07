import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("Error: OPENROUTER_API_KEY environment variable not set")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions
    )

    # Check that the usage data exists
    if response.usage is None:
        raise RuntimeError("API response did not include usage information")

    # Retrieve the message
    message = response.choices[0].message

    # Check if the message has tool calls
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)

            if not result_message.get("content"):
                raise Exception("Empty content in tool response")

            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        # Normal text reply, handle as such
        print(message.content)

    # Print information only if --verbose was used
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")



if __name__ == "__main__":
    main()