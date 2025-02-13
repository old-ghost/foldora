def del_all(path):
    for sub in path.iterdir():
        if sub.is_dir():
            del_all(sub)
        if sub.is_file():
            sub.unlink()
    path.rmdir()
