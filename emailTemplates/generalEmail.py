congress_bill_email_template = '''
Subject: Urgent Action Needed on {issue}

Dear {title} {name},

I am writing to urge you to {support} {issue}, which is currently under consideration. This bill is of great importance to me and many others in our community, and I believe it will have significant impacts on us.

{description}

As your constituent, I trust that you will carefully consider the implications of this bill and make the decision that aligns with the best interests of our community. Your {support} to this legislation would be greatly appreciated and remembered come election time.

Thank you for your attention to this matter. I look forward to hearing your stance on {issue}.

Sincerely,
{userInfo}'''


general_action_email_template = """
Subject: Urgent Action Needed on {issue}

Dear {title} {name},

I am writing to urge you to {support} {issue}. This is of great concern to me and many others in our community. I am not aware of any specific bill on this matter currently under consideration, and I believe it is imperative that steps are taken to address this issue promptly.

{description}

As your constituent, I trust that you will give due attention to this matter and use your influence to advocate for positive change. Your leadership in addressing this would be greatly appreciated and remembered come election time.

Thank you for your attention to this urgent matter. I look forward to hearing about any actions you plan to take.

Sincerely,
{userInfo}
"""

navigate_services_email_template = """
Subject: Assistance Needed with Constituent Services

Dear {title} {name},

I hope this email finds you well. I am writing to seek assistance with a matter related to services that I have been experiencing difficulty navigating in regards to {issue}.

{description}

I believe that your office may be able to provide valuable assistance in resolving this matter, and I would greatly appreciate any support you can offer. If possible, I would like to schedule a meeting or phone call to discuss this issue further and explore potential solutions.

Please let me know the best way to proceed or if there are any additional documents or information I should provide to facilitate the process.

Thank you for your attention to this matter. I look forward to hearing from you soon.

Sincerely,
{userInfo}
"""


events_town_halls_email_template = """
Subject: Inquiry Regarding {issue}

Dear {title} {name},

I hope this email finds you well. I am writing to inquire about the upcoming {issue} that I recently learned about.

{description}

I am interested in attending/participating in {issue} and would like to know more details about the agenda, speakers, and how constituents can participate.

Could you please provide me with more information about the event, including any relevant registration or RSVP details?

Thank you for your attention to this matter. I look forward to your response and hope to have the opportunity to engage with you and other constituents.

Sincerely,
{userInfo}
"""


general_feedback_email_template = """
Subject: General Feedback and Concerns

Dear {title} {name},

I hope this email finds you well. I am writing to share some general feedback and express a few concerns that I have regarding {issue}.

{description}

I believe it's important for elected officials to be aware of the concerns and opinions of their constituents, and I wanted to take this opportunity to share my perspective with you.

I would appreciate it if you could address these concerns or provide information on any actions that are being taken to address them.

Thank you for your attention to this matter. I look forward to hearing from you and hope that we can work together to address the issues facing our community.

Sincerely,
{userInfo}
"""

email_template_dict = {
    "bill":congress_bill_email_template,
    "issue":general_action_email_template,
    "service":navigate_services_email_template,
    "event":events_town_halls_email_template,
    "general":general_feedback_email_template
}