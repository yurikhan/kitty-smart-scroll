from typing import Iterator

import kitty.key_encoding as ke


REPORT_ALL_EVENT_TYPES = 2


def main():
    pass


def handle_result(args, result, target_window_id, boss):
    w = boss.window_id_map.get(target_window_id)
    if w is None:
        return

    if w.screen.is_main_linebuf():
        getattr(w, args[1])()
        return

    mods, key = ke.parse_shortcut(args[2])
    shift, alt, ctrl, super, hyper, meta, caps_lock, num_lock = (
        bool(mods & bit) for bit in (
           ke.SHIFT, ke.ALT, ke.CTRL, ke.SUPER,
           ke.HYPER, ke.META, ke.CAPS_LOCK, ke.NUM_LOCK))
    for action in [ke.EventType.PRESS, ke.EventType.RELEASE]:
        key_event = ke.KeyEvent(
            type=action, mods=mods, key=key,
            shift=shift, alt=alt, ctrl=ctrl, super=super,
            hyper=hyper, meta=meta, caps_lock=caps_lock, num_lock=num_lock)
        window_system_event = key_event.as_window_system_event()
        sequence = w.encoded_key(window_system_event)
        w.write_to_child(sequence)


handle_result.no_ui = True
