from flask import Flask, jsonify
import yaml

app = Flask(__name__)

# 读取 YAML 文件中的版本信息
def load_version_info():
    with open('version_info.yml', 'r') as file:
        return yaml.safe_load(file)

# 获取最新版本号
@app.route('/latest-version', methods=['GET'])
def latest_version():
    data = load_version_info()
    latest_version = data.get('latest_version', 'Unknown')
    return jsonify({'latest_version': latest_version})

# 获取所有版本号
@app.route('/all-versions', methods=['GET'])
def all_versions():
    data = load_version_info()
    all_versions = data.get('all_versions', [])
    return jsonify({'all_versions': all_versions})

if __name__ == '__main__':
    app.run()
