from sh import tail
import re 

if __name__ == "__main__":
    
    # for each line of the file...
    for line in tail("-f", "monitor.log",_iter=True):
        #ssh_server = re.search("^sshd.", line)
        #if ssh_server:
        print (line)
        
