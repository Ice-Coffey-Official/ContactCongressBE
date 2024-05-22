bill_phone_template = """
Hello, my name is {username}, and I am a constituent of {title} {name} from {state}. I am calling today to express my {support} to {issue}, which is currently under consideration.

{description}

I believe that this is very important, and I urge {title} {name} to take a stance that aligns with the best interests of our community.

As your constituent, I value your representation and hope that you will consider my perspective when making your decision on this important matter.

Thank you for your time and attention to this issue.
"""


general_issue_phone_template = """
Hello, my name is {username}, and I am a constituent of {title} {name} from {state}. I am calling today to urge {title} {name} to take {support} {issue}, as this is of great concern to me and many others in our community.

{description}

I believe that this is very important, and I hope that {title} {name} will use their influence to advocate for positive change on this matter.

As your constituent, I value your representation and trust that you will give due attention to this urgent issue. Your leadership in addressing this would be greatly appreciated and remembered come election time.

Thank you for your time and attention to this matter. I look forward to hearing about any actions you plan to take.
"""


navigate_services_phone_template = """
Hello, my name is {username}, and I am a constituent of {title} {name} from {state}. I am calling today to seek assistance with a matter related to services that I have been experiencing difficulty navigating in regards to {issue}.

{description}

I believe that your office may be able to provide valuable assistance in resolving this matter, and I would greatly appreciate any support you can offer.

Please let me know the best way to proceed or if there are any additional documents or information I should provide to facilitate the process.

Thank you for your attention to this matter. I look forward to hearing from you.
"""


events_town_halls_phone_template = """
Hello, my name is {username}, and I am a constituent of {title} {name} from {state}. I am calling today to inquire about your upcoming {issue} that I recently learned about.

{description}

I am interested in attending/participating in the event and would like to know more details about the agenda, speakers, and how constituents can participate.

Could you please provide me with more information about the event, including any relevant registration or RSVP details?

Thank you for your time. I appreciate any assistance you can provide, and I look forward to the event.
"""


general_feedback_phone_template = """
Hello, my name is {username}, and I am a constituent of {title} {name} from {state}. I am calling today to share some general feedback and express a few concerns that I have regarding {issue}.

{description}

I believe it's important for elected officials to be aware of the concerns and opinions of their constituents, and I wanted to take this opportunity to share my perspective with you.

I would appreciate it if you could address these concerns or provide information on any actions that are being taken to address them.

Thank you for your attention to this matter. I appreciate any assistance you can provide, and I look forward to your response.
"""

phone_template_dict = {
    "bill":bill_phone_template,
    "issue":general_issue_phone_template,
    "service":navigate_services_phone_template,
    "event":events_town_halls_phone_template,
    "general":general_feedback_phone_template
}