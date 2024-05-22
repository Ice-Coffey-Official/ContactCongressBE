import contentGen
from util import *
from emailTemplates.generalEmail import congress_bill_email_template, general_action_email_template, general_feedback_email_template, navigate_services_email_template, events_town_halls_email_template, email_template_dict
from phoneTemplates.generalPhone import bill_phone_template, general_issue_phone_template, general_feedback_phone_template, events_town_halls_phone_template,navigate_services_phone_template, phone_template_dict

def test_generate_email_bill():
    generator = contentGen.ContentGenerator()
    assert generator.generateEmail(
        "bill",
        "placeholder 1",
        "placeholder 2",
        "placeholder 3",
        "placeholder 4",
        "placeholder 5",
        "placeholder 6"
    ) == '''Subject: Urgent Action Needed on {issue}

Dear {title} {name},

I am writing to urge you to {support} {issue}, which is currently under consideration. This bill is of great importance to me and many others in our community, and I believe it will have significant impacts on us.

{description}

As your constituent, I trust that you will carefully consider the implications of this bill and make the decision that aligns with the best interests of our community. Your {support} to this legislation would be greatly appreciated and remembered come election time.

Thank you for your attention to this matter. I look forward to hearing your stance on {issue}.

Sincerely,
{userInfo}'''.format(
    issue="placeholder 1",
    title="placeholder 2",
    name="placeholder 3",
    support="placeholder 4",
    description="placeholder 5",
    userInfo="placeholder 6"
)

def test_generate_phone_call_bill():
    generator = contentGen.ContentGenerator()
    generator.generatePhone(
        "bill",
        "placeholder 1",
        "placeholder 2",
        "placeholder 3",
        "placeholder 4",
        "placeholder 5",
        "placeholder 6",
        "placeholder 7"
    ) == """
Hello, my name is {username}, and I am a constituent of {title} {name} from {state}. I am calling today to express my {support} to {issue}, which is currently under consideration.

{description}

I believe that this is very important, and I urge {title} {name} to take a stance that aligns with the best interests of our community.

As your constituent, I value your representation and hope that you will consider my perspective when making your decision on this important matter.

Thank you for your time and attention to this issue.
""".format(
    username="placeholder 1",
    title="placeholder 2",
    name="placeholder 3",
    state="placeholder 4",
    support="placeholder 5",
    issue="placeholder 6",
    description="placeholder 7"
)