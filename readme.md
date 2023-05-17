# vim-openai

## Install

- Clone
- Run `install.sh`
- Add `get_openai_completion.sh` to your `$PATH`

## Usage

### CLI

```bash
prompt="..."
echo "${prompt}" | get_openai_completion.sh <operation> <file_ext>
```

### Vim

- Write prompt
- Select text
- `:terminal get_openai_completion.sh <operation> <file_ext>` to get results in a new terminal window will appear with the generated code
- `:!get_openai_completion.sh <operation> <file_ext>` to replace selection with output

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

## Examples

### CLI

```
echo "Create a dockerfile for nodejs and yarn" | get_openai_completion.sh complete
```

### Vim

TODO
