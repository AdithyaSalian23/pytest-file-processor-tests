def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            if not data:
                return "Empty file"
            return f"Processed: {len(data)} characters"
    except Exception as e:
        return f"Error: {e}"
