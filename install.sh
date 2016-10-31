if [ $(whoami) == "root" ]; then
  if [ $0 == "install.sh" ]; then
    mkdir /usr/bin/dcp
    cp -R $(pwd)/. /usr/bin/dcp/
    chmod 555 /usr/bin/dcp/dcp.py
    for user in $(ls /home)
    do
      echo "alias dcp=/usr/bin/dcp/dcp.py">>/home/$user/.bashrc
      source /home/$user/.bashrc
    done
  else
    echo "cd to the dcp-sugar folder!"
  fi
else
  echo "use sudo"
fi
