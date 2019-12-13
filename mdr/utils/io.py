from datetime import datetime
from io import StringIO
import csv


class FileWriter:
    def __init__(self, name, encoding='utf-8', buffering=-1):
        self.name = name
        self.enc = encoding
        self.buf = buffering

        self.formatting = '%Y-%m-%d_%H-%M-%S.%f'
        self.current_dt = datetime.now().strftime(self.formatting)
        self.full_name = f'{self.name}_{self.current_dt}.mcs'
        self.current_file = open(self.full_name, 'wb', buffering=self.buf)

    def __del__(self):
        self.current_file.close()

    def write(self, *data, delim='\t', newline='\n'):
        data = [str(d) for d in data]
        data = delim.join(data)
        self.current_file.write(data.encode(encoding=self.enc))
        self.current_file.write(str(newline).encode(encoding=self.enc))

    def reset(self, name=None):
        if name is not None:
            self.name = name
        if not self.current_file.closed:
            self.current_file.close()
        self.current_dt = datetime.now().strftime(self.formatting)
        self.full_name = f'{self.name}_{self.current_dt}.mcs'
        self.current_file = open(self.full_name, 'wb', buffering=self.buf)

    def close(self):
        self.current_file.close()

    def get_current_name(self):
        return self.full_name


def serialize(data: dict) -> str:
    buf = StringIO()
    if 'header' not in data.keys() or 'data' not in data.keys():
        raise KeyError('Data dictionary is incorrect')
    buf.write('#>#>#>' + '<:>'.join([str(e) for e in data['header']]) + '#>#>#>' + '\n')
    writer = csv.writer(buf, dialect='unix')
    for e in data['data']:
        writer.writerow(e)
    buf.seek(0)
    return buf.read()


def deserialize(data: str) -> dict:
    parts = [e for e in data.split('#>#>#>') if e != '']
    header = [e.strip() for e in parts[0].split('<:>')]
    data_str = parts[1].strip()
    reader = csv.reader(StringIO(data_str), dialect='unix')
    arr = []
    for e in reader:
        arr.append([float(i) for i in e])
    return {
        'header': header,
        'data': arr
    }


def add_dt_str(name: str) -> str:
    formatting = '%Y-%m-%d_%H-%M-%S.%f'
    current_dt = datetime.now().strftime(formatting)
    full_name = f'{name}_{current_dt}.mcs'
    return full_name
