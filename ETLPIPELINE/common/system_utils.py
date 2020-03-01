import subprocess
import os
import uuid


def execute_local(args):
    print('running command : %s' %(''.join(args)))
    process = subprocess.Popen(args=args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()
    print('stdout: {}'.format(output))

# subprocess.PIPE opens a new PIPE for file handler. Otherwise it inherits the file handler from parent.
# process.communicate() prints/capture entire data at once. Use 'process.stdout()' for file/iterative process.


def del_local_file(list_of_file):
    for file in list_of_file:
        print('removing local file %s' %file)
        os.remove(file)


def read_file(path):
    content = open(path,'r')
    return content.read()


# Create random uuid generator
def generate_uuid():
    return str(uuid.uuid1())


