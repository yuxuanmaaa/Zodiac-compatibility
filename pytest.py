
# ---------------------------------------------------------------------
# Importation
# ---------------------------------------------------------------------

import zodiac_funcs as func


# ---------------------------------------------------------------------
# test function magical_tree
# ---------------------------------------------------------------------

assert callable(func.magical_tree)
assert isinstance(func.zodiac_exist('random'),bool)
assert func.zodiac_exist('aquarius') == True
assert func.zodiac_exist('random') == False

# ---------------------------------------------------------------------
# test function true_name
# ---------------------------------------------------------------------



assert callable(func.true_name)
assert isinstance(func.true_name('mandy'), bool)
assert func.true_name('mandy') == True
assert func.true_name('0324hjsdhfh') == False





