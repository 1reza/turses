###############################################################################
#                               coding=utf-8                                  #
#           Copyright (c) 2012 Nicolas Paris and Alejandro Gómez.             #
#       Licensed under the GPL License. See LICENSE.txt for full details.     #
###############################################################################

from datetime import datetime


def datetime_from_status_date(date):
    """Converts a date on a Twitter status to a `datetime` object."""
    return datetime.strptime(date, '%a %b %d %H:%M:%S +0000 %Y') 


class Timeline(object):
    """List of Twitter statuses ordered reversely by date."""

    def __init__(self, statuses=[]):
        self._key = lambda status: datetime_from_status_date(status.created_at)
        if statuses:
            self.statuses = sorted(statuses,
                                   key=self._key,
                                   reverse=True)
        else:
            self.statuses = statuses

    def add_status(self, new_status):
        """
        Adds the given status to the status list of the Timeline if it's
        not already in it.
        """
        if new_status not in self.statuses:
            self.statuses.append(new_status)
            self.statuses.sort(key=self._key, reverse=True)

    def add_statuses(self, new_statuses):
        """
        Adds the given new statuses to the status list of the Timeline
        if they are not already in it.
        """
        for status in new_statuses:
            self.add_status(status)

    def clear(self):
        """Clears the Timeline."""
        self.statuses = []

    def __len__(self):
        return len(self.statuses)

    def __iter__(self):
        return self.statuses.__iter__()

    def __getitem__(self, i):
        return self.statuses[i]
