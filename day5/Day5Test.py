import day5

def test_reacting_lower_higher():
    assert day5.reacting('a','A') == True

def test_reacting_higher_lower():
    assert day5.reacting('a','A') == True

def test_reacting_not_matching():
    assert day5.reacting('a','B') == False

def test_reacting_not_matching_higher():
    assert day5.reacting('A','b') == False

def test_reacting_not_matching_equal():
    assert day5.reacting('B','B') == False

def test_react_polymer_once():
    assert day5.react_polymer_once("aA") == ''

def test_react_polymer_once_odd():
    assert day5.react_polymer_once("aAB") == 'B'

def test_react_polymer_once_multiple():
        assert day5.react_polymer_once("caABB") == 'cBB'

def test_react_polymer_leaves_nothing():
        assert day5.react_polymer("abBA") == ''

def test_react_polymer_sample_input():
        assert day5.react_polymer("dabAcCaCBAcCcaDA") == 'dabCBAcaDA'        
