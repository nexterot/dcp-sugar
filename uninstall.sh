if [ $(whoami) == "root" ]; then
    if [ $0 == "uninstall.sh" ]; then
      rm -rf /usr/bin/dcp
      for user in $(ls /home)
      do
        ./uninstall.py /home/$user/.bashrc "alias dcp=/usr/bin/dcp/dcp.py"
        source /home/$user/.bashrc
      done
    else
      echo "cd to the dcp-sugar folder!"
    fi
else
  echo "use sudo"
fi
