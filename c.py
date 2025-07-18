import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd

def install (reg):
    zd.register_component (reg, zd.mkTemplate ( "C", None, instantiator))

def instantiator (reg, owner, name, template_data, arg):
    name_with_id = zd.gensymbol ("C")
    return zd.make_leaf ( name_with_id, owner, None, arg, handler)

def handler (eh, msg):
    # the mevent handler for B
    if msg.port == "q":
        zd.send (eh, "", "v", msg)
    elif msg.port == "r":
        zd.send (eh, "", "w", msg)
    elif msg.port == "s":
        zd.send (eh, "", "x", msg)
    elif msg.port == "t":
        zd.send (eh, "", "y", msg)
    elif msg.port == "u":
        zd.send (eh, "", "z", msg)
    else:
        zd.send (eh, "#", f"{eh.name}: unrecognized mevent {zd.format_mevent (msg)}", msg)
