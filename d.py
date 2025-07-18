import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd

def install (reg):
    zd.register_component (reg, zd.mkTemplate ( "D", None, instantiator))

def instantiator (reg, owner, name, template_data, arg):
    name_with_id = zd.gensymbol ("D")
    return zd.make_leaf ( name_with_id, owner, None, arg, handler)

def handler (eh, msg):
    # the mevent handler for D
    if msg.port == "":
        if msg.datum.v == "q":
            zd.send (eh, "", "u", msg)
        else:
            pass
    else:
        zd.send (eh, "#", f"{eh.name}: unrecognized mevent {zd.format_mevent (msg)}", msg)
