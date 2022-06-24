
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": "Jackson",
            "Age": 33,
            "lucky_numbers": [7,13,22]},
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": "Jackson",
            "Age": 30,
            "lucky_numbers": [8,14,24]},
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": "Jackson",
            "Age": 98,
            "lucky_numbers": [9,14,44]}
                                        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member in self._members:
                if member['id'] == id:
                    break
        self._members.remove(member)

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
