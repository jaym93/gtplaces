#!/bin/sh

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

PATH=$PATH:$ZCE_PREFIX/bin
check_root_privileges
if [ -z "$TMPDIR" ];then
    TMPDIR=/tmp
fi
STAMP=`date +%m%d%y%H%M%S`
ZEND_DATA_TMPDIR=$TMPDIR/report_bug_$STAMP
mkdir -p $ZEND_DATA_TMPDIR
export ZEND_DATA_TMPDIR
cd $ZEND_DATA_TMPDIR
while read COM ARG; do
    if which $COM > /dev/null 2>&1 ;then
        $COM $ARG >$ZEND_DATA_TMPDIR/$COM.out
	if [ $? -ne 0 ];then 
        	echo "$COM $ARG executed return code was not 0." >>$ZEND_DATA_TMPDIR/report_bug_error.log
	fi
    else
        echo "Could not execute $COM." >>$ZEND_DATA_TMPDIR/report_bug_error.log
    fi
done < "$ZCE_PREFIX"/share/bugreport/commands
if [ -n "$BASH_VERSION" ];then
    ulimit -a >$ZEND_DATA_TMPDIR/ulimit.out
fi

while read FILE DEST; do
    if [ -e "$FILE" ]; then
        cp -R $FILE $ZEND_DATA_TMPDIR/$DEST
    else
        echo "Could not copy $FILE into $ZEND_DATA_TMPDIR" >>$ZEND_DATA_TMPDIR/report_bug_error.log
    fi
done < "$ZCE_PREFIX"/share/bugreport/files
cat <<EOF

The information was collected successfully.
Use free text to describe the issue in your own words.
To submit the information press CONTROL-D

EOF
cat > $ZEND_DATA_TMPDIR/free_problem_desc
cd $TMPDIR
tar zcf zend_server_report_bug_$STAMP.tar.gz report_bug_$STAMP 
if [ $? -eq 0 ];then
    rm -rf $ZEND_DATA_TMPDIR
    echo "Archive created at $TMPDIR/zend_server_report_bug_$STAMP.tar.gz"
else
    echo "Could not create the archive, leaving $ZEND_DATA_TMPDIR behind for you to archive manually."
fi

