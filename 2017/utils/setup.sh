SHELL=/usr/bin/zsh
now=$((10#$(date +'%d')))
dir_name=Day_$now
echo $now
echo $dir_name
mkdir ../$dir_name
cp template.py ../$dir_name/$now.py
touch ../$dir_name/ex


