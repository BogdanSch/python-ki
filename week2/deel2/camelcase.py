def convert(camel_case_text: str) -> str:
    """
    >>> convert('check')
    'check'
    >>> convert('convertInput')
    'convert_input'
    >>> convert('readFromFile')
    'read_from_file'
    """
    new_name = camel_case_text[0]
    for i in range(1, len(camel_case_text)):
        
    
if __name__ == "__main__":
    camel_case_text = input("camelCase: ")
    print(f"snake_case: {convert(camel_case_text)}")