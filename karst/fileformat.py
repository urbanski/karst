from survey import Station, Shot
import re

class CompassDATFile():
    handle = None

    def __init__(self, file_handle):
        self.handle = file_handle

    def read(self):
        data = self.handle.read()
        survey_tuple = data.split("\x0d\x0a\x0c\x0d\x0a")
        for raw_survey in survey_tuple:
            self._parse_raw_survey(raw_survey)

    def _parse_survey_shot(self, raw):
        reg = re.match("\s*([A-Za-z0-9]+)\s*([A-Za-z0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)\s*([\-\.0-9]+)", raw)
        if reg != None:
            new_shot = Shot(reg.group(1), reg.group(2), reg.group(3), reg.group(4), reg.group(5))
            return new_shot

    def _parse_raw_survey(self, raw):
        lines = raw.split("\n")
        survey_dict = {'name': lines[1], 'date': lines[2], 'team': lines[4]}
        if len(lines) > 3:
            print survey_dict
            data_header = lines[7]

            for line in lines[9:]:
                #print "SHOT: %s" % line
                shot =  self._parse_survey_shot(line)
                print "%s -> %s" % (shot.station_from, shot.station_to)
