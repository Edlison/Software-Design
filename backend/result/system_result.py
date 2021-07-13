# @Author  : Edlison
# @Date    : 7/12/21 17:19


class SystemResult:
    def __init__(self):
        self.status = None
        self.msg = None
        self.data = None

    def ok(self, msg='success'):
        self.status = 0
        self.msg = msg
        return self

    def error(self, msg='error'):
        self.status = 1
        self.msg = msg
        return self

    def is_ok(self):
        if self.status is None or self.status != 0:
            return False
        else:
            return True

    def set_data(self, data):
        self.data = data

    def keys(self):
        return ['status', 'msg', 'data']

    def __getitem__(self, item):
        return getattr(self, item)
