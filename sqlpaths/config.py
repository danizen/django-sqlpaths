import attr


@attr.s(frozen=True)
class PathsConfig():
    DBSHELL = attr.ib(kw_only=True, default=False)
    INCLUDE = attr.ib(kw_only=True, default=['*.sql'])
    ROOT = attr.ib(kw_only=True, default=None)
    ALWAYS = attr.ib(kw_only=True, default=[])

    def __attrs_post_init__(self):
    	if not self.ROOT:
    		self.ROOT = os.path.join(settings.BASE_DIR, 'sql')

