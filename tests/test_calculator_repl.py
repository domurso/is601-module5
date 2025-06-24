from unittest.mock import patch
from app.calculator_repl import calculator_repl

def test_exit_command(monkeypatch):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    with patch("builtins.print") as mock_print:
        calculator_repl()
        mock_print.assert_any_call("Goodbye!")

def test_help_command(monkeypatch):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    with patch("builtins.print") as mock_print:
        calculator_repl()
        mock_print.assert_any_call("  add, subtract, multiply, divide, power, root - Perform calculations")

def test_unknown_command(monkeypatch):
    inputs = iter(["foobar", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Unknown command" in str(call.args[0]) for call in mock_print.call_args_list)

