#!/bin/bash
#

### BEGIN INIT INFO
# Provides:          zend-server
# Required-Start:    $local_fs $remote_fs $network $syslog
# Required-Stop:     $local_fs $remote_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop ZendServer daemons
### END INIT INFO
# For RHEL:

# chkconfig: 345 95 05
# description: Zend Server control script. Used to control Zend Daemons and Apache.


if [ -f /etc/zce.rc ];then
    . /etc/zce.rc
else
    echo "/etc/zce.rc doesn't exist!"
    exit 1;
fi
if [ -f $ZCE_PREFIX/bin/shell_functions.rc ];then
    . $ZCE_PREFIX/bin/shell_functions.rc
else
    echo "$ZCE_PREFIX/bin/shell_functions.rc doesn't exist!"
    exit 1;
fi
check_root_privileges
export ZEND_TMPDIR=$ZCE_PREFIX/tmp 
export TMPDIR=$ZCE_PREFIX/tmp 
usage()
{
    $ECHO_CMD "Usage: $0 <action>"
    $ECHO_CMD ""
    for ACTION in start stop restart;do
        $ECHO_CMD "$ACTION:\n   $ACTION all $PRODUCT_NAME daemons"
        for SCRIPT in $ZCE_PREFIX/etc/rc.d/*;do  
	    SCRIPT=`echo $SCRIPT|sed 's/[0-9][0-9]//'`
            $ECHO_CMD "$ACTION-`basename $SCRIPT:`\n    $ACTION `basename $SCRIPT` only.";
        done
        $ECHO_CMD "\n"
    done
    $ECHO_CMD "setup-jb            Setup Java bridge"
    $ECHO_CMD "version             Print $PRODUCT_NAME version"
    $ECHO_CMD "status              Get $PRODUCT_NAME status"
}
case $1 in
	"start")
		$ECHO_CMD "Starting $PRODUCT_NAME $PRODUCT_VERSION ..\n"
                if [ -d $ZCE_PREFIX/etc/rc.d ];then
                    for SCRIPT in $ZCE_PREFIX/etc/rc.d/*;do
			SCRIPT=`echo $SCRIPT|sed 's/[0-9][0-9]//'`
                        $0 $1-`basename $SCRIPT` %
                    done
                else
                    $0 $1-apache %
                    $0 $1-lighttpd %
                    $0 $1-monitor %
                fi
		$ECHO_CMD "\n$PRODUCT_NAME started..."
		;;

	"restart")
		$ECHO_CMD "Restarting $PRODUCT_NAME $PRODUCT_VERSION ..\n"
                if [ -d $ZCE_PREFIX/etc/rc.d ];then
                    for SCRIPT in $ZCE_PREFIX/etc/rc.d/*;do
		    	SCRIPT=`echo $SCRIPT|sed 's/[0-9][0-9]//'`
                        $0 stop-`basename $SCRIPT` %
                    done
				$ZCE_PREFIX/bin/clean_semaphores.sh
                sleep 2 
                    for SCRIPT in $ZCE_PREFIX/etc/rc.d/*;do
		    	SCRIPT=`echo $SCRIPT|sed 's/[0-9][0-9]//'`
                        $0 start-`basename $SCRIPT` %
                    done
                else
                    $0 $1-apache %
                    $0 $1-lighttpd %
                    $0 $1-monitor %
                fi
		$ECHO_CMD "\n$PRODUCT_NAME started..."
		;;

	"stop")
		$ECHO_CMD "Stopping $PRODUCT_NAME $PRODUCT_VERSION ..\n"
		if [ -d $ZCE_PREFIX/etc/rc.d ];then
			for SCRIPT in $ZCE_PREFIX/etc/rc.d/*;do
				SCRIPT=`echo $SCRIPT|sed 's/[0-9][0-9]//'`
				$0 $1-`basename $SCRIPT` %
			done
		else
			$0 $1-apache %
			$0 $1-lighttpd %
			$0 $1-monitor %
		fi
		$ZCE_PREFIX/bin/clean_semaphores.sh
        sleep 2 
		$ECHO_CMD "\n$PRODUCT_NAME stopped."
		;;

	"start-apache")
                if [ -x $ZCE_PREFIX/bin/apachectl ];then
                    $ZCE_PREFIX/bin/apachectl start
                fi
		;;

	"graceful-apache")
                if [ -x $ZCE_PREFIX/bin/apachectl ];then
                    $ZCE_PREFIX/bin/apachectl graceful
                fi
		;;

	"start-lighttpd")
				if [ -x $ZCE_PREFIX/bin/lighttpdctl.sh ];then
                	$ZCE_PREFIX/bin/lighttpdctl.sh start
				fi
		;;

	"start-monitor")
                if [ -x $ZCE_PREFIX/bin/monitor-node.sh ];then
                    $ZCE_PREFIX/bin/monitor-node.sh start
                fi
                ;;
		
	"start-scd")
                if [ -x $ZCE_PREFIX/bin/scd.sh ];then
                    $ZCE_PREFIX/bin/scd.sh start
                fi
		;;
		
	"start-jobqueue")
                if [ -x $ZCE_PREFIX/bin/jqd.sh ];then
                    $ZCE_PREFIX/bin/jqd.sh start
                fi
		;;
		
	"start-jb")
                if [ -x $ZCE_PREFIX/etc/rc.d/06jb ];then
                    $ZCE_PREFIX/bin/java_bridge.sh start
		fi
		;;

	"stop-apache")
                if [ -x $ZCE_PREFIX/bin/apachectl ];then
                    $ZCE_PREFIX/bin/apachectl stop
                fi
		;;

	"stop-lighttpd")
				if [ -x $ZCE_PREFIX/bin/lighttpdctl.sh ];then
                	$ZCE_PREFIX/bin/lighttpdctl.sh stop
				fi
		;;

	"stop-monitor")
                if [ -x $ZCE_PREFIX/bin/monitor-node.sh ];then
                    $ZCE_PREFIX/bin/monitor-node.sh stop
                fi
		;;

	"stop-scd")
                if [ -x $ZCE_PREFIX/bin/scd.sh ];then
                    $ZCE_PREFIX/bin/scd.sh stop
                fi
		;;

	"stop-jobqueue")
                if [ -x $ZCE_PREFIX/bin/jqd.sh ];then
                    $ZCE_PREFIX/bin/jqd.sh stop
                fi
		;;

	"restart-lighttpd")
				if [ -x $ZCE_PREFIX/bin/lighttpdctl.sh ];then
                	$ZCE_PREFIX/bin/lighttpdctl.sh restart
				fi
		;;

	"restart-scd")
                if [ -x $ZCE_PREFIX/bin/scd.sh ];then
                    $ZCE_PREFIX/bin/scd.sh restart
                fi
		;;

	"restart-monitor")
                if [ -x $ZCE_PREFIX/bin/monitor-node.sh ];then
                    $ZCE_PREFIX/bin/monitor-node.sh restart
                fi
		;;

	"restart-jobqueue")
                if [ -x $ZCE_PREFIX/bin/jqd.sh ];then
                    $ZCE_PREFIX/bin/jqd.sh restart
                fi
		;;

	"stop-jb")
                if [ -x $ZCE_PREFIX/etc/rc.d/06jb ];then
                    $ZCE_PREFIX/bin/java_bridge.sh stop
		fi
		;;

	"restart-jb")
                if [ -x $ZCE_PREFIX/etc/rc.d/06jb ];then
                    $ZCE_PREFIX/bin/java_bridge.sh restart
		fi
		;;

	"setup-jb")
                if [ -x $ZCE_PREFIX/bin/setup_jb.sh ];then
                    $ZCE_PREFIX/bin/setup_jb.sh
                else
                    echo "Java bridge is not installed, please install the java-bridge-zend-$DIST package."
                fi
		;;

	"restart-apache")
		$0 stop-apache
		sleep 2
		$0 start-apache
		;;

	"restart")
		$0 stop
		sleep 2 
		$0 start
		;;

	"status")
                apache_status $APACHE_PID_FILE
                for SCRIPT in $ZCE_PREFIX/etc/rc.d/*;do
		    $SCRIPT status
                done
		;;


        "version")
                $ECHO_CMD "$PRODUCT_NAME version: $PRODUCT_VERSION"
                ;;

	*)	
                usage
                exit 1
		;;
esac
