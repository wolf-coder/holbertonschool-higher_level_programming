#!/bin/bash
echo 'Type the file name'
read file_name
touch $file_name ; echo -e "#include <stdio.h>\nint main(void)\n{\n\treturn (0);\n}" > $file_name ;subl $file_name
#vim $file_name
