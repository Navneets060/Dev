        #!/bin/bash
        DBS=`mysql -uroot -p -e"show databases;"`
        for b in $DBS ;
        do
                mysql -uroot -p -e"show tables from $b"
        done