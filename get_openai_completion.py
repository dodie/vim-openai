#!/usr/bin/env python3

import openai
import os
import sys

openai.api_key = os.getenv('OPENAI_API_KEY')


# -------------------
# Helper / formatting
# -------------------

def read_stdin():
    code = ""
    for line in sys.stdin:
        code += line
    return code

def get_unit_name(file_ext):
    if file_ext == "py":
        return "Python function"
    elif file_ext == "java":
        return "Java method"
    elif file_ext == "cpp":
        return "C++ function"
    elif file_ext == "js":
        return "JavaScript function"
    elif file_ext == "php":
        return "PHP function"
    elif file_ext == "rb":
        return "Ruby method"
    elif file_ext == "cs":
        return "C# method"
    elif file_ext == "swift":
        return "Swift function"
    elif file_ext == "go":
        return "Go function"
    elif file_ext == "rs":
        return "Rust function"
    elif file_ext == "kt":
        return "Kotlin function"
    elif file_ext == "scala":
        return "Scala function"
    elif file_ext == "ts":
        return "TypeScript function"
    else:
        raise Exception("Unknown Language")

def get_file_ext():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "py"

def remove_wrapping_triple_quotes(code):
    code_lines = code.split('\n')
    if code_lines[0].startswith('```') and code_lines[-1].startswith('```'):
        code_lines = code_lines[1:-1]
    return '\n'.join(code_lines)

def split_paragraph_hint(string):
    if ">>>" in string:
        index = string.index(">>>")
        return (string[:index], string[index+3:])
    else:
        return (string, None)

# ------------------
# Generic completion
# ------------------

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# ------------
# Text related
# ------------

def complete_sentence(text):
    (paragraph, hints) = split_paragraph_hint(text)

    if hints is None:
        prompt = f"""
        Complete the last sentence of the text referenced by @TEXT based on the existing text.
        Just return the last, completed sentence.

        @TEXT: ```{paragraph}```
        """
        return get_completion(prompt)
    else:
        prompt = f"""
        Complete the last sentence of the text referenced by @TEXT based on @HINTS.
        Just return the last, completed sentence.

        @TEXT: ```{paragraph}```
        @HINTS: ```{hints}```
        """
        return get_completion(prompt)

# TODO: diff!
def proofread(text):
    prompt = f"""
    Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use
    any punctuation around the text:
    ```{text}```
    """
    response = get_completion(prompt)
    if response == "No errors found":
        return response
    else:
        # TODO: redlines is not good for the terminal
        # from redlines import Redlines
        # diff = Redlines(text,response)
        # return diff.output_markdown
        return response

# --------------
# Coding related
# --------------

def write_function(spec, unit_name):
    prompt = f"""
    Write a single {unit_name} that implements the specification \
    delimited by triple backticks.

    ```{spec}```

    Only return the code, nothing else.
    """
    return remove_wrapping_triple_quotes(get_completion(prompt))

def implement_todos(spec, unit_name):
    prompt = f"""
    Modify the following {unit_name} based on the instructions in TODO comments.
    If you find any functions in the code that you don't know about, just assume they are working correctly and leave them as they are.

    ```{spec}```

    Only return the code, nothing else.
    """
    return remove_wrapping_triple_quotes(get_completion(prompt))

# Might be slow with the 3 alternatives and explanation + code...
# TODO:
# - Add iterative functions. (Usually being not a chatbot is good but for alternative and fix suggestion it might be good if it could remember.)
#   - See chatbot chapter https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
def suggest_alternatives_for_function(code, unit_name):
    prompt = f"""
    Suggest 3 alternatives for the {unit_name} delimited by triple backticks. Write explanation and code.
    If you find any functions in the code that you don't know about, just assume they are working correctly and leave them as they are.

    ```{spec}```
    """
    return get_completion(prompt)

# TODO: see todo for suggest_alternatives_for_function
def suggest_fixes_for_fixmes(code, unit_name):
    prompt = f"""
    Suggest fixes for the {unit_name} delimited by triple backticks.
    Problems are added as FIXME comments.

    ```{spec}```
    """
    return get_completion(prompt)

def write_unit_tests_for_function(code, unit_name):
    prompt = f"""
    Write unit tests for the {unit_name} delimited by triple backticks.

    ```{spec}```
    """
    return get_completion(prompt)

# TODO: remove. not very good on its own, use write_function with examples
def write_function_for_unit_tests(code, unit_name):
    prompt = f"""
    Write the {unit_name} for the following test cases delimited by triple backticks.

    ```{spec}```
    """
    return get_completion(prompt)

# TODO: remove. not very good on its own, use write_function with examples
def write_function_for_examples(code, unit_name):
    prompt = f"""
    Write the {unit_name} that works like the following examples delimited by triple backticks.

    ```{spec}```
    """
    return get_completion(prompt)

spec = read_stdin()
unit_name = get_unit_name(get_file_ext())
print(write_function(spec, unit_name))
# print(proofread(spec))

