class BugFreeBug:
    """定义一个bug信息类"""

    bug_id = ""  # bug id
    title = ""  # bug名称
    href = ""  # bug链接
    status = ""  # bug状态
    severity = ""  # bug严重程度
    priority = ""  # bug优先级
    created_by = ""  # bug创建者
    created_at = ""  # bug创建时间
    solution = ""  # bug解决方案
    updated_at = ""  # 更新修改时间
    list_comments = []  # bug注释
    list_files = []  # bug附件

    def __init__(self, bug_id, title, href, status, severity, priority, created_by,
                 created_at, solution, comments, list_files, updated_at):
        """初始化"""
        self.bug_id = bug_id
        self.title = title
        self.href = href
        self.status = status
        self.severity = severity
        self.priority = priority
        self.created_by = created_by
        self.created_at = created_at
        self.solution = solution
        self.updated_at = updated_at
        self.list_comments = comments
        self.list_files = list_files

    def bug_info(self):
        """打印bug信息"""
        print("-----------------------------------------")
        print("bug_id:" + self.bug_id)
        print("title:" + self.title)
        print("href:" + self.href)
        print("status:" + self.status)
        print("severity:" + self.severity)
        print("priority:" + self.priority)
        print("created_by:" + self.created_by)
        print("created_at:" + self.created_at)
        print("solution:" + self.solution)
        print("list_comments:" + "[" + ",".join(self.list_comments) + "]")
        print("list_files:" + "[" + ",".join(self.list_files) + "]")
        print("-----------------------------------------")
