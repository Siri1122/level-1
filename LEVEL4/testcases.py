import pytest
from searchfordrive import searchfordrive
class Test_Drive:
    def test_DriveCase(self):
        obj=searchfordrive()
        self.expected=obj.find_drives()
        self.actual=['C','D']
        assert self.expected==self.actual