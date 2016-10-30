a=$(whoami)
if [ $a == "root" ]; then
  mkdir /usr/bin/dcp
  cp -R $(pwd)/. /usr/bin/dcp/
  chmod 555 /usr/bin/dcp/dcp.py
  b="alias dcp=/usr/bin/dcp/dcp.py"
  for user in $(ls /home)
  do
    echo $b>>/home/$user/.bashrc
  done
else
  echo "use sudo"
fi
