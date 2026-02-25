import pytest
import os
import platform
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestGetDefaultWorkDir:
    """Tests for config.get_default_work_dir() function."""

    def test_returns_string(self):
        from liteclaw.config import get_default_work_dir
        result = get_default_work_dir()
        assert isinstance(result, str)

    def test_windows_path(self, monkeypatch):
        """Test Windows path is returned on Windows."""
        from liteclaw.config import get_default_work_dir
        
        class MockPlatform:
            system = staticmethod(lambda: "Windows")
        
        monkeypatch.setattr("liteclaw.config.platform", MockPlatform)
        
        result = get_default_work_dir()
        assert result == r"C:\liteclaw"

    def test_linux_path(self):
        """Test Linux path is returned on Linux (on Windows, checks default works)."""
        from liteclaw.config import get_default_work_dir
        result = get_default_work_dir()
        assert "liteclaw" in result
        assert isinstance(result, str)

    def test_mac_path(self):
        """Test Mac path returns something with liteclaw."""
        from liteclaw.config import get_default_work_dir
        result = get_default_work_dir()
        assert "liteclaw" in result
        assert isinstance(result, str)


class TestSettingsMethods:
    """Tests for Settings class methods."""

    def test_get_screenshots_dir(self):
        from liteclaw.config import Settings
        
        settings = Settings(WORK_DIR="/test/work")
        result = settings.get_screenshots_dir()
        assert result.endswith("screenshots")

    def test_get_configs_dir(self):
        from liteclaw.config import Settings
        
        settings = Settings(WORK_DIR="/test/work")
        result = settings.get_configs_dir()
        assert result.endswith("configs")

    def test_get_notes_dir(self):
        from liteclaw.config import Settings
        
        settings = Settings(WORK_DIR="/test/work")
        result = settings.get_notes_dir()
        assert result.endswith("notes")

    def test_get_exports_dir(self):
        from liteclaw.config import Settings
        
        settings = Settings(WORK_DIR="/test/work")
        result = settings.get_exports_dir()
        assert result.endswith("exports")

    def test_get_agent_instructions_path(self):
        from liteclaw.config import Settings
        
        settings = Settings(WORK_DIR="/test/work")
        result = settings.get_agent_instructions_path()
        assert result.endswith("AGENT.md")

    def test_chrome_user_data_dir_property(self):
        from liteclaw.config import Settings
        
        settings = Settings(WORK_DIR="/test/work")
        result = settings.CHROME_USER_DATA_DIR
        assert result.endswith("browser")

    def test_default_values(self):
        """Test Settings has expected default values."""
        from liteclaw.config import Settings
        
        settings = Settings()
        
        assert settings.LLM_PROVIDER is not None
        assert settings.LLM_MODEL is not None
        assert settings.WHATSAPP_TYPE == "selenium"
        assert settings.BREAK_UNTIL == 0
        assert settings.WHATSAPP_SESSION_ID == "whatsapp"
