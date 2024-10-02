import ex00

key = ex00.key()
assert len(key) == 1337, "len(key) == 1337"
assert key[404] == 3, "key[404] == 3"
assert key > 9000, "key > 9000"
assert key.passphrase == "zax2rulez", "key.passphrase == \"zax2rulez\""
assert str(key) == "GeneralTsoKeycard", "str(key) == \"GeneralTsoKeycard\""