# -*- coding: UTF-8 -*-
# Example snippet to use in a PYTHONSTARTUP file
try:
    import readline,atexit
except ImportError:
    print "Module readline not available."
else:
    #import tab completion functionality
    import rlcompleter
    #activate tab completion
    readline.parse_and_bind("tab: complete")
    readline.read_history_file()
    atexit.register(pyreadline.write_history_file)
    del readline,rlcompleter,atexit
