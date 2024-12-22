import os
import tiktoken

# Ensure the tiktoken library is installed
try:
    import tiktoken
except ImportError:
    import subprocess
    subprocess.check_call(['pip', 'install', 'tiktoken'])
    import tiktoken

# Function to read the input file and chunk it
def chunk_text_file(input_file, output_folder, chunk_size=2048):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    # Split tokens into chunks
    chunks = [tokens[i:i + chunk_size] for i in range(0, len(tokens), chunk_size)]

    # Decode and save each chunk
    for i, chunk in enumerate(chunks, start=1):
        chunk_text = tokenizer.decode(chunk)
        output_file = os.path.join(output_folder, f'chunk{i}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(chunk_text)
        print(f'Chunk {i} saved with {len(chunk)} tokens.')

if __name__ == "__main__":
    input_file = 'folder/file.txt'
    output_folder = 'folder'
    chunk_text_file(input_file, output_folder)