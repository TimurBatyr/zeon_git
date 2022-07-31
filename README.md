# Zeon Git is analog of git
- with features:
  - add files
  - delete files
  - list files
  - backup file
  - restore file
  - create snapshots


- Commands:

  - fs --> returns where the command was called
  - fs init --> creates directories ".zeon_git/objects", ".zeon_git/index.txt", and "hookies"
  - fs add file_name(text.txt) --> adds file_name to directory ".zeon_git"
  - fs del file_name(text.txt) --> deletes file_name to directory ".zeon_git"
  - fs backup --> create backup of directory ".zeon_git"
  - fs restore --> restores backed file, which is zip file, to ".zeon_git"
 
- commands for snapshots:
  - fs snapshot create file_name(zeon_1.zip) --> creates snapshot(zeon_1.zip) in directory "snapshot"
  - fs snapshot del file_name(zeon_1.zip) --> deletes snapshot(zeon_1.zip) from directory "snapshot"
  - fs snapshot list --> lists file inside directory "snapshot"
  - fs snapshot restore file_name(zeon_1.zip) --> restores file_name(zeon_1.zip) from directory "snapshot" to directory ".zeon_git"
  - fs snapshot checkout file_name(zeon_1.zip) --> derives file_name(zeon_1.zip) from directpry "snapshot" and puts into a temporary directory "temp_dir"
    in order replace the current file in objects
  - fs snapshot commit file_name1(dir/dir/test.txt) file_name2(rest.txt) --> replaces "file_name1" with "file_name2"
  
  
