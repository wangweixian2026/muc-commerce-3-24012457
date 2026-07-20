import requests

# 全局会话，全程保持登录状态
session = requests.Session()

# 统一登录（只执行一次）
login_url = "http://127.0.0.1:5500/login"
login_data = {
    "username": "student",
    "password": "day07"
}
session.post(login_url, data=login_data)


# 第一个测试用例
def test_metrics_api():
    res = session.get("http://127.0.0.1:5500/api/metrics")
    assert res.json()["ok"] == True

# 第二个测试用例
def test_category_all():
    res = session.get("http://127.0.0.1:5500/api/categories")
    assert res.json()["category"] == "全部"

def test_errior():
    res = session.get("http://127.0.0.1:5500/400")
    data = res.json()
    assert res.status_code == 400
    assert data["OK"] == False
    assert "error" in data

if __name__ == "__main__":
    test_metrics_api()
    test_category_all()
    print("全部测试通过")

