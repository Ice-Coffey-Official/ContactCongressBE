class Profile:
    def __init__(self, name, state, party, birthday, entered, address, number, email, website, twitter, branch):
        self.name = name
        self.state = state
        self.party = party
        self.birthday = birthday
        self.entered = entered
        self.address = address
        self.number = number
        self.email = email
        self.website = website
        self.twitter = twitter
        self.branch = branch

    def __repr__(self):
        return str({
            "Name" : self.name,
            "State" : self.state,
            "Party" : self.party,
            "Birthday" : self.birthday,
            "Entered Office" : self.entered,
            "Address" : self.address,
            "Phone Number" : self.number,
            "Email Address" : self.email,
            "Website" : self.website,
            "Twitter" : self.twitter,
            "Branch" : self.branch
        })
    
    def as_dict(self):
        return {
            "Name" : self.name,
            "State" : self.state,
            "Party" : self.party,
            "Birthday" : self.birthday,
            "Entered Office" : self.entered,
            "Address" : self.address,
            "Phone Number" : self.number,
            "Email Address" : self.email,
            "Website" : self.website,
            "Twitter" : self.twitter,
            "Branch" : self.branch
        }