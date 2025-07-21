import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd
import b
import c
import d

try:
    # argv[1] is the directory path for this project (i.e. "."), no trailing slash
    # argv[2] is the string to be injected into the "" port of the system, once running
    # argv[3] is the name of the Part ("main" in this case - the "main" tab of crs.drawio)
    # argv[4:] are JSON files representing the Container parts of the system
    # b.py, c.py, d.py are Leaf parts (written in Python in this case)
    [palette, env] = zd.initialize_from_files (sys.argv[1], sys.argv[4:])
    b.install (palette)
    c.install (palette)
    d.install (palette)
    top = zd.start (arg=sys.argv[2], part_name=sys.argv[3], palette=palette, env=env)
except Exception as e:
    # this stuff makes the exception output less verbose
    #  in general we don't expect to get any exceptions, here, but, bugs and typos happen when humans write code
    _, _, tb = sys.exc_info()
    while tb.tb_next:
        tb = tb.tb_next
    frame = tb.tb_frame
    filename = frame.f_code.co_filename
    line_number = tb.tb_lineno
    print(f"\n\n\n*** {type(e).__name__} at {filename}:{line_number}: {e}", file=sys.stderr)
