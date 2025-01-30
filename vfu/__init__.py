import os
from subprocess import check_output, STDOUT


class vutil32:
    def __init__(self, path):
        if not path:
            raise Exception("[vfu] missing path")
        if not os.path.isfile(path):
            raise Exception("[vfu] no file found with path")
        if not os.path.isabs(path):
            raise Exception("[vfu] path must be absolute")
        self.path = path

        # check if can access program
        out = check_output([self.path, "-version"], shell=False, stderr=STDOUT)
        if b"Micro Focus extend file utility version 9.2.5" not in out:
            raise Exception("[vfu] unexpected version")

    def unload(self, src, dst, debug=False):
        if not os.path.isfile(src):
            raise Exception("[vfu] invalid src")
        if not os.path.isabs(src):
            raise Exception("[vfu] src must be an absolute path")
        if not os.path.isabs(dst):
            raise Exception("[vfu] dst must be an absolute path")

        out = check_output(
            [self.path, "-unload", "-t", src, dst], shell=False, stderr=STDOUT
        )

        if b"encrypted, unload not allowed" in out:
            raise Exception("[vfu] encrypted, unload not allowed")

        return dst
