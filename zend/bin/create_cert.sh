#!/bin/sh

if [ -f /etc/zce.rc ];then
    . /etc/zce.rc
else
    echo "/etc/zce.rc doesn't exist!"
    exit 1;
fi
PATH=$ZCE_PREFIX/bin:$PATH
mkdir -p $ZCE_PREFIX/etc/tls/certs
FQDN=`hostname`
if [ "$FQDN" = "" ];then
    FQDN=localhost.localdomain
fi
if [ -f $ZCE_PREFIX/etc/openssl.cnf ];then
    OPENSSL_CONF="$ZCE_PREFIX/etc/openssl.cnf"
    export OPENSSL_CONF
fi
if [ ! -f $ZCE_PREFIX/etc/tls/certs/lighttpd.pem ] ; then
    umask 077
    openssl req -new -x509 -days 365 -nodes \
                -out $ZCE_PREFIX/etc/tls/certs/lighttpd.pem  \
                -keyout $ZCE_PREFIX/etc/tls/certs/lighttpd.pem << EOF >/dev/null 2>&1
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
${FQDN}
root@${FQDN}
EOF
    chmod 600 $ZCE_PREFIX/etc/tls/certs/lighttpd.pem
fi
