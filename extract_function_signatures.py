import ast

def extract_function_signatures(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()

    tree = ast.parse(code)
    function_signatures = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            parameters = [param.arg for param in node.args.args]
            signature = f"{function_name}({', '.join(parameters)})"
            function_signatures.append(signature)

    return function_signatures

if __name__ == "__main__":
    file_path = "<file_name>.py"
    function_signatures = extract_function_signatures(file_path)

    for signature in function_signatures:
        print(signature)
