import paramiko


def execute_remote(key_path, instance_ip, username, cmd_arr):
    key = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # connect/ssh to the remote m/c.
        client.connect(hostname=instance_ip, username=username, pkey=key)

        #Execute the command on remote m/c.

        str_cmd = ' '.join(cmd_arr)
        print('Executing below command on %s on remote machine %s \n %s' %(instance_ip,str_cmd))
        stdin,stdout,stderr = client.exec_command(str_cmd) #returns a tuple
        print(stdout.read())

        #close the connection after the command is executed on remote m/c
        client.close()

    except Exception as e:
        print(e)