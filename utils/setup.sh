SHELL=/usr/bin/zsh
now=$(($(date +'%d')+1))
dir_name=Day_$now
echo $now
echo $dir_name
mkdir ../$dir_name
cp template.py ../$dir_name/$now.py
touch ../$dir_name/ex


