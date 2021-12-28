'''
@author: Shivam Mishra
@date: 27-12-21 8:29 PM
'''


class QuatityCustomException(Exception):

    def __init__(self,message):
        self.message = message

    def __str__(self):
        return self.message