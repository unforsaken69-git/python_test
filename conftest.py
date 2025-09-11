# conftest.py
import os
import shutil
import pytest
import subprocess

@pytest.fixture
def sample_data():
    print("\n[Setup] 建立資料")
    yield {"username": "test_user", "password": "1234"}
    print("\n[Teardown] 清除資料")


ALLURE_RESULTS_DIR = "allure-results"
ALLURE_REPORT_DIR = "allure-report"


@pytest.fixture(scope="session", autouse=True)
def clean_reports():
    """
    每次測試前清空 allure 結果與報告資料夾
    """
    for folder in [ALLURE_RESULTS_DIR, ALLURE_REPORT_DIR]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)


def pytest_sessionfinish(session, exitstatus):
    """
    測試結束後自動產生 Allure 報告
    """
    try:
        subprocess.run(
            ["allure", "generate", ALLURE_RESULTS_DIR, "-o", ALLURE_REPORT_DIR, "--clean"],
            shell=True,
            check=True,
        )
        print(f"\n✅ Allure 報告已生成在: {ALLURE_REPORT_DIR}/index.html")
    except Exception as e:
        print(f"\n⚠️  Allure 報告生成失敗: {e}")
