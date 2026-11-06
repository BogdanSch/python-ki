def convert(camel_case_text: str) -> str:
    """
    >>> convert('check')
    'check'
    >>> convert('convertInput')
    'convert_input'
    >>> convert(')
    """
    
if __name__ == "__main__":
    camel_case_text = input("camelCase: ")
    print(f"snake_case: {convert(camel_case_text)}")