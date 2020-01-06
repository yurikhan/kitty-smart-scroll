import kitty.conf.utils as ku
import kitty.key_encoding as ke
from kitty import keys
import kitty.fast_data_types as fdt


def main():
    pass


def actions(extended):
    yield keys.defines.GLFW_PRESS
    if extended:
        yield keys.defines.GLFW_RELEASE


def mods_to_glfw(mods):
    return sum(glfw
               for mod, glfw in {ke.SHIFT: fdt.GLFW_MOD_SHIFT,
                                 ke.CTRL:  fdt.GLFW_MOD_CONTROL,
                                 ke.ALT:   fdt.GLFW_MOD_ALT,
                                 ke.SUPER: fdt.GLFW_MOD_SUPER}.items()
               if mods & mod)


def handle_result(args, result, target_window_id, boss):
    w = boss.window_id_map.get(target_window_id)
    if w is None:
        return

    if w.screen.is_main_linebuf():
        getattr(w, args[1])()
        return

    mods, key, is_text = ku.parse_kittens_shortcut(args[2])
    if is_text:
        w.send_text(key)
        return

    extended = w.screen.extended_keyboard
    for action in actions(extended):
        sequence = (
            ('\x1b_{}\x1b\\' if extended else '{}')
            .format(
                keys.key_to_bytes(
                    getattr(keys.defines, 'GLFW_KEY_{}'.format(key)),
                    w.screen.cursor_key_mode, extended,
                    mods_to_glfw(mods), action)
                .decode('ascii')))
        w.write_to_child(sequence)


handle_result.no_ui = True
