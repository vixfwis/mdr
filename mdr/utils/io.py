from datetime import datetime


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


def parse_file_data(data):  # TODO: make serialization and v.v. class and subclass read and write
    arr = []
    for line in data.split('\n'):
        if line == '' or line[0] == '#':
            continue
        points = line.split('\t')
        arr.append((float(points[0]), float(points[1])))
    return arr
