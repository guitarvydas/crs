import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd

def install (reg):
    zd.register_component (reg, zd.mkTemplate ( "B", None, instantiator))

def instantiator (reg, owner, name, template_data, arg):
    name_with_id = zd.gensymbol ("B")
    return zd.make_leaf ( name_with_id, owner, None, arg, handler)

def handler (eh, msg):
    # the mevent handler for B
    if msg.port == "q":
        zd.send (eh, "s", "", msg)
    elif msg.port == "r":
        zd.send (eh, "t", "", msg)
    else:
        zd.send (eh, "#", f"{eh.name}: unrecognized mevent {zd.format_mevent (msg)}", msg)
