
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, initial_members=None):
        self._members = []
        self.last_name = 'Jackson'

        if initial_members:
            for member in initial_members:
                self.add_member(member)
        else:
            self.add_member({'first_name': 'John', 'age': 33,
                            'lucky_numbers': [7, 13, 22]})
            self.add_member({'first_name': 'Jane', 'age': 35,
                            'lucky_numbers': [10, 14, 3]})
            self.add_member(
                {'first_name': 'Jimmy', 'age': 5, 'lucky_numbers': [1]})

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)


    def add_member(self, member):        
        if not isinstance(member, dict):
            print("Member must be a dictionary.")
            return

        if 'id' not in member or member['id'] is None:
            member['id'] = self._generateId()

        required_keys = ['first_name', 'age', 'lucky_numbers']
        if not all(key in member for key in required_keys):
            print("Member dictionary is missing one or more required keys.")
            return

        member['last_name'] = self.last_name

        if not isinstance(member['first_name'], str) or \
        not isinstance(member['age'], int) or \
        not all(isinstance(x, int) for x in member['lucky_numbers']):
            print("Member dictionary has one or more incorrect types.")
            return

        if member['age'] <= 0:
            print("Age must be greater than 0.")
            return

        self._members.append(member)

    def delete_member(self, member_id):
        for index, member in enumerate(self._members):
            if member['id'] == member_id:
                del self._members[index]
                return True
        return False

    def get_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
