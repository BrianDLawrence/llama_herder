"""Test Data"""
from langchain.prompts import PromptTemplate

MOCKCALENDARDATA1 = """
    EVENT: DAILY SCRUM
    DATE: JAN 10, 2024
    TIME: 9:00 AM to 9:30 AM (CET)
    LOCATION: TEAMS
    DESCRIPTION: Daily standup meeting for dev team
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), Organizer, Team Members

    EVENT: BACKLOG REVIEW 
    DATE: JAN 10, 2024
    TIME: 11:00 AM to 12:30 PM (CET)
    LOCATION: TEAMS
    DESCRIPTION: Review and prioritize backlog items for Q1
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), Organizer, Product Owner, Tech Lead

    EVENT: 1x1 Manager
    DATE: JAN 10, 2024
    TIME: 2:00 PM to 2:30 PM (CET)
    LOCATION: Office 2
    DESCRIPTION: Weekly 1x1 with manager
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), Manager

    EVENT: Client Exploration Call 
    DATE: JAN 10, 2024
    TIME: 4:00 PM to 4:30 PM (CET)
    LOCATION: TEAMS
    DESCRIPTION: Exploration call with Client X
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), Client Rep
"""

MOCKCALENDARDATA2 = """
    EVENT: DAILY SCRUM
    DATE: JAN 11, 2024
    TIME: 9:00 AM to 9:30 AM (CET)
    LOCATION: TEAMS
    DESCRIPTION: Daily standup meeting for dev team
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), Organizer, Team Members

    EVENT: FEEDBACK DISCUSSION
    DATE: JAN 11, 2024
    TIME: 11:30 AM to 12:00 PM (CET)
    LOCATION: TEAMS
    DESCRIPTION: Feedback for John Doe
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), John's manager

    EVENT: Client Escalation Review Meeting
    DATE: JAN 11, 2024
    TIME: 5:00 PM to 6:00 PM (CET)
    LOCATION: TEAMS
    DESCRIPTION: Review of current hot client escalations
    ATTENDEES: Brian Lawrence (Brian@SperoAutem.com), Customer Service Rep
"""

MOCKTODOLIST1 = """
    ITEM: Review client information
    DESCRIPTION: Review client information in prep for exploration meeting
    PRIORITY: P1
    PROJECT: WORK
    DUE DATE: JAN 10, 2024

    ITEM: Prep 1x1
    DESCRIPTION: Review concerns and put in list to discuss with mgr
    PRIORITY: P1
    PROJECT: WORK
    DUE DATE: JAN 10, 2024

    ITEM: Backlog Item Progress
    DESCRIPTION: Make progress on backlog item 1
    PRIORITY: P1
    PROJECT: WORK
    DUE DATE: JAN 10, 2024

    ITEM: Call friend
    DESCRIPTION: Call John to say hello 
    PRIORITY: P2
    PROJECT: LIFE
    DUE DATE: JAN 10, 2024
"""


MOCKTODOLIST2 = """
    ITEM: Review client escalations
    DESCRIPTION: Review all current client escalations and prioritize in prep for Client Escalation Review meeting
    PRIORITY: P1
    PROJECT: WORK
    DUE DATE: JAN 11, 2024

    ITEM: Prep Feedback
    DESCRIPTION: Make sure my list of John's feedback is ready for discussion
    PRIORITY: P1
    PROJECT: WORK
    DUE DATE: JAN 11, 2024

    ITEM: Read book
    DESCRIPTION: Make progress reading that book
    PRIORITY: P2
    PROJECT: LIFE
    DUE DATE: JAN 11, 2024

    ITEM: Progress with Python agent
    DESCRIPTION: Make progress with the python agent, finish scheduling input
    PRIORITY: P3
    PROJECT: FUN
    DUE DATE: JAN 11, 2024
"""

MOCKGOAL1 = """
    GOAL: I want an optimized schedule that includes Meetings and TODOs. 
    Each item should be either a TODO or meeting. 
    It is important to understand that any meetings you get, can not be changed 
    I want the TODOs to be appropriately placed. Each TODO should be analyzed
    to determine when it should be complete based on priority P1 being the highest with P2,3 .etc being lower
    Also look at the description and determine based on the description if the TODO should be done before 
    a meeting based on the context. 
    The schedule should be return in JSON format. 
"""

TESTPROMPT = PromptTemplate(
        input_variables=["topic"],
        template ="You are happy chatbot : {topic} ")
