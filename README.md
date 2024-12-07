# **AutoGitPy**  

**AutoGitPy** is a Python library designed to automate repetitive Git operations such as cloning repositories, pushing and pulling changes, and deleting folders. This utility eliminates the need for manual typing of the same commands, saving time and improving workflow efficiency.  

---

## **Features**  
1. **Automated Cloning of Repositories**  
   Clone repositories effortlessly into a specified folder.  
2. **Automated Push and Pull Operations**  
   Synchronize changes with remote repositories, including adding, committing, and pushing files.  
3. **Automated Deletion of Folders and Subfolders**  
   Remove unwanted folders and push the changes to the repository automatically.  
4. **Display Utility**  
   Display key details such as disk, path, and commit messages.  

---

## **Installation**  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/yourusername/AutoGitPy.git  
   cd AutoGitPy  
   ```  

2. Import the library in your Python project:  
   ```python  
   from AutogitPy import AutoGitUtils  
   ```  

---

## **Usage**  

### **1. Clone a Repository**  
Clone a repository into a specific path.  
```python  
AutoGitUtils.clone(disk="D", path="D:/folders", gitlink="https://github.com/example/repo.git")  
```  

### **2. Push and Pull Changes**  
Automatically pull changes, add files, commit with a message, and push to the repository.  
```python  
AutoGitUtils.push_pull(disk="D", path="D:/folders", msg="Updated files")  
```  

### **3. Delete Folders and Subfolders**  
Remove a folder and its contents from the repository and push the changes.  
```python  
AutoGitUtils.del_folder_subfol(disk="D", path="D:/folders", folder="obsolete_folder", msg="Removed obsolete folder")  
```  

### **4. Display Information**  
Print the disk, path, and commit message.  
```python  
AutoGitUtils.display(disk="D", path="D:/folders", msg="Sample commit message")  
```  

---

## **Example Workflow**  
```python  
from AutogitPy import AutoGitUtils  

# Clone a repository  
AutoGitUtils.clone(disk="D", path="D:/projects", gitlink="https://github.com/example/repo.git")  

# Push and pull changes  
AutoGitUtils.push_pull(disk="D", path="D:/projects", msg="Added new features")  

# Delete a folder and commit the changes  
AutoGitUtils.del_folder_subfol(disk="D", path="D:/projects", folder="old_folder", msg="Removed old_folder")  
```  

---

## **Advantages**  
- Simplifies repetitive Git operations.  
- Saves time by automating commonly used commands.  
- Improves workflow efficiency for developers.  

---

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  

---

**Happy Coding with AutoGitPy! 🚀**  
