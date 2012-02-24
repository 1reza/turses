###############################################################################
#                               coding=utf-8                                  #
#                     Copyright (c) 2012 Alejandro Gómez.                     #
#       Licensed under the GPL License. See LICENSE.txt for full details.     #
###############################################################################

import sys
sys.path.append('../')
import unittest
from datetime import datetime

from twitter import Status

from turses.timeline import Timeline

class TimelineTest(unittest.TestCase):
    def setUp(self):
        self.timeline = Timeline()
        self.timeline.clear()
        self.assertEqual(len(self.timeline), 0)

    def _create_status_with_id_and_datetime(self, id, datetime):
        created_at = datetime.strftime('%a %b %d %H:%M:%S +0000 %Y')
        return Status(created_at=created_at, id=id,)

    def test_unique_statuses_in_timeline(self):
        self.assertEqual(len(self.timeline), 0)
        # create and add the status
        status = self._create_status_with_id_and_datetime(1, datetime.now())
        self.timeline.add_status(status)
        self.assertEqual(len(self.timeline), 1)
        # check that adding more than once does not duplicate element
        self.timeline.add_status(status)
        self.assertEqual(len(self.timeline), 1)

    def test_insert_different_statuses(self):
        old_status = self._create_status_with_id_and_datetime(1, 
                                                              datetime(1988, 12, 19))
        new_status = self._create_status_with_id_and_datetime(2, 
                                                              datetime.now())
        self.timeline.add_statuses([old_status, new_status])
        self.assertEqual(len(self.timeline), 2)

    def test_insert_different_statuses_individually(self):
        old_status = self._create_status_with_id_and_datetime(1, 
                                                              datetime(1988, 12, 19))
        new_status = self._create_status_with_id_and_datetime(2, 
                                                              datetime.now())
        self.timeline.add_status(old_status)
        self.assertEqual(len(self.timeline), 1)
        self.timeline.add_status(new_status)
        self.assertEqual(len(self.timeline), 2)

    def test_statuses_ordered_reversely_by_date(self):
        old_status = self._create_status_with_id_and_datetime(1, 
                                                              datetime(1988, 12, 19))
        new_status = self._create_status_with_id_and_datetime(2, 
                                                              datetime.now())
        self.timeline.add_statuses([old_status, new_status])
        self.assertEqual(self.timeline[0], new_status)
        self.assertEqual(self.timeline[1], old_status)
        

if __name__ == '__main__':
    unittest.main()
