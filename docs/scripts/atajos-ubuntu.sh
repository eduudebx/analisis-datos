#!/bin/bash

if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then 
   
    # Terminal ----------------------------------------------------

    cls(){
        clear
    }

    src(){
        source ~/.bashrc
    }

    atajos(){
        nvim ~/Zbodhix/.Scripts/comandos.sh
    }

    analisis_datos(){
        cd ~/Zbodhix/GH/analisis-datos/
    }

    linux_base(){
	lsb_release -a
    }

    ayuda(){
        echo -e "\ncls, src, linux_base, atajos, analisis_datos"
        echo -e "base, conda_list, deactivate"
        echo -e "gsavec, gadd, glist, gpush, gpull"
        echo -e "docker_*, mongodb_*, mysql_*, postgres_*\n"           
    }

    # Miniconda ---------------------------------------------------
    base(){
        conda activate ista
    }

    deactivate(){
        conda deactivate
    }

    conda_list(){
        echo -e "\nnumpy, pandas, matplotlib, seaborn"
        echo -e "\n"
    }

 
    # MySQL ------------------------------------------------------
    mysql_status(){
        sudo systemctl status mysql
    }

    mysql_stop(){
        sudo systemctl stop mysql
    }

    mysql_disable(){
        sudo systemctl disable mysql
    }

    mysql_start(){
        sudo systemctl start mysql
    }

    mysql_restart(){
        sudo systemctl restart mysql
    }

    mysql_root(){
        mysql -u root -p
    }

    # Postgresql ----------------------------------------------------
    postgres_status(){
        sudo systemctl status postgresql
    }

    postgres_stop(){
        sudo systemctl stop postgresql
    }

    postgres_disable(){
        sudo systemctl disable postgresql
    }

    postgres_start(){
        sudo systemctl start postgresql
    }

    postgres_restart(){
        sudo systemctl restart postgresql
    }

    # MongoDB ----------------------------------------------------
    mongodb_status(){
        sudo systemctl status mongod
    }

    mongodb_stop(){
        sudo systemctl stop mongod
    }

    mongodb_disable(){
        sudo systemctl disable mongod
    }

    mongodb_start(){
        sudo systemctl start mongod
    }

    mongodb_restart(){
        sudo systemctl restart mongod
    }


 # Docker ----------------------------------------------------
    docker_status(){
        sudo systemctl status docker
    }

    docker_stop(){
        sudo systemctl stop docker
    }

    docker_disable(){
        sudo systemctl disable docker
    }

    docker_start(){
        sudo systemctl start docker
    }

    docker_restart(){
        sudo systemctl restart docker
    }

    # Git ----------------------------------------------------

    gadd(){
        git add .
    }

    gsavec(){
        git config --global credential.helper store
    }

    glist(){
        git config --list
    }

    gpush(){
	git push
    }

    gpull(){
	git pull
    }
fi
