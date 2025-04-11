from lib.grammar_stats import *
import pytest

def test_empty_string_raises_exception():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("")
    error_msg = str(e.value)
    assert error_msg == "No text to analyse!"

def test_correct_string_returns_true():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Shall I compare thee to a Summer's day?")
    result == True

def test_incorrect_string_returns_false_no_caps_or_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("to be or not to be")
    assert result == False

def test_incorrect_string_returns_false_no_caps_and_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("to be or not to be?")
    assert result == False

def test_incorrect_string_returns_false_with_caps_no_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("To be or not to be")
    assert result == False

def test_return_percentage_when_one_is_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Shall I compare thee to a Summer's day?")
    assert grammar_stats.percentage_good() == 100

def test_return_percentage_when_three_are_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Fair is foul and foul is fair!")
    grammar_stats.check("When shall we three meet again?")
    grammar_stats.check("By the pricking of my thumbs, something wicked this way comes.")
    assert grammar_stats.percentage_good() == 100

def test_all_checks_fail():
    grammar_stats = GrammarStats()
    grammar_stats.check("fair is foul and foul is fair!")
    grammar_stats.check("When shall we three meet again")
    grammar_stats.check("by the pricking of my thumbs, something wicked this way comes,")
    assert grammar_stats.percentage_good() == 0

def test_half_checks_fail():
    grammar_stats = GrammarStats()
    grammar_stats.check("Fair is foul and foul is fair!")
    grammar_stats.check("When shall we three meet again")
    assert grammar_stats.percentage_good() == 50

def test_third_checks_fail():
    grammar_stats = GrammarStats()
    grammar_stats.check("Fair is foul and foul is fair!")
    grammar_stats.check("When shall we three meet again")
    grammar_stats.check("By the pricking of my thumbs, something wicked this way comes.")
    assert grammar_stats.percentage_good() == 67