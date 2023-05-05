#!/usr/bin/env bash

current_file="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/get_openai_completion.sh"
original_file=$(realpath "${current_file}")
script_dir=$(dirname "${original_file}")
source ${script_dir}/venv/bin/activate
${script_dir}/get_openai_completion.py $@
