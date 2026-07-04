import pytest
from playwright.sync_api import sync_playwright, expect
import time
import subprocess
import os
import signal


@pytest.fixture(scope="session")
def server():
    """Start FastAPI server for E2E tests"""
    process = subprocess.Popen(
        ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    time.sleep(2)
    
    yield
    
    os.kill(process.pid, signal.SIGTERM)
    process.wait()


class TestBlogAPIE2E:
    """End-to-End tests for Blog API using Playwright"""
    
    @pytest.fixture(autouse=True)
    def setup(self, server):
        """Setup browser for each test"""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        yield
        self.context.close()
        self.browser.close()
        self.playwright.stop()
    
    def test_api_health_check(self, server):
        """Test API is responding to requests"""
        response = self.page.goto("http://127.0.0.1:8000/")
        assert response.status == 200
    
    def test_swagger_documentation_available(self, server):
        """Test Swagger UI documentation is available"""
        self.page.goto("http://127.0.0.1:8000/docs")
        self.page.wait_for_load_state("networkidle")
