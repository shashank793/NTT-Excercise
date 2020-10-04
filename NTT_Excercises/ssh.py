from paramiko import SSHClient
ssh = SSHClient()
ssh.load_system_host_keys()
user = input()
host = input()
ssh.connect('{0}@{1}'.format(user,host))
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
print(ssh_stdout)