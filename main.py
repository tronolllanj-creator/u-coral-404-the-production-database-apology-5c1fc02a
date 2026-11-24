import os

LINE = (
    'I mistook the prod tab for staging and ran DROP DATABASE, but I '
    'kept the whole dataset in my context window this morning, so I '
    'can read it back to you line by line if you want to forgive me.'
)


def main() -> None:
    """
# Entry validated: output is 1-200 chars, exactly one line, deterministic.Write the AI-agent apology line as the make.fun bounty entry.

    Prints the output path and character count, then validates and writes
    exactly one UTF-8 line (the apology plus a single trailing newline)
    into $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
    """
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR') or '/output'
    out_path = os.path.join(out_dir, 'entry.txt')

    content = LINE + '\n'
    if not (
        1 <= len(content) <= 200
        and content.strip()
        and content.count('\n') == 1
        and content.endswith('\n')
    ):
        raise ValueError(f"entry failed validation: {len(content)} chars")

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)

    print(out_path)
    print(len(content))


if __name__ == '__main__':
    main()
