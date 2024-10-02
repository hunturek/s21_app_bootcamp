def fix_wiring(cables, sockets, plugs):
    yield '\n'.join(
        [f'plug {c} into {s} using {p}' for c, s, p in zip(
            (item for item in cables if isinstance(item, str)),
            (item for item in sockets if isinstance(item, str)),
            (item for item in plugs if isinstance(item, str))
        )] + 
        [f'weld {c} to {s} without plug' for c, s in zip(
            list(item for item in cables if isinstance(item, str))[len(plugs):],
            list(item for item in sockets if isinstance(item, str))[len(plugs):]
        )]
    )

plugs = ['plugZ', None, 'plugY', 'plugX']
sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
cables = ['cable2', 'cable1', False]
    
if __name__ == "__main__":
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
