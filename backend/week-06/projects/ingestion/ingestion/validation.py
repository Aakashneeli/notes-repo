"""Learner: validate the filename, declared type, bounded bytes and UTF-8 text.
Raise UploadProblem with status 400/413/415 as specified in README.
"""
class UploadProblem(Exception):
    def __init__(self, status, code):
        self.status, self.code = status, code
        super().__init__(code)
async def read_validated(upload, max_bytes):
    raise NotImplementedError("Return bytes after checks; close UploadFile in finally")
