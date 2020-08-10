import os



"""os.system(f'cmd /k "d: && cd datascience_git\Assignments\{ip_folder} && git pull  && git add . && git commit -m "AUTOMATE FILES" && git push "')"""
class AutoGitUtils():
    """def __init__(self,gitlink,msg,folder,disk,path):
        self.gitlink=input('enter')
        self.msg=input('enter')
        self.folder=input('enter')
        self.disk=input('enter')
        self.path=input('enter')"""
        
    def display(path,msg,disk):
        print(path,msg,disk)

  
         
        
    def clone(self):
        os.system(f'cmd /k "{self.disk}: && cd {self.path} && git clone {self.gitlink} && git status "')


    def push_pull(self):
        os.system(f'cmd /k " {self.disk}: && cd {self.path} && git pull  && git add . && git commit -m """{self.msg}""" && git push origin master && git status"')



    def del_folder_subfol(self):
        os.system(f'cmd /k " {self.disk}: && cd {self.path} &&git rm -r {self.folder} && git commit -m "{self.msg}" && git push origin master && git status"')
