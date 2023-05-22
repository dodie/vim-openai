# vim-openai

## Install

- Clone
- Run `install.sh`
- Add `get_openai_completion.sh` to your `$PATH`

## Usage

Export your OpenAI key in the `OPENAI_KEY` environment variable.

### Vim

- Write prompt
- Select text
- `:terminal get_openai_completion.sh <operation> <file_ext>` to get results in a new terminal window will appear with the generated code
- `:!get_openai_completion.sh <operation> <file_ext>` to replace selection with output

#### Example

Write specification for a Python function then select it and execute `:terminal get_openai_completion.sh write_function py`:

![image](https://github.com/dodie/vim-openai/assets/1114220/caf7840e-b7e1-411a-81ab-6826ed7bac8d)

### CLI

```bash
prompt="..."
echo "${prompt}" | get_openai_completion.sh <operation> <file_ext>
```

#### Example

```
echo "Create a dockerfile for nodejs and yarn" | get_openai_completion.sh complete
```

![image](https://github.com/dodie/vim-openai/assets/1114220/df638948-9692-4116-9c0d-fff585b79de6)

## Parameters

- `operation`:
  - `complete` (default): sends the prompt without any modification
  - Coding related:
    - `write_function`
    - `implement_todos_in_function`
    - `review_function`
    - `write_unit_tests_for_function`
  - Writing related:
    - `complete_sentence`
    - `rephrase_text`
    - `proofread`
- `file_ext` should be the extension of the file you are working on

