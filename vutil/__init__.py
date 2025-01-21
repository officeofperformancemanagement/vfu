from subprocess import check_output

class VUTIL:
    def __init__(self, path):
        if not path:
            raise Exception("[vutil-py] missing path")
        if not os.path.isfile(path):
            raise Exception("[vutil-py] no file found with path")
        if not os.path.isabs(path):
            raise Exception("[vutil-py] path must be absolute")
        self.path = path

    def unload(self, src, dst):
        if not os.path.isfile(src):
            raise Exception("[vutil-py] invalid src")
        if not os.path.isabs(src):
            raise Exception("[vutil-py] src must be an absolute path")
        if not os.path.isabs(dst):
            raise Exception("[vutil-py] dst must be an absolute path")
        check_output([self.path, "-unload", "-t", src, dst], shell=False)
        return dst
