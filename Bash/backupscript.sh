            #!/bin/bash  -x        
            SRCD="/c/cygwin64/nav"
            TGTD="/c/cygwin64/nav/backups"
            OF=home-$(date +%Y%m%d).tgz
            tar -cZf $TGTD$OF $SRCD