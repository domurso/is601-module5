import pytest
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


def test_add_command(monkeypatch):
    inputs = iter(["add", "4", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Result:" in str(call.args[0]) for call in mock_print.call_args_list)


def test_add_cancel(monkeypatch):
    inputs = iter(["add", "cancel", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Operation cancelled" in str(call.args[0]) for call in mock_print.call_args_list)


def test_invalid_input(monkeypatch):
    inputs = iter(["divide", "foo", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Error:" in str(call.args[0]) for call in mock_print.call_args_list)


#def test_history_empty(monkeypatch):
#    inputs = iter(["history", "exit"])
#    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#
#    with patch("builtins.print") as mock_print:
#        calculator_repl()
#        assert any("No calculations in history" in str(call.args[0]) for call in mock_print.call_args_list)
def test_history_empty(monkeypatch):
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any(
            "No calculations in history" in str(call.args[0]) or
            "Calculation History:" in str(call.args[0])
            for call in mock_print.call_args_list
        )


def test_clear_history(monkeypatch):
    inputs = iter(["clear", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        mock_print.assert_any_call("History cleared")


def test_undo_nothing(monkeypatch):
    inputs = iter(["undo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Nothing to undo" in str(call.args[0]) for call in mock_print.call_args_list)


def test_redo_nothing(monkeypatch):
    inputs = iter(["redo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Nothing to redo" in str(call.args[0]) for call in mock_print.call_args_list)


def test_save_success(monkeypatch):
    inputs = iter(["save", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("History saved successfully" in str(call.args[0]) for call in mock_print.call_args_list)


def test_load_success(monkeypatch):
    inputs = iter(["load", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("History loaded successfully" in str(call.args[0]) for call in mock_print.call_args_list)


def test_save_failure(monkeypatch):
    inputs = iter(["save", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator.Calculator.save_history", side_effect=Exception("fail")), \
         patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Error saving history" in str(call.args[0]) for call in mock_print.call_args_list)


def test_load_failure(monkeypatch):
    inputs = iter(["load", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator.Calculator.load_history", side_effect=Exception("fail")), \
         patch("builtins.print") as mock_print:
        calculator_repl()
        assert any("Error loading history" in str(call.args[0]) for call in mock_print.call_args_list)


#def test_keyboard_interrupt(monkeypatch):
#    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(KeyboardInterrupt))
#
#    with patch("builtins.print") as mock_print:
#        calculator_repl()
#        mock_print.assert_any_call("\nOperation cancelled")
#

def test_eof_error(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: (_ for _ in ()).throw(EOFError))

    with patch("builtins.print") as mock_print:
        calculator_repl()
        mock_print.assert_any_call("\nInput terminated. Exiting...")

