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
        nvim ~/Documentos/.Scripts/comandos.sh
    }

    analisis_datos(){
        cd ~/Documentos/.Eduardo/GH/analisis-datos/
    }

    # Miniconda ---------------------------------------------------
    base(){
        conda activate base
    }

    deactivate(){
        conda deactivate
    }

    conda_list(){
        echo -e "\nnumpy, pandas, statsmodels, scipy, seaborn, matplotlib"
        echo -e "TKinter, pymysql, pymongo, fastapi.\n"
    }

    # Herramientas de Análisis de datos --------------------------
    refine(){
        ~/openrefine-3.8.2/./refine
    }

    weka(){
        ~/weka-3-8-6/./weka.sh
    }

    magrada(){
        java -jar ~/Magrada/Magrada.jar
    }

    tabula(){
        java -jar ~/tabula/tabula.jar
    }
 
    # MySQL ------------------------------------------------------
    mysql_status(){
        sudo systemctl status mysql
    }

    mysql_stop(){
        sudo systemctl disable mysql
        sudo systemctl stop mysql
    }

    mysql_start(){
        sudo systemctl start mysql
    }

    mysql_restart(){
        sudo systemctl restart mysql
    }

    mongo_status(){
        sudo systemctl status mongod
    }

    mysql_on(){
        mysql_start
        mysql -u root -p
    }

    # MongoDB ----------------------------------------------------
    mongo_stop(){
        sudo systemctl disable mongod
        sudo systemctl stop mongod        
    }

    mongo_start(){
        sudo systemctl start mongod
    }

    mongo_restart(){
        sudo systemctl restart mongod
    }

    mongo_on(){
        mongosh
    }
fi
