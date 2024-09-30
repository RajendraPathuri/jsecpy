import javalang

def parse_java_code(java_code):
    try:
        java_ast = javalang.parse.parse(java_code)
    except javalang.parser.JavaSyntaxError as e:
        raise ValueError(f"Error parsing Java code: {str(e)}")

    return java_ast
