import pytest
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestIsCommandSafe:
    """Tests for tools.is_command_safe() function."""

    def test_safe_echo_command(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("echo hello")
        assert is_safe is True
        assert reason == ""

    def test_safe_dir_command(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("dir")
        assert is_safe is True
        assert reason == ""

    def test_safe_ls_command(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("ls -la")
        assert is_safe is True
        assert reason == ""

    def test_blocked_taskkill_python(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("taskkill /F /IM python.exe")
        assert is_safe is False
        assert "BLOCKED" in reason

    def test_blocked_taskkill_node(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("taskkill /F /IM node.exe")
        assert is_safe is False
        assert "BLOCKED" in reason

    def test_blocked_kill_python(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("kill -9 python")
        assert is_safe is False

    def test_blocked_pkill(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("pkill -f python")
        assert is_safe is False

    def test_blocked_rm_rf_root(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("rm -rf /")
        assert is_safe is False
        assert "BLOCKED" in reason

    def test_blocked_windows_format(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("format c: /fs:ntfs")
        assert is_safe is False

    def test_blocked_rmdir_windows(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("rmdir /s /q c:")
        assert is_safe is False

    def test_blocked_del_windows(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("del /f /s /q c:")
        assert is_safe is False

    def test_blocked_shutdown_windows(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("shutdown /s /t 0")
        assert is_safe is False

    def test_blocked_shutdown_linux(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("shutdown -h now")
        assert is_safe is False

    def test_blocked_registry_delete(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("reg delete HKLM\\Software")
        assert is_safe is False

    def test_blocked_netsh_firewall(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("netsh firewall disable")
        assert is_safe is False

    def test_case_insensitive(self):
        """Test that blocking is case insensitive."""
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("TASKKILL /F /IM python.exe")
        assert is_safe is False

    def test_safe_git_command(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("git status")
        assert is_safe is True

    def test_safe_pip_install(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("pip install requests")
        assert is_safe is True

    def test_safe_python_script(self):
        from liteclaw.tools import is_command_safe
        
        is_safe, reason = is_command_safe("python script.py")
        assert is_safe is True
