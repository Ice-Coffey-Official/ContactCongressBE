from emailTemplates.generalEmail import *
from phoneTemplates.generalPhone import *

class ContentGenerator:

    def __init__(self):
        pass

    def generateEmail(self, type, issue, title, name, support, description, userInfo):
        return email_template_dict[type].format(
            issue=issue,
            title=title,
            name=name,
            support=support,
            description=description,
            userInfo=userInfo
        )

    def generatePhone(self, type, username, title, name, state, support, issue, description):
        return phone_template_dict[type].format(
            username=username,
            title=title,
            name=name,
            state=state,
            support=support,
            issue=issue,
            description=description
        )