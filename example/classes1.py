### "imports"
from classes import Data

### "other-imports"
import StringIO # Can't use io.StringIO, csv lib does not support unicode
import csv
import json

### "csv-subclass"
class Csv(Data):
    """
    CSV type.
    """
    aliases = ['csv']

    def present(self):
        s = StringIO.StringIO()
        writer = csv.DictWriter(s, self.data[0].keys())

        writer.writeheader()
        writer.writerows(self.data)
        
        return s.getvalue()

### "json-subclass"
class Json(Data):
    """
    JSON type.
    """
    aliases = ['json']

    def present(self):
        return json.dumps(self.data) 

