#!/bin/bash
#do not forget to put this script name in the .gitignore directory in order to not 'push' it  !! -> you can execute this commands:
# echo createFile.sh >>.gitignore
echo 'Type the file name'
read file_name
touch $file_name ; chmod u+x $file_name ;echo -e "#!/bin/bash\n" > $file_name ; vim $file_name
#vim $file_name
