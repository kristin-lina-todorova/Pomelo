from flask import Flask, request, jsonify
import subprocess
import threading

app = Flask(__name__)

def execute_code(code, result_queue):
    try:
        # Execute the Python code and capture the output
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, timeout=5, universal_newlines=True)
        result_queue.put(result)
    except subprocess.CalledProcessError as e:
        result_queue.put(e.output)
    except subprocess.TimeoutExpired:
        result_queue.put('Code execution timed out.')
    except Exception as e:
        result_queue.put(str(e))

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.json.get('code')
    result_queue = queue.Queue()
    thread = threading.Thread(target=execute_code, args=(code, result_queue))
    thread.start()
    thread.join(timeout=10)  # Wait for thread to finish executing or timeout
    result = result_queue.get()
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True)
