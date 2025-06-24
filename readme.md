============================= test session starts ==============================
platform linux -- Python 3.13.3, pytest-8.3.3, pluggy-1.5.0 -- /home/loki/documents/coding/is601/module5/venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/loki/documents/coding/is601/module5
configfile: pytest.ini
testpaths: tests
plugins: pylint-0.21.0, cov-6.0.0
collecting ... collected 119 items

tests/test_calculation.py::test_addition PASSED                          [  0%]
tests/test_calculation.py::test_subtraction PASSED                       [  1%]
tests/test_calculation.py::test_multiplication PASSED                    [  2%]
tests/test_calculation.py::test_division PASSED                          [  3%]
tests/test_calculation.py::test_division_by_zero PASSED                  [  4%]
tests/test_calculation.py::test_power PASSED                             [  5%]
tests/test_calculation.py::test_negative_power PASSED                    [  5%]
tests/test_calculation.py::test_root PASSED                              [  6%]
tests/test_calculation.py::test_invalid_root PASSED                      [  7%]
tests/test_calculation.py::test_unknown_operation PASSED                 [  8%]
tests/test_calculation.py::test_to_dict PASSED                           [  9%]
tests/test_calculation.py::test_from_dict PASSED                         [ 10%]
tests/test_calculation.py::test_invalid_from_dict PASSED                 [ 10%]
tests/test_calculation.py::test_format_result PASSED                     [ 11%]
tests/test_calculation.py::test_equality PASSED                          [ 12%]
tests/test_calculation.py::test_from_dict_result_mismatch PASSED         [ 13%]
tests/test_calculator.py::test_calculator_initialization PASSED          [ 14%]
tests/test_calculator.py::test_logging_setup PASSED                      [ 15%]
tests/test_calculator.py::test_add_observer PASSED                       [ 15%]
tests/test_calculator.py::test_remove_observer PASSED                    [ 16%]
tests/test_calculator.py::test_set_operation PASSED                      [ 17%]
tests/test_calculator.py::test_perform_operation_addition PASSED         [ 18%]
tests/test_calculator.py::test_perform_operation_validation_error PASSED [ 19%]
tests/test_calculator.py::test_perform_operation_operation_error PASSED  [ 20%]
tests/test_calculator.py::test_undo PASSED                               [ 21%]
tests/test_calculator.py::test_redo PASSED                               [ 21%]
tests/test_calculator.py::test_save_history PASSED                       [ 22%]
tests/test_calculator.py::test_load_history PASSED                       [ 23%]
tests/test_calculator.py::test_clear_history PASSED                      [ 24%]
tests/test_calculator.py::test_calculator_repl_exit PASSED               [ 25%]
tests/test_calculator.py::test_calculator_repl_help PASSED               [ 26%]
tests/test_calculator.py::test_calculator_repl_addition PASSED           [ 26%]
tests/test_calculator.py::test_undo_empty_stack_returns_false PASSED     [ 27%]
tests/test_calculator.py::test_redo_empty_stack_returns_false PASSED     [ 28%]
tests/test_calculator.py::test_history_trimmed_when_exceeds_max PASSED   [ 29%]
tests/test_calculator.py::test_save_empty_history_creates_empty_csv PASSED [ 30%]
tests/test_calculator.py::test_load_history_no_file_logs_info PASSED     [ 31%]
tests/test_calculator_repl.py::test_exit_command PASSED                  [ 31%]
tests/test_calculator_repl.py::test_help_command PASSED                  [ 32%]
tests/test_calculator_repl.py::test_unknown_command PASSED               [ 33%]
tests/test_calculator_repl.py::test_add_command PASSED                   [ 34%]
tests/test_calculator_repl.py::test_add_cancel PASSED                    [ 35%]
tests/test_calculator_repl.py::test_invalid_input PASSED                 [ 36%]
tests/test_calculator_repl.py::test_history_empty PASSED                 [ 36%]
tests/test_calculator_repl.py::test_clear_history PASSED                 [ 37%]
tests/test_calculator_repl.py::test_undo_nothing PASSED                  [ 38%]
tests/test_calculator_repl.py::test_redo_nothing PASSED                  [ 39%]
tests/test_calculator_repl.py::test_save_success PASSED                  [ 40%]
tests/test_calculator_repl.py::test_load_success PASSED                  [ 41%]
tests/test_calculator_repl.py::test_save_failure PASSED                  [ 42%]
tests/test_calculator_repl.py::test_load_failure PASSED                  [ 42%]
tests/test_calculator_repl.py::test_eof_error PASSED                     [ 43%]
tests/test_config.py::test_default_configuration PASSED                  [ 44%]
tests/test_config.py::test_custom_configuration PASSED                   [ 45%]
tests/test_config.py::test_directory_properties PASSED                   [ 46%]
tests/test_config.py::test_file_properties PASSED                        [ 47%]
tests/test_config.py::test_invalid_max_history_size PASSED               [ 47%]
tests/test_config.py::test_invalid_precision PASSED                      [ 48%]
tests/test_config.py::test_invalid_max_input_value PASSED                [ 49%]
tests/test_config.py::test_auto_save_env_var_true PASSED                 [ 50%]
tests/test_config.py::test_auto_save_env_var_one PASSED                  [ 51%]
tests/test_config.py::test_auto_save_env_var_false PASSED                [ 52%]
tests/test_config.py::test_auto_save_env_var_zero PASSED                 [ 52%]
tests/test_config.py::test_environment_overrides PASSED                  [ 53%]
tests/test_config.py::test_default_fallbacks PASSED                      [ 54%]
tests/test_config.py::test_get_project_root PASSED                       [ 55%]
tests/test_config.py::test_log_dir_property PASSED                       [ 56%]
tests/test_config.py::test_history_dir_property PASSED                   [ 57%]
tests/test_config.py::test_log_file_property PASSED                      [ 57%]
tests/test_config.py::test_history_file_property PASSED                  [ 58%]
tests/test_exceptions.py::test_calculator_error_is_base_exception PASSED [ 59%]
tests/test_exceptions.py::test_validation_error_is_calculator_error PASSED [ 60%]
tests/test_exceptions.py::test_validation_error_specific_exception PASSED [ 61%]
tests/test_exceptions.py::test_operation_error_is_calculator_error PASSED [ 62%]
tests/test_exceptions.py::test_operation_error_specific_exception PASSED [ 63%]
tests/test_exceptions.py::test_configuration_error_is_calculator_error PASSED [ 63%]
tests/test_exceptions.py::test_configuration_error_specific_exception PASSED [ 64%]
tests/test_history.py::test_logging_observer_logs_calculation PASSED     [ 65%]
tests/test_history.py::test_logging_observer_no_calculation PASSED       [ 66%]
tests/test_history.py::test_autosave_observer_triggers_save PASSED       [ 67%]
tests/test_history.py::test_autosave_observer_logs_autosave PASSED       [ 68%]
tests/test_history.py::test_autosave_observer_does_not_trigger_save_when_disabled PASSED [ 68%]
tests/test_history.py::test_autosave_observer_invalid_calculator PASSED  [ 69%]
tests/test_history.py::test_autosave_observer_no_calculation PASSED      [ 70%]
tests/test_operations.py::TestOperation::test_str_representation PASSED  [ 71%]
tests/test_operations.py::TestAddition::test_valid_operations PASSED     [ 72%]
tests/test_operations.py::TestAddition::test_invalid_operations PASSED   [ 73%]
tests/test_operations.py::TestSubtraction::test_valid_operations PASSED  [ 73%]
tests/test_operations.py::TestSubtraction::test_invalid_operations PASSED [ 74%]
tests/test_operations.py::TestMultiplication::test_valid_operations PASSED [ 75%]
tests/test_operations.py::TestMultiplication::test_invalid_operations PASSED [ 76%]
tests/test_operations.py::TestDivision::test_valid_operations PASSED     [ 77%]
tests/test_operations.py::TestDivision::test_invalid_operations PASSED   [ 78%]
tests/test_operations.py::TestPower::test_valid_operations PASSED        [ 78%]
tests/test_operations.py::TestPower::test_invalid_operations PASSED      [ 79%]
tests/test_operations.py::TestRoot::test_valid_operations PASSED         [ 80%]
tests/test_operations.py::TestRoot::test_invalid_operations PASSED       [ 81%]
tests/test_operations.py::TestOperationFactory::test_create_valid_operations PASSED [ 82%]
tests/test_operations.py::TestOperationFactory::test_create_invalid_operation PASSED [ 83%]
tests/test_operations.py::TestOperationFactory::test_register_valid_operation PASSED [ 84%]
tests/test_operations.py::TestOperationFactory::test_register_invalid_operation PASSED [ 84%]
tests/test_validators.py::test_validate_number_positive_integer PASSED   [ 85%]
tests/test_validators.py::test_validate_number_positive_decimal PASSED   [ 86%]
tests/test_validators.py::test_validate_number_positive_string_integer PASSED [ 87%]
tests/test_validators.py::test_validate_number_positive_string_decimal PASSED [ 88%]
tests/test_validators.py::test_validate_number_negative_integer PASSED   [ 89%]
tests/test_validators.py::test_validate_number_negative_decimal PASSED   [ 89%]
tests/test_validators.py::test_validate_number_negative_string_integer PASSED [ 90%]
tests/test_validators.py::test_validate_number_negative_string_decimal PASSED [ 91%]
tests/test_validators.py::test_validate_number_zero PASSED               [ 92%]
tests/test_validators.py::test_validate_number_trimmed_string PASSED     [ 93%]
tests/test_validators.py::test_validate_number_invalid_string PASSED     [ 94%]
tests/test_validators.py::test_validate_number_exceeds_max_value PASSED  [ 94%]
tests/test_validators.py::test_validate_number_exceeds_max_value_string PASSED [ 95%]
tests/test_validators.py::test_validate_number_exceeds_negative_max_value PASSED [ 96%]
tests/test_validators.py::test_validate_number_empty_string PASSED       [ 97%]
tests/test_validators.py::test_validate_number_whitespace_string PASSED  [ 98%]
tests/test_validators.py::test_validate_number_none_value PASSED         [ 99%]
tests/test_validators.py::test_validate_number_non_numeric_type PASSED   [100%]

---------- coverage: platform linux, python 3.13.3-final-0 -----------
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
app/__init__.py                 0      0   100%
app/calculation.py             47      4    91%   81, 188, 200, 222
app/calculator.py             133     16    88%   103-106, 230-233, 272-275, 309-312, 324-333
app/calculator_config.py       42      0   100%
app/calculator_memento.py      13      2    85%   34, 53
app/calculator_repl.py        106     16    85%   63, 79, 87, 120-121, 138-140, 148-149, 154-163
app/exceptions.py               8      0   100%
app/history.py                 23      0   100%
app/input_validators.py        18      0   100%
app/operations.py              62      0   100%
---------------------------------------------------------
TOTAL                         452     38    92%
Coverage HTML written to dir htmlcov


============================= 119 passed in 0.79s ==============================
