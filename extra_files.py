from os import path, walk


def insert_extra_files():
    extra_dirs = ['app/templates', 'app/static','app/data']
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)

    return extra_files