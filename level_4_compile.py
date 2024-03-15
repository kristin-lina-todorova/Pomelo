import subprocess

def execute_python_code(code):
    try:
        with open('temp_code.py', 'w') as file:
            file.write(code)
        
        result = subprocess.check_output(['python', 'temp_code.py'], stderr=subprocess.STDOUT, timeout=5, universal_newlines=True)
        
        return result.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()
    except subprocess.TimeoutExpired:
        return 'Code execution timed out.'
    except Exception as e:
        return str(e)
