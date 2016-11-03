'''
$ berlinale1;1454331524;995823735;213.61.32.110;10;1580;0;wowza02;instance1;wowza_app;

$ app-name;timestamp;session-id;client-IP;seconds;kbytes;client-type;server-name;instance;stream-name;
'''

from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

class MRBerlinaleKBytes(MRJob):

    def mapper(self, _, line):
        (app_name, timestamp_start, session_id,
         client_ip, length_stream, kbyte_transf,
         client_type, server_name, wowza_instance, stream_name) = line.split(";")
        yield app_name, int(kbyte_transf)


    def reducer(self, app_name, kbytes):
        yield app_name, sum(kbytes)

if __name__ == '__main__':
    MRBerlinaleKBytes.run()