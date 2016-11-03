from berlinale import MRBerlinaleKBytes

import logging
logging.basicConfig(level=logging.INFO)


INPUT_FILE = 's3://alexcomu/berlinale_aggregated.csv'

mr_job = MRBerlinaleKBytes(args=['-v', '-r', 'emr', 
                                '--conf-path', 'mrjob.conf',
                                INPUT_FILE])

output = {}
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        key, value = mr_job.parse_output_line(line)
        output[key] = value

import json
print json.dumps(output)
