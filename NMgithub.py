import git 
import os 
import shutil

def push_latest():
    local_repo = "/home/netman/csci5180/poc_local_repository"
    repo_url = "git@github.com:sarang2403/poc.git"
    local_folder = "/home/netman/csci5180/poc"

    if not os.path.exists(local_repo):
        #Cloning is required for the first time. 
        repo = git.Repo.clone_from(repo_url, local_repo)
    else:
        #If local Repository is already cloned
        repo = git.Repo(local_repo)
        #We just need to pull so that the local and the remote repo have the exact same content. 
        repo.git.pull('origin', 'main')


    #This copies all files from local storage to local repository - regardless if they are same or not. 
    #shutil.copy(image, os.path.join(local_repo, image))
    #shutil.copy(file, os.path.join(local_repo, file))

    for item in os.listdir(local_folder):
        s = os.path.join(local_folder, item)
        d = os.path.join(local_repo, item)

        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s,d)


    repo.git.add(A=True) #This adds everything not tracked yet. 
    repo.index.commit("Updating the file") 
    origin = repo.remotes.origin 
    origin.push('main') #Push to Main
    print("Pushed latest changes to remote repository")

def main():
    push_latest()

if __name__ == "__main__":
    main()








