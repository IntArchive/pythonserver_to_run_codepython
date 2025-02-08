import requests
def run_python(code_python):
    # Đoạn code Python muốn gửi đến server
    python_code = code_python

    # URL của server
    url = "http://localhost:8090/run-python"

    # Gửi yêu cầu POST với dữ liệu code
    response = requests.post(url, json={"code": python_code})

    # Hiển thị kết quả
    return response.json()['output']

if __name__ == "__main__":
    print("Request run python program")
