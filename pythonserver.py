from flask import Flask, request, jsonify
import io
import sys

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    try:
        # Nhận đoạn code từ yêu cầu POST
        code = request.json.get('code')
        
        # Chuyển hướng stdout để thu thập output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        # Thực thi đoạn code
        exec_globals = {}
        exec(code, exec_globals)

        # Thu thập kết quả từ stdout
        output = sys.stdout.getvalue()

        # Khôi phục stdout ban đầu
        sys.stdout = old_stdout

        return jsonify({"output": output.strip()})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    # Chạy server trên localhost, cổng 5000
    app.run(host='localhost', port=8090, debug=True)

