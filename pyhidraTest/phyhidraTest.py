import pyhidra

with pyhidra.open_program("test_ls") as flat_api:
    program = flat_api.getCurrentProgram()
    listing = program.getExecutableSHA256()
    print(listing)