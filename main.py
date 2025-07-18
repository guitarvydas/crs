import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd
import b
import c

try:
    [palette, env] = zd.initialize_from_files (sys.argv[1], sys.argv[4:])
    b.install (palette)
    c.install (palette)
    top = zd.start_bare (part_name=sys.argv[3], palette=palette, env=env)
    zd.inject_mevent (top, "q", "")
    zd.inject_mevent (top, "r", "")
except Exception as e:
    _, _, tb = sys.exc_info()
    while tb.tb_next:
        tb = tb.tb_next
    frame = tb.tb_frame
    filename = frame.f_code.co_filename
    line_number = tb.tb_lineno
    print(f"\n\n\n*** {type(e).__name__} at {filename}:{line_number}: {e}", file=sys.stderr)
