
class NoteSearchParams:
    def __init__(self, submittedAfter=None, submittedBefore=None, targetDate=None, targetUsers=None):
        self.submittedAfter = submittedAfter;
        self.submittedBefore = submittedBefore;
        self.targetDate = targetDate;
        self.targetUsers = targetUsers;
