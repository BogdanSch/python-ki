def convert(camel_case_text: str) -> str:
    """
    >>> convert('check')
    'check'
    >>> convert('convertInput')
    'convert_input'
    >>> convert('readFromFile')
    'read_from_file'
    >>> convert('')
    ''
    """
    if len(camel_case_text) == 0:
        return ""
    
    new_name = camel_case_text[0]
    for i in range(1, len(camel_case_text)):
        if camel_case_text[i].isupper():
            new_name += f"_{camel_case_text[i].lower()}"
        else:
            new_name += camel_case_text[i]
    return new_name
    
if __name__ == "__main__":
    camel_case_text = input("camelCase: ")
    print(f"snake_case: {convert(camel_case_text)}")