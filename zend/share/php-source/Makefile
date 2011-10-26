srcdir = /php-5.3.2
builddir = /php-5.3.2
top_srcdir = /php-5.3.2
top_builddir = /php-5.3.2
EGREP = grep -E
SED = /bin/sed
CONFIGURE_COMMAND = './configure' '--disable-xml' '--disable-dom' '--disable-libxml' '--disable-simplexml' '--without-pear' '--disable-xmlreader' '--disable-xmlwriter' '--without-iconv' '--with-openssl-dir=/usr/local/openssl-0.9.8l'
CONFIGURE_OPTIONS = '--disable-xml' '--disable-dom' '--disable-libxml' '--disable-simplexml' '--without-pear' '--disable-xmlreader' '--disable-xmlwriter' '--without-iconv' '--with-openssl-dir=/usr/local/openssl-0.9.8l'
PHP_MAJOR_VERSION = 5
PHP_MINOR_VERSION = 3
PHP_RELEASE_VERSION = 2
PHP_EXTRA_VERSION =
AWK = gawk
YACC = bison -y
RE2C = exit 0;
RE2C_FLAGS =
SHLIB_SUFFIX_NAME = so
SHLIB_DL_SUFFIX_NAME = so
SAPI_CLI_PATH = sapi/cli/php
BUILD_CLI = $(LIBTOOL) --mode=link $(CC) -export-dynamic $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) $(EXTRA_LDFLAGS_PROGRAM) $(LDFLAGS) $(PHP_RPATHS) $(PHP_GLOBAL_OBJS) $(PHP_CLI_OBJS) $(EXTRA_LIBS) $(ZEND_EXTRA_LIBS) -o $(SAPI_CLI_PATH)
INSTALL_CLI = $(mkinstalldirs) $(INSTALL_ROOT)$(bindir); $(INSTALL) -m 0755 $(SAPI_CLI_PATH) $(INSTALL_ROOT)$(bindir)/$(program_prefix)php$(program_suffix)$(EXEEXT)
SAPI_CGI_PATH = sapi/cgi/php-cgi
BUILD_CGI = $(LIBTOOL) --mode=link $(CC) -export-dynamic $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) $(EXTRA_LDFLAGS_PROGRAM) $(LDFLAGS) $(PHP_RPATHS) $(PHP_GLOBAL_OBJS) $(PHP_SAPI_OBJS) $(EXTRA_LIBS) $(ZEND_EXTRA_LIBS) -o $(SAPI_CGI_PATH)
PROG_SENDMAIL =
SQLITE3_SHARED_LIBADD =
FILTER_SHARED_LIBADD =
JSON_SHARED_LIBADD =
PDO_SQLITE_SHARED_LIBADD =
SESSION_SHARED_LIBADD =
LEMON = exit 0;
SQLITE_SHARED_LIBADD =
SQLITE_ENCODING = ISO8859
SQLITE_VERSION = 2.8.17
PHP_INSTALLED_SAPIS = cli cgi
PHP_EXECUTABLE = $(top_builddir)/$(SAPI_CLI_PATH)
PHP_CLI_TARGET = $(SAPI_CLI_PATH)
PHP_SAPI_OBJS = sapi/cgi/cgi_main.lo sapi/cgi/fastcgi.lo main/internal_functions.lo
PHP_CLI_OBJS = sapi/cli/php_cli.lo sapi/cli/php_cli_readline.lo main/internal_functions_cli.lo
PHP_GLOBAL_OBJS = ext/date/php_date.lo ext/date/lib/astro.lo ext/date/lib/dow.lo ext/date/lib/parse_date.lo ext/date/lib/parse_tz.lo ext/date/lib/timelib.lo ext/date/lib/tm2unixtime.lo ext/date/lib/unixtime2tm.lo ext/date/lib/parse_iso_intervals.lo ext/date/lib/interval.lo ext/ereg/ereg.lo ext/ereg/regex/regcomp.lo ext/ereg/regex/regexec.lo ext/ereg/regex/regerror.lo ext/ereg/regex/regfree.lo ext/pcre/pcrelib/pcre_chartables.lo ext/pcre/pcrelib/pcre_ucd.lo ext/pcre/pcrelib/pcre_compile.lo ext/pcre/pcrelib/pcre_config.lo ext/pcre/pcrelib/pcre_exec.lo ext/pcre/pcrelib/pcre_fullinfo.lo ext/pcre/pcrelib/pcre_get.lo ext/pcre/pcrelib/pcre_globals.lo ext/pcre/pcrelib/pcre_info.lo ext/pcre/pcrelib/pcre_maketables.lo ext/pcre/pcrelib/pcre_newline.lo ext/pcre/pcrelib/pcre_ord2utf8.lo ext/pcre/pcrelib/pcre_refcount.lo ext/pcre/pcrelib/pcre_study.lo ext/pcre/pcrelib/pcre_tables.lo ext/pcre/pcrelib/pcre_try_flipped.lo ext/pcre/pcrelib/pcre_valid_utf8.lo ext/pcre/pcrelib/pcre_version.lo ext/pcre/pcrelib/pcre_xclass.lo ext/pcre/php_pcre.lo ext/sqlite3/sqlite3.lo ext/sqlite3/libsqlite/sqlite3.lo ext/ctype/ctype.lo ext/fileinfo/fileinfo.lo ext/fileinfo/libmagic/apprentice.lo ext/fileinfo/libmagic/apptype.lo ext/fileinfo/libmagic/ascmagic.lo ext/fileinfo/libmagic/cdf.lo ext/fileinfo/libmagic/cdf_time.lo ext/fileinfo/libmagic/compress.lo ext/fileinfo/libmagic/encoding.lo ext/fileinfo/libmagic/fsmagic.lo ext/fileinfo/libmagic/funcs.lo ext/fileinfo/libmagic/is_tar.lo ext/fileinfo/libmagic/magic.lo ext/fileinfo/libmagic/print.lo ext/fileinfo/libmagic/readcdf.lo ext/fileinfo/libmagic/readelf.lo ext/fileinfo/libmagic/softmagic.lo ext/filter/filter.lo ext/filter/sanitizing_filters.lo ext/filter/logical_filters.lo ext/filter/callback_filter.lo ext/hash/hash.lo ext/hash/hash_md.lo ext/hash/hash_sha.lo ext/hash/hash_ripemd.lo ext/hash/hash_haval.lo ext/hash/hash_tiger.lo ext/hash/hash_gost.lo ext/hash/hash_snefru.lo ext/hash/hash_whirlpool.lo ext/hash/hash_adler32.lo ext/hash/hash_crc32.lo ext/hash/hash_salsa.lo ext/json/json.lo ext/json/utf8_to_utf16.lo ext/json/utf8_decode.lo ext/json/JSON_parser.lo ext/pdo/pdo.lo ext/pdo/pdo_dbh.lo ext/pdo/pdo_stmt.lo ext/pdo/pdo_sql_parser.lo ext/pdo/pdo_sqlstate.lo ext/pdo_sqlite/pdo_sqlite.lo ext/pdo_sqlite/sqlite_driver.lo ext/pdo_sqlite/sqlite_statement.lo ext/phar/util.lo ext/phar/tar.lo ext/phar/zip.lo ext/phar/stream.lo ext/phar/func_interceptors.lo ext/phar/dirstream.lo ext/phar/phar.lo ext/phar/phar_object.lo ext/phar/phar_path_check.lo ext/posix/posix.lo ext/reflection/php_reflection.lo ext/session/session.lo ext/session/mod_files.lo ext/session/mod_mm.lo ext/session/mod_user.lo ext/spl/php_spl.lo ext/spl/spl_functions.lo ext/spl/spl_engine.lo ext/spl/spl_iterators.lo ext/spl/spl_array.lo ext/spl/spl_directory.lo ext/spl/spl_exceptions.lo ext/spl/spl_observer.lo ext/spl/spl_dllist.lo ext/spl/spl_heap.lo ext/spl/spl_fixedarray.lo ext/sqlite/sqlite.lo ext/sqlite/sess_sqlite.lo ext/sqlite/pdo_sqlite2.lo ext/sqlite/libsqlite/src/opcodes.lo ext/sqlite/libsqlite/src/parse.lo ext/sqlite/libsqlite/src/encode.lo ext/sqlite/libsqlite/src/auth.lo ext/sqlite/libsqlite/src/btree.lo ext/sqlite/libsqlite/src/build.lo ext/sqlite/libsqlite/src/delete.lo ext/sqlite/libsqlite/src/expr.lo ext/sqlite/libsqlite/src/func.lo ext/sqlite/libsqlite/src/hash.lo ext/sqlite/libsqlite/src/insert.lo ext/sqlite/libsqlite/src/main.lo ext/sqlite/libsqlite/src/os.lo ext/sqlite/libsqlite/src/pager.lo ext/sqlite/libsqlite/src/printf.lo ext/sqlite/libsqlite/src/random.lo ext/sqlite/libsqlite/src/select.lo ext/sqlite/libsqlite/src/table.lo ext/sqlite/libsqlite/src/tokenize.lo ext/sqlite/libsqlite/src/update.lo ext/sqlite/libsqlite/src/util.lo ext/sqlite/libsqlite/src/vdbe.lo ext/sqlite/libsqlite/src/attach.lo ext/sqlite/libsqlite/src/btree_rb.lo ext/sqlite/libsqlite/src/pragma.lo ext/sqlite/libsqlite/src/vacuum.lo ext/sqlite/libsqlite/src/copy.lo ext/sqlite/libsqlite/src/vdbeaux.lo ext/sqlite/libsqlite/src/date.lo ext/sqlite/libsqlite/src/where.lo ext/sqlite/libsqlite/src/trigger.lo ext/standard/crypt_freesec.lo ext/standard/crypt_blowfish.lo ext/standard/crypt_sha512.lo ext/standard/crypt_sha256.lo ext/standard/php_crypt_r.lo ext/standard/array.lo ext/standard/base64.lo ext/standard/basic_functions.lo ext/standard/browscap.lo ext/standard/crc32.lo ext/standard/crypt.lo ext/standard/cyr_convert.lo ext/standard/datetime.lo ext/standard/dir.lo ext/standard/dl.lo ext/standard/dns.lo ext/standard/exec.lo ext/standard/file.lo ext/standard/filestat.lo ext/standard/flock_compat.lo ext/standard/formatted_print.lo ext/standard/fsock.lo ext/standard/head.lo ext/standard/html.lo ext/standard/image.lo ext/standard/info.lo ext/standard/iptc.lo ext/standard/lcg.lo ext/standard/link.lo ext/standard/mail.lo ext/standard/math.lo ext/standard/md5.lo ext/standard/metaphone.lo ext/standard/microtime.lo ext/standard/pack.lo ext/standard/pageinfo.lo ext/standard/quot_print.lo ext/standard/rand.lo ext/standard/soundex.lo ext/standard/string.lo ext/standard/scanf.lo ext/standard/syslog.lo ext/standard/type.lo ext/standard/uniqid.lo ext/standard/url.lo ext/standard/var.lo ext/standard/versioning.lo ext/standard/assert.lo ext/standard/strnatcmp.lo ext/standard/levenshtein.lo ext/standard/incomplete_class.lo ext/standard/url_scanner_ex.lo ext/standard/ftp_fopen_wrapper.lo ext/standard/http_fopen_wrapper.lo ext/standard/php_fopen_wrapper.lo ext/standard/credits.lo ext/standard/css.lo ext/standard/var_unserializer.lo ext/standard/ftok.lo ext/standard/sha1.lo ext/standard/user_filters.lo ext/standard/uuencode.lo ext/standard/filters.lo ext/standard/proc_open.lo ext/standard/streamsfuncs.lo ext/standard/http.lo ext/tokenizer/tokenizer.lo ext/tokenizer/tokenizer_data.lo TSRM/TSRM.lo TSRM/tsrm_strtok_r.lo TSRM/tsrm_virtual_cwd.lo main/main.lo main/snprintf.lo main/spprintf.lo main/php_sprintf.lo main/safe_mode.lo main/fopen_wrappers.lo main/alloca.lo main/php_scandir.lo main/php_ini.lo main/SAPI.lo main/rfc1867.lo main/php_content_types.lo main/strlcpy.lo main/strlcat.lo main/mergesort.lo main/reentrancy.lo main/php_variables.lo main/php_ticks.lo main/network.lo main/php_open_temporary_file.lo main/php_logos.lo main/output.lo main/getopt.lo main/streams/streams.lo main/streams/cast.lo main/streams/memory.lo main/streams/filter.lo main/streams/plain_wrapper.lo main/streams/userspace.lo main/streams/transports.lo main/streams/xp_socket.lo main/streams/mmap.lo main/streams/glob_wrapper.lo Zend/zend_language_parser.lo Zend/zend_language_scanner.lo Zend/zend_ini_parser.lo Zend/zend_ini_scanner.lo Zend/zend_alloc.lo Zend/zend_compile.lo Zend/zend_constants.lo Zend/zend_dynamic_array.lo Zend/zend_execute_API.lo Zend/zend_highlight.lo Zend/zend_llist.lo Zend/zend_opcode.lo Zend/zend_operators.lo Zend/zend_ptr_stack.lo Zend/zend_stack.lo Zend/zend_variables.lo Zend/zend.lo Zend/zend_API.lo Zend/zend_extensions.lo Zend/zend_hash.lo Zend/zend_list.lo Zend/zend_indent.lo Zend/zend_builtin_functions.lo Zend/zend_sprintf.lo Zend/zend_ini.lo Zend/zend_qsort.lo Zend/zend_multibyte.lo Zend/zend_ts_hash.lo Zend/zend_stream.lo Zend/zend_iterators.lo Zend/zend_interfaces.lo Zend/zend_exceptions.lo Zend/zend_strtod.lo Zend/zend_gc.lo Zend/zend_closures.lo Zend/zend_float.lo Zend/zend_objects.lo Zend/zend_object_handlers.lo Zend/zend_objects_API.lo Zend/zend_default_classes.lo Zend/zend_execute.lo
PHP_MODULES =
PHP_ZEND_EX =
EXT_LIBS =
abs_builddir = /php-5.3.2
abs_srcdir = /php-5.3.2
php_abs_top_builddir = /php-5.3.2
php_abs_top_srcdir = /php-5.3.2
bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/sbin
exec_prefix = ${prefix}
program_prefix =
program_suffix =
includedir = ${prefix}/include
libdir = ${exec_prefix}/lib/php
mandir = ${prefix}/man
phplibdir = /php-5.3.2/modules
phptempdir = /php-5.3.2/libs
prefix = /usr/local
localstatedir = ${prefix}/var
datadir = ${prefix}/share/php
datarootdir = /usr/local/php
sysconfdir = ${prefix}/etc
EXEEXT =
CC = gcc
CFLAGS = $(CFLAGS_CLEAN) -prefer-non-pic -static
CFLAGS_CLEAN = -O2 -pipe -g -fvisibility=hidden
CPP = gcc -E
CPPFLAGS =
CXX =
CXXFLAGS = -prefer-non-pic -static
CXXFLAGS_CLEAN =
DEBUG_CFLAGS =
EXTENSION_DIR = /usr/local/lib/php/extensions/no-debug-non-zts-20090626
EXTRA_LDFLAGS =
EXTRA_LDFLAGS_PROGRAM =
EXTRA_LIBS = -lcrypt -lresolv -lcrypt -lrt -lrt -lm -ldl -lnsl -lcrypt -lcrypt
ZEND_EXTRA_LIBS =
INCLUDES = -I/php-5.3.2/ext/date/lib -I/php-5.3.2/ext/ereg/regex -I/php-5.3.2/ext/sqlite3/libsqlite -I$(top_builddir)/TSRM -I$(top_builddir)/Zend
EXTRA_INCLUDES =
INCLUDE_PATH = .:
INSTALL_IT = @echo "Installing PHP CGI binary: $(INSTALL_ROOT)$(bindir)/"; $(INSTALL) -m 0755 $(SAPI_CGI_PATH) $(INSTALL_ROOT)$(bindir)/$(program_prefix)php-cgi$(program_suffix)$(EXEEXT)
LFLAGS =
LIBTOOL = $(SHELL) $(top_builddir)/libtool --silent --preserve-dup-deps
LN_S = ln -s
NATIVE_RPATHS =
PEAR_INSTALLDIR =
PHP_BUILD_DATE = 2010-03-31
PHP_LDFLAGS =
PHP_LIBS =
OVERALL_TARGET = $(SAPI_CGI_PATH)
PHP_RPATHS =
PHP_SAPI = cgi
PHP_VERSION = 5.3.2
PHP_VERSION_ID = 50302
SHELL = /bin/sh
SHARED_LIBTOOL = $(LIBTOOL)
WARNING_LEVEL =
PHP_FRAMEWORKS =
PHP_FRAMEWORKPATH =
INSTALL_HEADERS = ext/date/php_date.h ext/date/lib/timelib.h ext/date/lib/timelib_structs.h ext/date/lib/timelib_config.h ext/ereg/php_ereg.h ext/ereg/php_regex.h ext/ereg/regex/ ext/pcre/php_pcre.h ext/pcre/pcrelib/ ext/filter/php_filter.h ext/hash/php_hash.h ext/hash/php_hash_md.h ext/hash/php_hash_sha.h ext/hash/php_hash_ripemd.h ext/hash/php_hash_haval.h ext/hash/php_hash_tiger.h ext/hash/php_hash_gost.h ext/hash/php_hash_snefru.h ext/hash/php_hash_whirlpool.h ext/hash/php_hash_adler32.h ext/hash/php_hash_crc32.h ext/hash/php_hash_salsa.h ext/hash/php_hash_types.h ext/json/php_json.h ext/pdo/php_pdo.h ext/pdo/php_pdo_driver.h ext/session/php_session.h ext/session/mod_files.h ext/session/mod_user.h ext/spl/php_spl.h ext/spl/spl_array.h ext/spl/spl_directory.h ext/spl/spl_engine.h ext/spl/spl_exceptions.h ext/spl/spl_functions.h ext/spl/spl_iterators.h ext/spl/spl_observer.h ext/spl/spl_dllist.h ext/spl/spl_heap.h ext/spl/spl_fixedarray.h ext/sqlite/libsqlite/src/sqlite.h ext/standard/ Zend/ TSRM/ include/ main/ main/streams/
ZEND_EXT_TYPE = zend_extension
all_targets = $(OVERALL_TARGET) $(PHP_MODULES) $(PHP_ZEND_EX) $(PHP_CLI_TARGET) pharcmd
install_targets = install-sapi install-cli install-build install-headers install-programs install-pharcmd
mkinstalldirs = $(top_srcdir)/build/shtool mkdir -p
INSTALL = $(top_srcdir)/build/shtool install -c
INSTALL_DATA = $(INSTALL) -m 644

DEFS = -DPHP_ATOM_INC -I$(top_builddir)/include -I$(top_builddir)/main -I$(top_srcdir)
COMMON_FLAGS = $(DEFS) $(INCLUDES) $(EXTRA_INCLUDES) $(CPPFLAGS) $(PHP_FRAMEWORKPATH)

all: $(all_targets) 
	@echo
	@echo "Build complete."
	@echo "Don't forget to run 'make test'."
	@echo
	
build-modules: $(PHP_MODULES) $(PHP_ZEND_EX)

libphp$(PHP_MAJOR_VERSION).la: $(PHP_GLOBAL_OBJS) $(PHP_SAPI_OBJS)
	$(LIBTOOL) --mode=link $(CC) $(CFLAGS) $(EXTRA_CFLAGS) -rpath $(phptempdir) $(EXTRA_LDFLAGS) $(LDFLAGS) $(PHP_RPATHS) $(PHP_GLOBAL_OBJS) $(PHP_SAPI_OBJS) $(EXTRA_LIBS) $(ZEND_EXTRA_LIBS) -o $@
	-@$(LIBTOOL) --silent --mode=install cp $@ $(phptempdir)/$@ >/dev/null 2>&1

libs/libphp$(PHP_MAJOR_VERSION).bundle: $(PHP_GLOBAL_OBJS) $(PHP_SAPI_OBJS)
	$(CC) $(MH_BUNDLE_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) $(LDFLAGS) $(EXTRA_LDFLAGS) $(PHP_GLOBAL_OBJS:.lo=.o) $(PHP_SAPI_OBJS:.lo=.o) $(PHP_FRAMEWORKS) $(EXTRA_LIBS) $(ZEND_EXTRA_LIBS) -o $@ && cp $@ libs/libphp$(PHP_MAJOR_VERSION).so

install: $(all_targets) $(install_targets)

install-sapi: $(OVERALL_TARGET)
	@echo "Installing PHP SAPI module:       $(PHP_SAPI)"
	-@$(mkinstalldirs) $(INSTALL_ROOT)$(bindir)
	-@if test ! -r $(phptempdir)/libphp$(PHP_MAJOR_VERSION).$(SHLIB_DL_SUFFIX_NAME); then \
		for i in 0.0.0 0.0 0; do \
			if test -r $(phptempdir)/libphp$(PHP_MAJOR_VERSION).$(SHLIB_DL_SUFFIX_NAME).$$i; then \
				$(LN_S) $(phptempdir)/libphp$(PHP_MAJOR_VERSION).$(SHLIB_DL_SUFFIX_NAME).$$i $(phptempdir)/libphp$(PHP_MAJOR_VERSION).$(SHLIB_DL_SUFFIX_NAME); \
				break; \
			fi; \
		done; \
	fi
	@$(INSTALL_IT)

install-modules: build-modules
	@test -d modules && \
	$(mkinstalldirs) $(INSTALL_ROOT)$(EXTENSION_DIR)
	@echo "Installing shared extensions:     $(INSTALL_ROOT)$(EXTENSION_DIR)/"
	@rm -f modules/*.la >/dev/null 2>&1
	@$(INSTALL) modules/* $(INSTALL_ROOT)$(EXTENSION_DIR)

install-headers:
	-@if test "$(INSTALL_HEADERS)"; then \
		for i in `echo $(INSTALL_HEADERS)`; do \
			i=`$(top_srcdir)/build/shtool path -d $$i`; \
			paths="$$paths $(INSTALL_ROOT)$(phpincludedir)/$$i"; \
		done; \
		$(mkinstalldirs) $$paths && \
		echo "Installing header files:          $(INSTALL_ROOT)$(phpincludedir)/" && \
		for i in `echo $(INSTALL_HEADERS)`; do \
			if test "$(PHP_PECL_EXTENSION)"; then \
				src=`echo $$i | $(SED) -e "s#ext/$(PHP_PECL_EXTENSION)/##g"`; \
			else \
				src=$$i; \
			fi; \
			if test -f "$(top_srcdir)/$$src"; then \
				$(INSTALL_DATA) $(top_srcdir)/$$src $(INSTALL_ROOT)$(phpincludedir)/$$i; \
			elif test -f "$(top_builddir)/$$src"; then \
				$(INSTALL_DATA) $(top_builddir)/$$src $(INSTALL_ROOT)$(phpincludedir)/$$i; \
			else \
				(cd $(top_srcdir)/$$src && $(INSTALL_DATA) *.h $(INSTALL_ROOT)$(phpincludedir)/$$i; \
				cd $(top_builddir)/$$src && $(INSTALL_DATA) *.h $(INSTALL_ROOT)$(phpincludedir)/$$i) 2>/dev/null || true; \
			fi \
		done; \
	fi

PHP_TEST_SETTINGS = -d 'open_basedir=' -d 'output_buffering=0' -d 'memory_limit=-1'
PHP_TEST_SHARED_EXTENSIONS =  ` \
	if test "x$(PHP_MODULES)" != "x"; then \
		for i in $(PHP_MODULES)""; do \
			. $$i; $(top_srcdir)/build/shtool echo -n -- " -d extension=$$dlname"; \
		done; \
	fi; \
	if test "x$(PHP_ZEND_EX)" != "x"; then \
		for i in $(PHP_ZEND_EX)""; do \
			. $$i; $(top_srcdir)/build/shtool echo -n -- " -d $(ZEND_EXT_TYPE)=$(top_builddir)/modules/$$dlname"; \
		done; \
	fi`
PHP_DEPRECATED_DIRECTIVES_REGEX = '^(define_syslog_variables|register_(globals|long_arrays)?|safe_mode|magic_quotes_(gpc|runtime|sybase)?|(zend_)?extension(_debug)?(_ts)?)[\t\ ]*='

test: all
	-@if test ! -z "$(PHP_EXECUTABLE)" && test -x "$(PHP_EXECUTABLE)"; then \
		INI_FILE=`$(PHP_EXECUTABLE) -d 'display_errors=stderr' -r 'echo php_ini_loaded_file();' 2> /dev/null`; \
		if test "$$INI_FILE"; then \
			$(EGREP) -h -v $(PHP_DEPRECATED_DIRECTIVES_REGEX) "$$INI_FILE" > $(top_builddir)/tmp-php.ini; \
		else \
			echo > $(top_builddir)/tmp-php.ini; \
		fi; \
		INI_SCANNED_PATH=`$(PHP_EXECUTABLE) -d 'display_errors=stderr' -r '$$a = explode(",\n", trim(php_ini_scanned_files())); echo $$a[0];' 2> /dev/null`; \
		if test "$$INI_SCANNED_PATH"; then \
			INI_SCANNED_PATH=`$(top_srcdir)/build/shtool path -d $$INI_SCANNED_PATH`; \
			$(EGREP) -h -v $(PHP_DEPRECATED_DIRECTIVES_REGEX) "$$INI_SCANNED_PATH"/*.ini >> $(top_builddir)/tmp-php.ini; \
		fi; \
		TEST_PHP_EXECUTABLE=$(PHP_EXECUTABLE) \
		TEST_PHP_SRCDIR=$(top_srcdir) \
		CC="$(CC)" \
			$(PHP_EXECUTABLE) -n -c $(top_builddir)/tmp-php.ini $(PHP_TEST_SETTINGS) $(top_srcdir)/run-tests.php -n -c $(top_builddir)/tmp-php.ini -d extension_dir=$(top_builddir)/modules/ $(PHP_TEST_SHARED_EXTENSIONS) $(TESTS); \
	else \
		echo "ERROR: Cannot run tests without CLI sapi."; \
	fi

clean:
	find . -name \*.gcno -o -name \*.gcda | xargs rm -f
	find . -name \*.lo -o -name \*.o | xargs rm -f
	find . -name \*.la -o -name \*.a | xargs rm -f 
	find . -name \*.so | xargs rm -f
	find . -name .libs -a -type d|xargs rm -rf
	rm -f libphp$(PHP_MAJOR_VERSION).la $(SAPI_CLI_PATH) $(OVERALL_TARGET) modules/* libs/*

distclean: clean
	rm -f Makefile config.cache config.log config.status Makefile.objects Makefile.fragments libtool main/php_config.h stamp-h sapi/apache/libphp$(PHP_MAJOR_VERSION).module buildmk.stamp
	$(EGREP) define'.*include/php' $(top_srcdir)/configure | $(SED) 's/.*>//'|xargs rm -f

.PHONY: all clean install distclean test
.NOEXPORT:
cli: $(SAPI_CLI_PATH)

$(SAPI_CLI_PATH): $(PHP_GLOBAL_OBJS) $(PHP_CLI_OBJS)
	$(BUILD_CLI)

install-cli: $(SAPI_CLI_PATH)
	@echo "Installing PHP CLI binary:        $(INSTALL_ROOT)$(bindir)/"
	@$(INSTALL_CLI)
	@echo "Installing PHP CLI man page:      $(INSTALL_ROOT)$(mandir)/man1/"
	@$(mkinstalldirs) $(INSTALL_ROOT)$(mandir)/man1
	@$(INSTALL_DATA) sapi/cli/php.1 $(INSTALL_ROOT)$(mandir)/man1/$(program_prefix)php$(program_suffix).1
$(SAPI_CGI_PATH): $(PHP_GLOBAL_OBJS) $(PHP_SAPI_OBJS)
	$(BUILD_CGI)

ext/fileinfo/libmagic/apprentice.lo: /php-5.3.2/ext/fileinfo/data_file.c
phpincludedir=$(prefix)/include/php

PDO_HEADER_FILES= \
	php_pdo.h \
	php_pdo_driver.h

install-pdo-headers:
	@echo "Installing PDO headers:          $(INSTALL_ROOT)$(phpincludedir)/ext/pdo/"
	@$(mkinstalldirs) $(INSTALL_ROOT)$(phpincludedir)/ext/pdo
	@for f in $(PDO_HEADER_FILES); do \
		if test -f "$(top_srcdir)/$$f"; then \
			$(INSTALL_DATA) $(top_srcdir)/$$f $(INSTALL_ROOT)$(phpincludedir)/ext/pdo; \
		elif test -f "$(top_builddir)/$$f"; then \
			$(INSTALL_DATA) $(top_builddir)/$$f $(INSTALL_ROOT)$(phpincludedir)/ext/pdo; \
		elif test -f "$(top_srcdir)/ext/pdo/$$f"; then \
			$(INSTALL_DATA) $(top_srcdir)/ext/pdo/$$f $(INSTALL_ROOT)$(phpincludedir)/ext/pdo; \
		elif test -f "$(top_builddir)/ext/pdo/$$f"; then \
			$(INSTALL_DATA) $(top_builddir)/ext/pdo/$$f $(INSTALL_ROOT)$(phpincludedir)/ext/pdo; \
		else \
			echo "hmmm"; \
		fi \
	done;

# mini hack
install: $(all_targets) $(install_targets) install-pdo-headers


/php-5.3.2/ext/phar/phar_path_check.c: /php-5.3.2/ext/phar/phar_path_check.re
	$(RE2C) -b -o /php-5.3.2/ext/phar/phar_path_check.c /php-5.3.2/ext/phar/phar_path_check.re

pharcmd: ext/phar/phar.php ext/phar/phar.phar

PHP_PHARCMD_SETTINGS = -d 'open_basedir=' -d 'output_buffering=0' -d 'memory_limit=-1' -d phar.readonly=0 -d 'safe_mode=0'
PHP_PHARCMD_EXECUTABLE = ` \
	if test -x "$(top_builddir)/$(SAPI_CLI_PATH)"; then \
		$(top_srcdir)/build/shtool echo -n -- "$(top_builddir)/$(SAPI_CLI_PATH) -n"; \
		if test "x$(PHP_MODULES)" != "x"; then \
		$(top_srcdir)/build/shtool echo -n -- " -d extension_dir=$(top_builddir)/modules"; \
		for i in bz2 zlib phar; do \
			if test -f "$(top_builddir)/modules/$$i.la"; then \
				. $(top_builddir)/modules/$$i.la; $(top_srcdir)/build/shtool echo -n -- " -d extension=$$dlname"; \
			fi; \
		done; \
		fi; \
	else \
		$(top_srcdir)/build/shtool echo -n -- "$(PHP_EXECUTABLE)"; \
	fi;`
PHP_PHARCMD_BANG = `if test -x "$(PHP_EXECUTABLE)"; then \
		$(top_srcdir)/build/shtool echo -n -- "$(PHP_EXECUTABLE)"; \
	else \
		$(top_srcdir)/build/shtool echo -n -- "$(INSTALL_ROOT)$(bindir)/$(program_prefix)php$(program_suffix)$(EXEEXT)"; \
	fi; `

ext/phar/phar/phar.inc: /php-5.3.2/ext/phar/phar/phar.inc
	-@test -d ext/phar/phar || mkdir ext/phar/phar
	-@test -f ext/phar/phar/phar.inc || cp /php-5.3.2/ext/phar/phar/phar.inc ext/phar/phar/phar.inc

ext/phar/phar.php: /php-5.3.2/ext/phar/build_precommand.php /php-5.3.2/ext/phar/phar/*.inc /php-5.3.2/ext/phar/phar/*.php $(SAPI_CLI_PATH)
	-@echo "Generating phar.php"
	@$(PHP_PHARCMD_EXECUTABLE) $(PHP_PHARCMD_SETTINGS) /php-5.3.2/ext/phar/build_precommand.php > ext/phar/phar.php

ext/phar/phar.phar: ext/phar/phar.php ext/phar/phar/phar.inc /php-5.3.2/ext/phar/phar/*.inc /php-5.3.2/ext/phar/phar/*.php $(SAPI_CLI_PATH)
	-@echo "Generating phar.phar"
	-@rm -f ext/phar/phar.phar
	-@rm -f /php-5.3.2/ext/phar/phar.phar
	@$(PHP_PHARCMD_EXECUTABLE) $(PHP_PHARCMD_SETTINGS) ext/phar/phar.php pack -f ext/phar/phar.phar -a pharcommand -c auto -x \\.svn -p 0 -s /php-5.3.2/ext/phar/phar/phar.php -h sha1 -b "$(PHP_PHARCMD_BANG)"  /php-5.3.2/ext/phar/phar/
	-@chmod +x ext/phar/phar.phar

install-pharcmd: pharcmd
	-@$(mkinstalldirs) $(INSTALL_ROOT)$(bindir)
	$(INSTALL) ext/phar/phar.phar $(INSTALL_ROOT)$(bindir)
	-@rm -f $(INSTALL_ROOT)$(bindir)/phar
	$(LN_S) -f $(bindir)/phar.phar $(INSTALL_ROOT)$(bindir)/phar
/php-5.3.2/ext/sqlite/libsqlite/src/parse.c: /php-5.3.2/ext/sqlite/libsqlite/src/parse.y
	@$(LEMON) /php-5.3.2/ext/sqlite/libsqlite/src/parse.y 

/php-5.3.2/ext/standard/var_unserializer.c: /php-5.3.2/ext/standard/var_unserializer.re
	@(cd $(top_srcdir); $(RE2C) -b -o ext/standard/var_unserializer.c ext/standard/var_unserializer.re)

/php-5.3.2/ext/standard/url_scanner_ex.c: /php-5.3.2/ext/standard/url_scanner_ex.re
	@(cd $(top_srcdir); $(RE2C) -b -o ext/standard/url_scanner_ex.c	ext/standard/url_scanner_ex.re)

ext/standard/info.lo: ext/standard/../../main/build-defs.h

ext/standard/basic_functions.lo: $(top_srcdir)/Zend/zend_language_parser.h
$(top_srcdir)/Zend/zend_language_parser.c:
$(top_srcdir)/Zend/zend_language_scanner.c:
ext/tokenizer/tokenizer.lo: $(top_srcdir)/Zend/zend_language_parser.c $(top_srcdir)/Zend/zend_language_scanner.c

#
# Build environment install
#

phpincludedir = $(includedir)/php
phpbuilddir = $(libdir)/build

BUILD_FILES = \
	scripts/phpize.m4 \
	build/mkdep.awk \
	build/scan_makefile_in.awk \
	build/libtool.m4 \
	Makefile.global \
	acinclude.m4 \
	ltmain.sh \
	run-tests.php

BUILD_FILES_EXEC = \
	build/shtool \
	config.guess \
	config.sub

bin_SCRIPTS = phpize php-config
man_PAGES = phpize php-config

install-build:
	@echo "Installing build environment:     $(INSTALL_ROOT)$(phpbuilddir)/"
	@$(mkinstalldirs) $(INSTALL_ROOT)$(phpbuilddir) $(INSTALL_ROOT)$(bindir) && \
	(cd $(top_srcdir) && \
	$(INSTALL) $(BUILD_FILES_EXEC) $(INSTALL_ROOT)$(phpbuilddir) && \
	$(INSTALL_DATA) $(BUILD_FILES) $(INSTALL_ROOT)$(phpbuilddir))

install-programs: scripts/phpize scripts/php-config
	@echo "Installing helper programs:       $(INSTALL_ROOT)$(bindir)/"
	@for prog in $(bin_SCRIPTS); do \
		echo "  program: $(program_prefix)$${prog}$(program_suffix)"; \
		$(INSTALL) -m 755 scripts/$${prog} $(INSTALL_ROOT)$(bindir)/$(program_prefix)$${prog}$(program_suffix); \
	done
	@echo "Installing man pages:             $(INSTALL_ROOT)$(mandir)/man1/"
	@$(mkinstalldirs) $(INSTALL_ROOT)$(mandir)/man1
	@for page in $(man_PAGES); do \
		echo "  page: $(program_prefix)$${page}$(program_suffix).1"; \
		$(INSTALL_DATA) scripts/man1/$${page}.1 $(INSTALL_ROOT)$(mandir)/man1/$(program_prefix)$${page}$(program_suffix).1; \
	done
	
scripts/phpize: /php-5.3.2/scripts/phpize.in $(top_builddir)/config.status
	(CONFIG_FILES=$@ CONFIG_HEADERS= $(top_builddir)/config.status)

scripts/php-config: /php-5.3.2/scripts/php-config.in $(top_builddir)/config.status
	(CONFIG_FILES=$@ CONFIG_HEADERS= $(top_builddir)/config.status)

#
# Zend
#

Zend/zend_language_scanner.lo: /php-5.3.2/Zend/zend_language_parser.h
Zend/zend_ini_scanner.lo: /php-5.3.2/Zend/zend_ini_parser.h

/php-5.3.2/Zend/zend_language_scanner.c: /php-5.3.2/Zend/zend_language_scanner.l
	@(cd $(top_srcdir); $(RE2C) $(RE2C_FLAGS) --case-inverted -cbdFt Zend/zend_language_scanner_defs.h -oZend/zend_language_scanner.c Zend/zend_language_scanner.l)

/php-5.3.2/Zend/zend_language_parser.h: /php-5.3.2/Zend/zend_language_parser.c
/php-5.3.2/Zend/zend_language_parser.c: /php-5.3.2/Zend/zend_language_parser.y
	@$(YACC) -p zend -v -d /php-5.3.2/Zend/zend_language_parser.y -o $@

/php-5.3.2/Zend/zend_ini_parser.h: /php-5.3.2/Zend/zend_ini_parser.c
/php-5.3.2/Zend/zend_ini_parser.c: /php-5.3.2/Zend/zend_ini_parser.y
	@$(YACC) -p ini_ -v -d /php-5.3.2/Zend/zend_ini_parser.y -o $@

/php-5.3.2/Zend/zend_ini_scanner.c: /php-5.3.2/Zend/zend_ini_scanner.l
	@(cd $(top_srcdir); $(RE2C) $(RE2C_FLAGS) --case-inverted -cbdFt Zend/zend_ini_scanner_defs.h -oZend/zend_ini_scanner.c Zend/zend_ini_scanner.l)

Zend/zend_indent.lo Zend/zend_highlight.lo Zend/zend_compile.lo: /php-5.3.2/Zend/zend_language_parser.h
Zend/zend_execute.lo: /php-5.3.2/Zend/zend_vm_execute.h /php-5.3.2/Zend/zend_vm_opcodes.h
sapi/cgi/cgi_main.lo: /php-5.3.2/sapi/cgi/cgi_main.c
	$(LIBTOOL) --mode=compile $(CC)  -Isapi/cgi/ -I/php-5.3.2/sapi/cgi/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/sapi/cgi/cgi_main.c -o sapi/cgi/cgi_main.lo 
sapi/cgi/fastcgi.lo: /php-5.3.2/sapi/cgi/fastcgi.c
	$(LIBTOOL) --mode=compile $(CC)  -Isapi/cgi/ -I/php-5.3.2/sapi/cgi/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/sapi/cgi/fastcgi.c -o sapi/cgi/fastcgi.lo 
ext/date/php_date.lo: /php-5.3.2/ext/date/php_date.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/php_date.c -o ext/date/php_date.lo 
ext/date/lib/astro.lo: /php-5.3.2/ext/date/lib/astro.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/astro.c -o ext/date/lib/astro.lo 
ext/date/lib/dow.lo: /php-5.3.2/ext/date/lib/dow.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/dow.c -o ext/date/lib/dow.lo 
ext/date/lib/parse_date.lo: /php-5.3.2/ext/date/lib/parse_date.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/parse_date.c -o ext/date/lib/parse_date.lo 
ext/date/lib/parse_tz.lo: /php-5.3.2/ext/date/lib/parse_tz.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/parse_tz.c -o ext/date/lib/parse_tz.lo 
ext/date/lib/timelib.lo: /php-5.3.2/ext/date/lib/timelib.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/timelib.c -o ext/date/lib/timelib.lo 
ext/date/lib/tm2unixtime.lo: /php-5.3.2/ext/date/lib/tm2unixtime.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/tm2unixtime.c -o ext/date/lib/tm2unixtime.lo 
ext/date/lib/unixtime2tm.lo: /php-5.3.2/ext/date/lib/unixtime2tm.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/unixtime2tm.c -o ext/date/lib/unixtime2tm.lo 
ext/date/lib/parse_iso_intervals.lo: /php-5.3.2/ext/date/lib/parse_iso_intervals.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/parse_iso_intervals.c -o ext/date/lib/parse_iso_intervals.lo 
ext/date/lib/interval.lo: /php-5.3.2/ext/date/lib/interval.c
	$(LIBTOOL) --mode=compile $(CC) -Iext/date/lib -Iext/date/ -I/php-5.3.2/ext/date/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/date/lib/interval.c -o ext/date/lib/interval.lo 
ext/ereg/ereg.lo: /php-5.3.2/ext/ereg/ereg.c
	$(LIBTOOL) --mode=compile $(CC) -Dregexec=php_regexec -Dregerror=php_regerror -Dregfree=php_regfree -Dregcomp=php_regcomp -Iext/ereg/ -I/php-5.3.2/ext/ereg/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/ereg/ereg.c -o ext/ereg/ereg.lo 
ext/ereg/regex/regcomp.lo: /php-5.3.2/ext/ereg/regex/regcomp.c
	$(LIBTOOL) --mode=compile $(CC) -Dregexec=php_regexec -Dregerror=php_regerror -Dregfree=php_regfree -Dregcomp=php_regcomp -Iext/ereg/ -I/php-5.3.2/ext/ereg/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/ereg/regex/regcomp.c -o ext/ereg/regex/regcomp.lo 
ext/ereg/regex/regexec.lo: /php-5.3.2/ext/ereg/regex/regexec.c
	$(LIBTOOL) --mode=compile $(CC) -Dregexec=php_regexec -Dregerror=php_regerror -Dregfree=php_regfree -Dregcomp=php_regcomp -Iext/ereg/ -I/php-5.3.2/ext/ereg/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/ereg/regex/regexec.c -o ext/ereg/regex/regexec.lo 
ext/ereg/regex/regerror.lo: /php-5.3.2/ext/ereg/regex/regerror.c
	$(LIBTOOL) --mode=compile $(CC) -Dregexec=php_regexec -Dregerror=php_regerror -Dregfree=php_regfree -Dregcomp=php_regcomp -Iext/ereg/ -I/php-5.3.2/ext/ereg/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/ereg/regex/regerror.c -o ext/ereg/regex/regerror.lo 
ext/ereg/regex/regfree.lo: /php-5.3.2/ext/ereg/regex/regfree.c
	$(LIBTOOL) --mode=compile $(CC) -Dregexec=php_regexec -Dregerror=php_regerror -Dregfree=php_regfree -Dregcomp=php_regcomp -Iext/ereg/ -I/php-5.3.2/ext/ereg/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/ereg/regex/regfree.c -o ext/ereg/regex/regfree.lo 
ext/pcre/pcrelib/pcre_chartables.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_chartables.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_chartables.c -o ext/pcre/pcrelib/pcre_chartables.lo 
ext/pcre/pcrelib/pcre_ucd.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_ucd.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_ucd.c -o ext/pcre/pcrelib/pcre_ucd.lo 
ext/pcre/pcrelib/pcre_compile.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_compile.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_compile.c -o ext/pcre/pcrelib/pcre_compile.lo 
ext/pcre/pcrelib/pcre_config.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_config.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_config.c -o ext/pcre/pcrelib/pcre_config.lo 
ext/pcre/pcrelib/pcre_exec.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_exec.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_exec.c -o ext/pcre/pcrelib/pcre_exec.lo 
ext/pcre/pcrelib/pcre_fullinfo.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_fullinfo.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_fullinfo.c -o ext/pcre/pcrelib/pcre_fullinfo.lo 
ext/pcre/pcrelib/pcre_get.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_get.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_get.c -o ext/pcre/pcrelib/pcre_get.lo 
ext/pcre/pcrelib/pcre_globals.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_globals.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_globals.c -o ext/pcre/pcrelib/pcre_globals.lo 
ext/pcre/pcrelib/pcre_info.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_info.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_info.c -o ext/pcre/pcrelib/pcre_info.lo 
ext/pcre/pcrelib/pcre_maketables.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_maketables.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_maketables.c -o ext/pcre/pcrelib/pcre_maketables.lo 
ext/pcre/pcrelib/pcre_newline.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_newline.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_newline.c -o ext/pcre/pcrelib/pcre_newline.lo 
ext/pcre/pcrelib/pcre_ord2utf8.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_ord2utf8.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_ord2utf8.c -o ext/pcre/pcrelib/pcre_ord2utf8.lo 
ext/pcre/pcrelib/pcre_refcount.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_refcount.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_refcount.c -o ext/pcre/pcrelib/pcre_refcount.lo 
ext/pcre/pcrelib/pcre_study.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_study.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_study.c -o ext/pcre/pcrelib/pcre_study.lo 
ext/pcre/pcrelib/pcre_tables.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_tables.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_tables.c -o ext/pcre/pcrelib/pcre_tables.lo 
ext/pcre/pcrelib/pcre_try_flipped.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_try_flipped.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_try_flipped.c -o ext/pcre/pcrelib/pcre_try_flipped.lo 
ext/pcre/pcrelib/pcre_valid_utf8.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_valid_utf8.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_valid_utf8.c -o ext/pcre/pcrelib/pcre_valid_utf8.lo 
ext/pcre/pcrelib/pcre_version.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_version.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_version.c -o ext/pcre/pcrelib/pcre_version.lo 
ext/pcre/pcrelib/pcre_xclass.lo: /php-5.3.2/ext/pcre/pcrelib/pcre_xclass.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/pcrelib/pcre_xclass.c -o ext/pcre/pcrelib/pcre_xclass.lo 
ext/pcre/php_pcre.lo: /php-5.3.2/ext/pcre/php_pcre.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/pcre/pcrelib -Iext/pcre/ -I/php-5.3.2/ext/pcre/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pcre/php_pcre.c -o ext/pcre/php_pcre.lo 
ext/sqlite3/sqlite3.lo: /php-5.3.2/ext/sqlite3/sqlite3.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite3/libsqlite -DSQLITE_ENABLE_FTS3=1 -DSQLITE_CORE=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_THREADSAFE=0  -Iext/sqlite3/ -I/php-5.3.2/ext/sqlite3/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite3/sqlite3.c -o ext/sqlite3/sqlite3.lo 
ext/sqlite3/libsqlite/sqlite3.lo: /php-5.3.2/ext/sqlite3/libsqlite/sqlite3.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite3/libsqlite -DSQLITE_ENABLE_FTS3=1 -DSQLITE_CORE=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_THREADSAFE=0  -Iext/sqlite3/ -I/php-5.3.2/ext/sqlite3/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite3/libsqlite/sqlite3.c -o ext/sqlite3/libsqlite/sqlite3.lo 
ext/ctype/ctype.lo: /php-5.3.2/ext/ctype/ctype.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/ctype/ -I/php-5.3.2/ext/ctype/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/ctype/ctype.c -o ext/ctype/ctype.lo 
ext/fileinfo/fileinfo.lo: /php-5.3.2/ext/fileinfo/fileinfo.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/fileinfo.c -o ext/fileinfo/fileinfo.lo 
ext/fileinfo/libmagic/apprentice.lo: /php-5.3.2/ext/fileinfo/libmagic/apprentice.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/apprentice.c -o ext/fileinfo/libmagic/apprentice.lo 
ext/fileinfo/libmagic/apptype.lo: /php-5.3.2/ext/fileinfo/libmagic/apptype.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/apptype.c -o ext/fileinfo/libmagic/apptype.lo 
ext/fileinfo/libmagic/ascmagic.lo: /php-5.3.2/ext/fileinfo/libmagic/ascmagic.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/ascmagic.c -o ext/fileinfo/libmagic/ascmagic.lo 
ext/fileinfo/libmagic/cdf.lo: /php-5.3.2/ext/fileinfo/libmagic/cdf.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/cdf.c -o ext/fileinfo/libmagic/cdf.lo 
ext/fileinfo/libmagic/cdf_time.lo: /php-5.3.2/ext/fileinfo/libmagic/cdf_time.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/cdf_time.c -o ext/fileinfo/libmagic/cdf_time.lo 
ext/fileinfo/libmagic/compress.lo: /php-5.3.2/ext/fileinfo/libmagic/compress.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/compress.c -o ext/fileinfo/libmagic/compress.lo 
ext/fileinfo/libmagic/encoding.lo: /php-5.3.2/ext/fileinfo/libmagic/encoding.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/encoding.c -o ext/fileinfo/libmagic/encoding.lo 
ext/fileinfo/libmagic/fsmagic.lo: /php-5.3.2/ext/fileinfo/libmagic/fsmagic.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/fsmagic.c -o ext/fileinfo/libmagic/fsmagic.lo 
ext/fileinfo/libmagic/funcs.lo: /php-5.3.2/ext/fileinfo/libmagic/funcs.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/funcs.c -o ext/fileinfo/libmagic/funcs.lo 
ext/fileinfo/libmagic/is_tar.lo: /php-5.3.2/ext/fileinfo/libmagic/is_tar.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/is_tar.c -o ext/fileinfo/libmagic/is_tar.lo 
ext/fileinfo/libmagic/magic.lo: /php-5.3.2/ext/fileinfo/libmagic/magic.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/magic.c -o ext/fileinfo/libmagic/magic.lo 
ext/fileinfo/libmagic/print.lo: /php-5.3.2/ext/fileinfo/libmagic/print.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/print.c -o ext/fileinfo/libmagic/print.lo 
ext/fileinfo/libmagic/readcdf.lo: /php-5.3.2/ext/fileinfo/libmagic/readcdf.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/readcdf.c -o ext/fileinfo/libmagic/readcdf.lo 
ext/fileinfo/libmagic/readelf.lo: /php-5.3.2/ext/fileinfo/libmagic/readelf.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/readelf.c -o ext/fileinfo/libmagic/readelf.lo 
ext/fileinfo/libmagic/softmagic.lo: /php-5.3.2/ext/fileinfo/libmagic/softmagic.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/fileinfo/libmagic -Iext/fileinfo/ -I/php-5.3.2/ext/fileinfo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/fileinfo/libmagic/softmagic.c -o ext/fileinfo/libmagic/softmagic.lo 
ext/filter/filter.lo: /php-5.3.2/ext/filter/filter.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/filter/ -I/php-5.3.2/ext/filter/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/filter/filter.c -o ext/filter/filter.lo 
ext/filter/sanitizing_filters.lo: /php-5.3.2/ext/filter/sanitizing_filters.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/filter/ -I/php-5.3.2/ext/filter/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/filter/sanitizing_filters.c -o ext/filter/sanitizing_filters.lo 
ext/filter/logical_filters.lo: /php-5.3.2/ext/filter/logical_filters.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/filter/ -I/php-5.3.2/ext/filter/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/filter/logical_filters.c -o ext/filter/logical_filters.lo 
ext/filter/callback_filter.lo: /php-5.3.2/ext/filter/callback_filter.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/filter/ -I/php-5.3.2/ext/filter/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/filter/callback_filter.c -o ext/filter/callback_filter.lo 
ext/hash/hash.lo: /php-5.3.2/ext/hash/hash.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash.c -o ext/hash/hash.lo 
ext/hash/hash_md.lo: /php-5.3.2/ext/hash/hash_md.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_md.c -o ext/hash/hash_md.lo 
ext/hash/hash_sha.lo: /php-5.3.2/ext/hash/hash_sha.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_sha.c -o ext/hash/hash_sha.lo 
ext/hash/hash_ripemd.lo: /php-5.3.2/ext/hash/hash_ripemd.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_ripemd.c -o ext/hash/hash_ripemd.lo 
ext/hash/hash_haval.lo: /php-5.3.2/ext/hash/hash_haval.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_haval.c -o ext/hash/hash_haval.lo 
ext/hash/hash_tiger.lo: /php-5.3.2/ext/hash/hash_tiger.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_tiger.c -o ext/hash/hash_tiger.lo 
ext/hash/hash_gost.lo: /php-5.3.2/ext/hash/hash_gost.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_gost.c -o ext/hash/hash_gost.lo 
ext/hash/hash_snefru.lo: /php-5.3.2/ext/hash/hash_snefru.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_snefru.c -o ext/hash/hash_snefru.lo 
ext/hash/hash_whirlpool.lo: /php-5.3.2/ext/hash/hash_whirlpool.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_whirlpool.c -o ext/hash/hash_whirlpool.lo 
ext/hash/hash_adler32.lo: /php-5.3.2/ext/hash/hash_adler32.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_adler32.c -o ext/hash/hash_adler32.lo 
ext/hash/hash_crc32.lo: /php-5.3.2/ext/hash/hash_crc32.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_crc32.c -o ext/hash/hash_crc32.lo 
ext/hash/hash_salsa.lo: /php-5.3.2/ext/hash/hash_salsa.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/hash/ -I/php-5.3.2/ext/hash/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/hash/hash_salsa.c -o ext/hash/hash_salsa.lo 
ext/json/json.lo: /php-5.3.2/ext/json/json.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/json/ -I/php-5.3.2/ext/json/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/json/json.c -o ext/json/json.lo 
ext/json/utf8_to_utf16.lo: /php-5.3.2/ext/json/utf8_to_utf16.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/json/ -I/php-5.3.2/ext/json/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/json/utf8_to_utf16.c -o ext/json/utf8_to_utf16.lo 
ext/json/utf8_decode.lo: /php-5.3.2/ext/json/utf8_decode.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/json/ -I/php-5.3.2/ext/json/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/json/utf8_decode.c -o ext/json/utf8_decode.lo 
ext/json/JSON_parser.lo: /php-5.3.2/ext/json/JSON_parser.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/json/ -I/php-5.3.2/ext/json/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/json/JSON_parser.c -o ext/json/JSON_parser.lo 
ext/pdo/pdo.lo: /php-5.3.2/ext/pdo/pdo.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/pdo/ -I/php-5.3.2/ext/pdo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo/pdo.c -o ext/pdo/pdo.lo 
ext/pdo/pdo_dbh.lo: /php-5.3.2/ext/pdo/pdo_dbh.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/pdo/ -I/php-5.3.2/ext/pdo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo/pdo_dbh.c -o ext/pdo/pdo_dbh.lo 
ext/pdo/pdo_stmt.lo: /php-5.3.2/ext/pdo/pdo_stmt.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/pdo/ -I/php-5.3.2/ext/pdo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo/pdo_stmt.c -o ext/pdo/pdo_stmt.lo 
ext/pdo/pdo_sql_parser.lo: /php-5.3.2/ext/pdo/pdo_sql_parser.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/pdo/ -I/php-5.3.2/ext/pdo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo/pdo_sql_parser.c -o ext/pdo/pdo_sql_parser.lo 
ext/pdo/pdo_sqlstate.lo: /php-5.3.2/ext/pdo/pdo_sqlstate.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/pdo/ -I/php-5.3.2/ext/pdo/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo/pdo_sqlstate.c -o ext/pdo/pdo_sqlstate.lo 
ext/pdo_sqlite/pdo_sqlite.lo: /php-5.3.2/ext/pdo_sqlite/pdo_sqlite.c
	$(LIBTOOL) --mode=compile $(CC) -DPDO_SQLITE_BUNDLED=1 -DSQLITE_ENABLE_FTS3=1 -DSQLITE_CORE=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_THREADSAFE=0 -I/php-5.3.2/ext -Iext/pdo_sqlite/ -I/php-5.3.2/ext/pdo_sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo_sqlite/pdo_sqlite.c -o ext/pdo_sqlite/pdo_sqlite.lo 
ext/pdo_sqlite/sqlite_driver.lo: /php-5.3.2/ext/pdo_sqlite/sqlite_driver.c
	$(LIBTOOL) --mode=compile $(CC) -DPDO_SQLITE_BUNDLED=1 -DSQLITE_ENABLE_FTS3=1 -DSQLITE_CORE=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_THREADSAFE=0 -I/php-5.3.2/ext -Iext/pdo_sqlite/ -I/php-5.3.2/ext/pdo_sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo_sqlite/sqlite_driver.c -o ext/pdo_sqlite/sqlite_driver.lo 
ext/pdo_sqlite/sqlite_statement.lo: /php-5.3.2/ext/pdo_sqlite/sqlite_statement.c
	$(LIBTOOL) --mode=compile $(CC) -DPDO_SQLITE_BUNDLED=1 -DSQLITE_ENABLE_FTS3=1 -DSQLITE_CORE=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 -DSQLITE_THREADSAFE=0 -I/php-5.3.2/ext -Iext/pdo_sqlite/ -I/php-5.3.2/ext/pdo_sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/pdo_sqlite/sqlite_statement.c -o ext/pdo_sqlite/sqlite_statement.lo 
ext/phar/util.lo: /php-5.3.2/ext/phar/util.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/util.c -o ext/phar/util.lo 
ext/phar/tar.lo: /php-5.3.2/ext/phar/tar.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/tar.c -o ext/phar/tar.lo 
ext/phar/zip.lo: /php-5.3.2/ext/phar/zip.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/zip.c -o ext/phar/zip.lo 
ext/phar/stream.lo: /php-5.3.2/ext/phar/stream.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/stream.c -o ext/phar/stream.lo 
ext/phar/func_interceptors.lo: /php-5.3.2/ext/phar/func_interceptors.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/func_interceptors.c -o ext/phar/func_interceptors.lo 
ext/phar/dirstream.lo: /php-5.3.2/ext/phar/dirstream.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/dirstream.c -o ext/phar/dirstream.lo 
ext/phar/phar.lo: /php-5.3.2/ext/phar/phar.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/phar.c -o ext/phar/phar.lo 
ext/phar/phar_object.lo: /php-5.3.2/ext/phar/phar_object.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/phar_object.c -o ext/phar/phar_object.lo 
ext/phar/phar_path_check.lo: /php-5.3.2/ext/phar/phar_path_check.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/phar/ -I/php-5.3.2/ext/phar/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/phar/phar_path_check.c -o ext/phar/phar_path_check.lo 
ext/posix/posix.lo: /php-5.3.2/ext/posix/posix.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/posix/ -I/php-5.3.2/ext/posix/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/posix/posix.c -o ext/posix/posix.lo 
ext/reflection/php_reflection.lo: /php-5.3.2/ext/reflection/php_reflection.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/reflection/ -I/php-5.3.2/ext/reflection/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/reflection/php_reflection.c -o ext/reflection/php_reflection.lo 
ext/session/session.lo: /php-5.3.2/ext/session/session.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/session/ -I/php-5.3.2/ext/session/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/session/session.c -o ext/session/session.lo 
ext/session/mod_files.lo: /php-5.3.2/ext/session/mod_files.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/session/ -I/php-5.3.2/ext/session/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/session/mod_files.c -o ext/session/mod_files.lo 
ext/session/mod_mm.lo: /php-5.3.2/ext/session/mod_mm.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/session/ -I/php-5.3.2/ext/session/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/session/mod_mm.c -o ext/session/mod_mm.lo 
ext/session/mod_user.lo: /php-5.3.2/ext/session/mod_user.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/session/ -I/php-5.3.2/ext/session/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/session/mod_user.c -o ext/session/mod_user.lo 
ext/spl/php_spl.lo: /php-5.3.2/ext/spl/php_spl.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/php_spl.c -o ext/spl/php_spl.lo 
ext/spl/spl_functions.lo: /php-5.3.2/ext/spl/spl_functions.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_functions.c -o ext/spl/spl_functions.lo 
ext/spl/spl_engine.lo: /php-5.3.2/ext/spl/spl_engine.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_engine.c -o ext/spl/spl_engine.lo 
ext/spl/spl_iterators.lo: /php-5.3.2/ext/spl/spl_iterators.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_iterators.c -o ext/spl/spl_iterators.lo 
ext/spl/spl_array.lo: /php-5.3.2/ext/spl/spl_array.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_array.c -o ext/spl/spl_array.lo 
ext/spl/spl_directory.lo: /php-5.3.2/ext/spl/spl_directory.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_directory.c -o ext/spl/spl_directory.lo 
ext/spl/spl_exceptions.lo: /php-5.3.2/ext/spl/spl_exceptions.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_exceptions.c -o ext/spl/spl_exceptions.lo 
ext/spl/spl_observer.lo: /php-5.3.2/ext/spl/spl_observer.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_observer.c -o ext/spl/spl_observer.lo 
ext/spl/spl_dllist.lo: /php-5.3.2/ext/spl/spl_dllist.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_dllist.c -o ext/spl/spl_dllist.lo 
ext/spl/spl_heap.lo: /php-5.3.2/ext/spl/spl_heap.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_heap.c -o ext/spl/spl_heap.lo 
ext/spl/spl_fixedarray.lo: /php-5.3.2/ext/spl/spl_fixedarray.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/spl/ -I/php-5.3.2/ext/spl/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/spl/spl_fixedarray.c -o ext/spl/spl_fixedarray.lo 
ext/sqlite/sqlite.lo: /php-5.3.2/ext/sqlite/sqlite.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/sqlite.c -o ext/sqlite/sqlite.lo 
ext/sqlite/sess_sqlite.lo: /php-5.3.2/ext/sqlite/sess_sqlite.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/sess_sqlite.c -o ext/sqlite/sess_sqlite.lo 
ext/sqlite/pdo_sqlite2.lo: /php-5.3.2/ext/sqlite/pdo_sqlite2.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/pdo_sqlite2.c -o ext/sqlite/pdo_sqlite2.lo 
ext/sqlite/libsqlite/src/opcodes.lo: /php-5.3.2/ext/sqlite/libsqlite/src/opcodes.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/opcodes.c -o ext/sqlite/libsqlite/src/opcodes.lo 
ext/sqlite/libsqlite/src/parse.lo: /php-5.3.2/ext/sqlite/libsqlite/src/parse.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/parse.c -o ext/sqlite/libsqlite/src/parse.lo 
ext/sqlite/libsqlite/src/encode.lo: /php-5.3.2/ext/sqlite/libsqlite/src/encode.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/encode.c -o ext/sqlite/libsqlite/src/encode.lo 
ext/sqlite/libsqlite/src/auth.lo: /php-5.3.2/ext/sqlite/libsqlite/src/auth.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/auth.c -o ext/sqlite/libsqlite/src/auth.lo 
ext/sqlite/libsqlite/src/btree.lo: /php-5.3.2/ext/sqlite/libsqlite/src/btree.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/btree.c -o ext/sqlite/libsqlite/src/btree.lo 
ext/sqlite/libsqlite/src/build.lo: /php-5.3.2/ext/sqlite/libsqlite/src/build.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/build.c -o ext/sqlite/libsqlite/src/build.lo 
ext/sqlite/libsqlite/src/delete.lo: /php-5.3.2/ext/sqlite/libsqlite/src/delete.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/delete.c -o ext/sqlite/libsqlite/src/delete.lo 
ext/sqlite/libsqlite/src/expr.lo: /php-5.3.2/ext/sqlite/libsqlite/src/expr.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/expr.c -o ext/sqlite/libsqlite/src/expr.lo 
ext/sqlite/libsqlite/src/func.lo: /php-5.3.2/ext/sqlite/libsqlite/src/func.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/func.c -o ext/sqlite/libsqlite/src/func.lo 
ext/sqlite/libsqlite/src/hash.lo: /php-5.3.2/ext/sqlite/libsqlite/src/hash.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/hash.c -o ext/sqlite/libsqlite/src/hash.lo 
ext/sqlite/libsqlite/src/insert.lo: /php-5.3.2/ext/sqlite/libsqlite/src/insert.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/insert.c -o ext/sqlite/libsqlite/src/insert.lo 
ext/sqlite/libsqlite/src/main.lo: /php-5.3.2/ext/sqlite/libsqlite/src/main.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/main.c -o ext/sqlite/libsqlite/src/main.lo 
ext/sqlite/libsqlite/src/os.lo: /php-5.3.2/ext/sqlite/libsqlite/src/os.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/os.c -o ext/sqlite/libsqlite/src/os.lo 
ext/sqlite/libsqlite/src/pager.lo: /php-5.3.2/ext/sqlite/libsqlite/src/pager.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/pager.c -o ext/sqlite/libsqlite/src/pager.lo 
ext/sqlite/libsqlite/src/printf.lo: /php-5.3.2/ext/sqlite/libsqlite/src/printf.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/printf.c -o ext/sqlite/libsqlite/src/printf.lo 
ext/sqlite/libsqlite/src/random.lo: /php-5.3.2/ext/sqlite/libsqlite/src/random.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/random.c -o ext/sqlite/libsqlite/src/random.lo 
ext/sqlite/libsqlite/src/select.lo: /php-5.3.2/ext/sqlite/libsqlite/src/select.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/select.c -o ext/sqlite/libsqlite/src/select.lo 
ext/sqlite/libsqlite/src/table.lo: /php-5.3.2/ext/sqlite/libsqlite/src/table.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/table.c -o ext/sqlite/libsqlite/src/table.lo 
ext/sqlite/libsqlite/src/tokenize.lo: /php-5.3.2/ext/sqlite/libsqlite/src/tokenize.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/tokenize.c -o ext/sqlite/libsqlite/src/tokenize.lo 
ext/sqlite/libsqlite/src/update.lo: /php-5.3.2/ext/sqlite/libsqlite/src/update.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/update.c -o ext/sqlite/libsqlite/src/update.lo 
ext/sqlite/libsqlite/src/util.lo: /php-5.3.2/ext/sqlite/libsqlite/src/util.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/util.c -o ext/sqlite/libsqlite/src/util.lo 
ext/sqlite/libsqlite/src/vdbe.lo: /php-5.3.2/ext/sqlite/libsqlite/src/vdbe.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/vdbe.c -o ext/sqlite/libsqlite/src/vdbe.lo 
ext/sqlite/libsqlite/src/attach.lo: /php-5.3.2/ext/sqlite/libsqlite/src/attach.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/attach.c -o ext/sqlite/libsqlite/src/attach.lo 
ext/sqlite/libsqlite/src/btree_rb.lo: /php-5.3.2/ext/sqlite/libsqlite/src/btree_rb.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/btree_rb.c -o ext/sqlite/libsqlite/src/btree_rb.lo 
ext/sqlite/libsqlite/src/pragma.lo: /php-5.3.2/ext/sqlite/libsqlite/src/pragma.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/pragma.c -o ext/sqlite/libsqlite/src/pragma.lo 
ext/sqlite/libsqlite/src/vacuum.lo: /php-5.3.2/ext/sqlite/libsqlite/src/vacuum.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/vacuum.c -o ext/sqlite/libsqlite/src/vacuum.lo 
ext/sqlite/libsqlite/src/copy.lo: /php-5.3.2/ext/sqlite/libsqlite/src/copy.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/copy.c -o ext/sqlite/libsqlite/src/copy.lo 
ext/sqlite/libsqlite/src/vdbeaux.lo: /php-5.3.2/ext/sqlite/libsqlite/src/vdbeaux.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/vdbeaux.c -o ext/sqlite/libsqlite/src/vdbeaux.lo 
ext/sqlite/libsqlite/src/date.lo: /php-5.3.2/ext/sqlite/libsqlite/src/date.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/date.c -o ext/sqlite/libsqlite/src/date.lo 
ext/sqlite/libsqlite/src/where.lo: /php-5.3.2/ext/sqlite/libsqlite/src/where.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/where.c -o ext/sqlite/libsqlite/src/where.lo 
ext/sqlite/libsqlite/src/trigger.lo: /php-5.3.2/ext/sqlite/libsqlite/src/trigger.c
	$(LIBTOOL) --mode=compile $(CC) -I/php-5.3.2/ext/sqlite/libsqlite/src -Iext/sqlite/libsqlite/src -I/php-5.3.2/ext -Iext/sqlite/ -I/php-5.3.2/ext/sqlite/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/sqlite/libsqlite/src/trigger.c -o ext/sqlite/libsqlite/src/trigger.lo 
ext/standard/crypt_freesec.lo: /php-5.3.2/ext/standard/crypt_freesec.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/crypt_freesec.c -o ext/standard/crypt_freesec.lo 
ext/standard/crypt_blowfish.lo: /php-5.3.2/ext/standard/crypt_blowfish.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/crypt_blowfish.c -o ext/standard/crypt_blowfish.lo 
ext/standard/crypt_sha512.lo: /php-5.3.2/ext/standard/crypt_sha512.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/crypt_sha512.c -o ext/standard/crypt_sha512.lo 
ext/standard/crypt_sha256.lo: /php-5.3.2/ext/standard/crypt_sha256.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/crypt_sha256.c -o ext/standard/crypt_sha256.lo 
ext/standard/php_crypt_r.lo: /php-5.3.2/ext/standard/php_crypt_r.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/php_crypt_r.c -o ext/standard/php_crypt_r.lo 
ext/standard/array.lo: /php-5.3.2/ext/standard/array.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/array.c -o ext/standard/array.lo 
ext/standard/base64.lo: /php-5.3.2/ext/standard/base64.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/base64.c -o ext/standard/base64.lo 
ext/standard/basic_functions.lo: /php-5.3.2/ext/standard/basic_functions.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/basic_functions.c -o ext/standard/basic_functions.lo 
ext/standard/browscap.lo: /php-5.3.2/ext/standard/browscap.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/browscap.c -o ext/standard/browscap.lo 
ext/standard/crc32.lo: /php-5.3.2/ext/standard/crc32.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/crc32.c -o ext/standard/crc32.lo 
ext/standard/crypt.lo: /php-5.3.2/ext/standard/crypt.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/crypt.c -o ext/standard/crypt.lo 
ext/standard/cyr_convert.lo: /php-5.3.2/ext/standard/cyr_convert.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/cyr_convert.c -o ext/standard/cyr_convert.lo 
ext/standard/datetime.lo: /php-5.3.2/ext/standard/datetime.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/datetime.c -o ext/standard/datetime.lo 
ext/standard/dir.lo: /php-5.3.2/ext/standard/dir.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/dir.c -o ext/standard/dir.lo 
ext/standard/dl.lo: /php-5.3.2/ext/standard/dl.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/dl.c -o ext/standard/dl.lo 
ext/standard/dns.lo: /php-5.3.2/ext/standard/dns.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/dns.c -o ext/standard/dns.lo 
ext/standard/exec.lo: /php-5.3.2/ext/standard/exec.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/exec.c -o ext/standard/exec.lo 
ext/standard/file.lo: /php-5.3.2/ext/standard/file.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/file.c -o ext/standard/file.lo 
ext/standard/filestat.lo: /php-5.3.2/ext/standard/filestat.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/filestat.c -o ext/standard/filestat.lo 
ext/standard/flock_compat.lo: /php-5.3.2/ext/standard/flock_compat.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/flock_compat.c -o ext/standard/flock_compat.lo 
ext/standard/formatted_print.lo: /php-5.3.2/ext/standard/formatted_print.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/formatted_print.c -o ext/standard/formatted_print.lo 
ext/standard/fsock.lo: /php-5.3.2/ext/standard/fsock.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/fsock.c -o ext/standard/fsock.lo 
ext/standard/head.lo: /php-5.3.2/ext/standard/head.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/head.c -o ext/standard/head.lo 
ext/standard/html.lo: /php-5.3.2/ext/standard/html.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/html.c -o ext/standard/html.lo 
ext/standard/image.lo: /php-5.3.2/ext/standard/image.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/image.c -o ext/standard/image.lo 
ext/standard/info.lo: /php-5.3.2/ext/standard/info.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/info.c -o ext/standard/info.lo 
ext/standard/iptc.lo: /php-5.3.2/ext/standard/iptc.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/iptc.c -o ext/standard/iptc.lo 
ext/standard/lcg.lo: /php-5.3.2/ext/standard/lcg.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/lcg.c -o ext/standard/lcg.lo 
ext/standard/link.lo: /php-5.3.2/ext/standard/link.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/link.c -o ext/standard/link.lo 
ext/standard/mail.lo: /php-5.3.2/ext/standard/mail.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/mail.c -o ext/standard/mail.lo 
ext/standard/math.lo: /php-5.3.2/ext/standard/math.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/math.c -o ext/standard/math.lo 
ext/standard/md5.lo: /php-5.3.2/ext/standard/md5.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/md5.c -o ext/standard/md5.lo 
ext/standard/metaphone.lo: /php-5.3.2/ext/standard/metaphone.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/metaphone.c -o ext/standard/metaphone.lo 
ext/standard/microtime.lo: /php-5.3.2/ext/standard/microtime.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/microtime.c -o ext/standard/microtime.lo 
ext/standard/pack.lo: /php-5.3.2/ext/standard/pack.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/pack.c -o ext/standard/pack.lo 
ext/standard/pageinfo.lo: /php-5.3.2/ext/standard/pageinfo.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/pageinfo.c -o ext/standard/pageinfo.lo 
ext/standard/quot_print.lo: /php-5.3.2/ext/standard/quot_print.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/quot_print.c -o ext/standard/quot_print.lo 
ext/standard/rand.lo: /php-5.3.2/ext/standard/rand.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/rand.c -o ext/standard/rand.lo 
ext/standard/soundex.lo: /php-5.3.2/ext/standard/soundex.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/soundex.c -o ext/standard/soundex.lo 
ext/standard/string.lo: /php-5.3.2/ext/standard/string.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/string.c -o ext/standard/string.lo 
ext/standard/scanf.lo: /php-5.3.2/ext/standard/scanf.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/scanf.c -o ext/standard/scanf.lo 
ext/standard/syslog.lo: /php-5.3.2/ext/standard/syslog.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/syslog.c -o ext/standard/syslog.lo 
ext/standard/type.lo: /php-5.3.2/ext/standard/type.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/type.c -o ext/standard/type.lo 
ext/standard/uniqid.lo: /php-5.3.2/ext/standard/uniqid.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/uniqid.c -o ext/standard/uniqid.lo 
ext/standard/url.lo: /php-5.3.2/ext/standard/url.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/url.c -o ext/standard/url.lo 
ext/standard/var.lo: /php-5.3.2/ext/standard/var.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/var.c -o ext/standard/var.lo 
ext/standard/versioning.lo: /php-5.3.2/ext/standard/versioning.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/versioning.c -o ext/standard/versioning.lo 
ext/standard/assert.lo: /php-5.3.2/ext/standard/assert.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/assert.c -o ext/standard/assert.lo 
ext/standard/strnatcmp.lo: /php-5.3.2/ext/standard/strnatcmp.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/strnatcmp.c -o ext/standard/strnatcmp.lo 
ext/standard/levenshtein.lo: /php-5.3.2/ext/standard/levenshtein.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/levenshtein.c -o ext/standard/levenshtein.lo 
ext/standard/incomplete_class.lo: /php-5.3.2/ext/standard/incomplete_class.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/incomplete_class.c -o ext/standard/incomplete_class.lo 
ext/standard/url_scanner_ex.lo: /php-5.3.2/ext/standard/url_scanner_ex.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/url_scanner_ex.c -o ext/standard/url_scanner_ex.lo 
ext/standard/ftp_fopen_wrapper.lo: /php-5.3.2/ext/standard/ftp_fopen_wrapper.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/ftp_fopen_wrapper.c -o ext/standard/ftp_fopen_wrapper.lo 
ext/standard/http_fopen_wrapper.lo: /php-5.3.2/ext/standard/http_fopen_wrapper.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/http_fopen_wrapper.c -o ext/standard/http_fopen_wrapper.lo 
ext/standard/php_fopen_wrapper.lo: /php-5.3.2/ext/standard/php_fopen_wrapper.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/php_fopen_wrapper.c -o ext/standard/php_fopen_wrapper.lo 
ext/standard/credits.lo: /php-5.3.2/ext/standard/credits.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/credits.c -o ext/standard/credits.lo 
ext/standard/css.lo: /php-5.3.2/ext/standard/css.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/css.c -o ext/standard/css.lo 
ext/standard/var_unserializer.lo: /php-5.3.2/ext/standard/var_unserializer.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/var_unserializer.c -o ext/standard/var_unserializer.lo 
ext/standard/ftok.lo: /php-5.3.2/ext/standard/ftok.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/ftok.c -o ext/standard/ftok.lo 
ext/standard/sha1.lo: /php-5.3.2/ext/standard/sha1.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/sha1.c -o ext/standard/sha1.lo 
ext/standard/user_filters.lo: /php-5.3.2/ext/standard/user_filters.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/user_filters.c -o ext/standard/user_filters.lo 
ext/standard/uuencode.lo: /php-5.3.2/ext/standard/uuencode.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/uuencode.c -o ext/standard/uuencode.lo 
ext/standard/filters.lo: /php-5.3.2/ext/standard/filters.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/filters.c -o ext/standard/filters.lo 
ext/standard/proc_open.lo: /php-5.3.2/ext/standard/proc_open.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/proc_open.c -o ext/standard/proc_open.lo 
ext/standard/streamsfuncs.lo: /php-5.3.2/ext/standard/streamsfuncs.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/streamsfuncs.c -o ext/standard/streamsfuncs.lo 
ext/standard/http.lo: /php-5.3.2/ext/standard/http.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/standard/ -I/php-5.3.2/ext/standard/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/standard/http.c -o ext/standard/http.lo 
ext/tokenizer/tokenizer.lo: /php-5.3.2/ext/tokenizer/tokenizer.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/tokenizer/ -I/php-5.3.2/ext/tokenizer/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/tokenizer/tokenizer.c -o ext/tokenizer/tokenizer.lo 
ext/tokenizer/tokenizer_data.lo: /php-5.3.2/ext/tokenizer/tokenizer_data.c
	$(LIBTOOL) --mode=compile $(CC)  -Iext/tokenizer/ -I/php-5.3.2/ext/tokenizer/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/ext/tokenizer/tokenizer_data.c -o ext/tokenizer/tokenizer_data.lo 
sapi/cli/php_cli.lo: /php-5.3.2/sapi/cli/php_cli.c
	$(LIBTOOL) --mode=compile $(CC)  -Isapi/cli/ -I/php-5.3.2/sapi/cli/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/sapi/cli/php_cli.c -o sapi/cli/php_cli.lo 
sapi/cli/php_cli_readline.lo: /php-5.3.2/sapi/cli/php_cli_readline.c
	$(LIBTOOL) --mode=compile $(CC)  -Isapi/cli/ -I/php-5.3.2/sapi/cli/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/sapi/cli/php_cli_readline.c -o sapi/cli/php_cli_readline.lo 
TSRM/TSRM.lo: /php-5.3.2/TSRM/TSRM.c
	$(LIBTOOL) --mode=compile $(CC)  -ITSRM/ -I/php-5.3.2/TSRM/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/TSRM/TSRM.c -o TSRM/TSRM.lo 
TSRM/tsrm_strtok_r.lo: /php-5.3.2/TSRM/tsrm_strtok_r.c
	$(LIBTOOL) --mode=compile $(CC)  -ITSRM/ -I/php-5.3.2/TSRM/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/TSRM/tsrm_strtok_r.c -o TSRM/tsrm_strtok_r.lo 
TSRM/tsrm_virtual_cwd.lo: /php-5.3.2/TSRM/tsrm_virtual_cwd.c
	$(LIBTOOL) --mode=compile $(CC)  -ITSRM/ -I/php-5.3.2/TSRM/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/TSRM/tsrm_virtual_cwd.c -o TSRM/tsrm_virtual_cwd.lo 
main/main.lo: /php-5.3.2/main/main.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/main.c -o main/main.lo 
main/snprintf.lo: /php-5.3.2/main/snprintf.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/snprintf.c -o main/snprintf.lo 
main/spprintf.lo: /php-5.3.2/main/spprintf.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/spprintf.c -o main/spprintf.lo 
main/php_sprintf.lo: /php-5.3.2/main/php_sprintf.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_sprintf.c -o main/php_sprintf.lo 
main/safe_mode.lo: /php-5.3.2/main/safe_mode.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/safe_mode.c -o main/safe_mode.lo 
main/fopen_wrappers.lo: /php-5.3.2/main/fopen_wrappers.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/fopen_wrappers.c -o main/fopen_wrappers.lo 
main/alloca.lo: /php-5.3.2/main/alloca.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/alloca.c -o main/alloca.lo 
main/php_scandir.lo: /php-5.3.2/main/php_scandir.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_scandir.c -o main/php_scandir.lo 
main/php_ini.lo: /php-5.3.2/main/php_ini.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_ini.c -o main/php_ini.lo 
main/SAPI.lo: /php-5.3.2/main/SAPI.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/SAPI.c -o main/SAPI.lo 
main/rfc1867.lo: /php-5.3.2/main/rfc1867.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/rfc1867.c -o main/rfc1867.lo 
main/php_content_types.lo: /php-5.3.2/main/php_content_types.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_content_types.c -o main/php_content_types.lo 
main/strlcpy.lo: /php-5.3.2/main/strlcpy.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/strlcpy.c -o main/strlcpy.lo 
main/strlcat.lo: /php-5.3.2/main/strlcat.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/strlcat.c -o main/strlcat.lo 
main/mergesort.lo: /php-5.3.2/main/mergesort.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/mergesort.c -o main/mergesort.lo 
main/reentrancy.lo: /php-5.3.2/main/reentrancy.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/reentrancy.c -o main/reentrancy.lo 
main/php_variables.lo: /php-5.3.2/main/php_variables.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_variables.c -o main/php_variables.lo 
main/php_ticks.lo: /php-5.3.2/main/php_ticks.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_ticks.c -o main/php_ticks.lo 
main/network.lo: /php-5.3.2/main/network.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/network.c -o main/network.lo 
main/php_open_temporary_file.lo: /php-5.3.2/main/php_open_temporary_file.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_open_temporary_file.c -o main/php_open_temporary_file.lo 
main/php_logos.lo: /php-5.3.2/main/php_logos.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/php_logos.c -o main/php_logos.lo 
main/output.lo: /php-5.3.2/main/output.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/output.c -o main/output.lo 
main/getopt.lo: /php-5.3.2/main/getopt.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/getopt.c -o main/getopt.lo 
main/streams/streams.lo: /php-5.3.2/main/streams/streams.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/streams.c -o main/streams/streams.lo 
main/streams/cast.lo: /php-5.3.2/main/streams/cast.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/cast.c -o main/streams/cast.lo 
main/streams/memory.lo: /php-5.3.2/main/streams/memory.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/memory.c -o main/streams/memory.lo 
main/streams/filter.lo: /php-5.3.2/main/streams/filter.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/filter.c -o main/streams/filter.lo 
main/streams/plain_wrapper.lo: /php-5.3.2/main/streams/plain_wrapper.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/plain_wrapper.c -o main/streams/plain_wrapper.lo 
main/streams/userspace.lo: /php-5.3.2/main/streams/userspace.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/userspace.c -o main/streams/userspace.lo 
main/streams/transports.lo: /php-5.3.2/main/streams/transports.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/transports.c -o main/streams/transports.lo 
main/streams/xp_socket.lo: /php-5.3.2/main/streams/xp_socket.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/xp_socket.c -o main/streams/xp_socket.lo 
main/streams/mmap.lo: /php-5.3.2/main/streams/mmap.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/mmap.c -o main/streams/mmap.lo 
main/streams/glob_wrapper.lo: /php-5.3.2/main/streams/glob_wrapper.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/streams/ -I/php-5.3.2/main/streams/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/main/streams/glob_wrapper.c -o main/streams/glob_wrapper.lo 
main/internal_functions.lo: main/internal_functions.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c main/internal_functions.c -o main/internal_functions.lo 
main/internal_functions_cli.lo: main/internal_functions_cli.c
	$(LIBTOOL) --mode=compile $(CC)  -Imain/ -I/php-5.3.2/main/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c main/internal_functions_cli.c -o main/internal_functions_cli.lo 
Zend/zend_language_parser.lo: /php-5.3.2/Zend/zend_language_parser.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_language_parser.c -o Zend/zend_language_parser.lo 
Zend/zend_language_scanner.lo: /php-5.3.2/Zend/zend_language_scanner.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_language_scanner.c -o Zend/zend_language_scanner.lo 
Zend/zend_ini_parser.lo: /php-5.3.2/Zend/zend_ini_parser.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_ini_parser.c -o Zend/zend_ini_parser.lo 
Zend/zend_ini_scanner.lo: /php-5.3.2/Zend/zend_ini_scanner.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_ini_scanner.c -o Zend/zend_ini_scanner.lo 
Zend/zend_alloc.lo: /php-5.3.2/Zend/zend_alloc.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_alloc.c -o Zend/zend_alloc.lo 
Zend/zend_compile.lo: /php-5.3.2/Zend/zend_compile.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_compile.c -o Zend/zend_compile.lo 
Zend/zend_constants.lo: /php-5.3.2/Zend/zend_constants.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_constants.c -o Zend/zend_constants.lo 
Zend/zend_dynamic_array.lo: /php-5.3.2/Zend/zend_dynamic_array.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_dynamic_array.c -o Zend/zend_dynamic_array.lo 
Zend/zend_execute_API.lo: /php-5.3.2/Zend/zend_execute_API.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_execute_API.c -o Zend/zend_execute_API.lo 
Zend/zend_highlight.lo: /php-5.3.2/Zend/zend_highlight.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_highlight.c -o Zend/zend_highlight.lo 
Zend/zend_llist.lo: /php-5.3.2/Zend/zend_llist.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_llist.c -o Zend/zend_llist.lo 
Zend/zend_opcode.lo: /php-5.3.2/Zend/zend_opcode.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_opcode.c -o Zend/zend_opcode.lo 
Zend/zend_operators.lo: /php-5.3.2/Zend/zend_operators.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_operators.c -o Zend/zend_operators.lo 
Zend/zend_ptr_stack.lo: /php-5.3.2/Zend/zend_ptr_stack.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_ptr_stack.c -o Zend/zend_ptr_stack.lo 
Zend/zend_stack.lo: /php-5.3.2/Zend/zend_stack.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_stack.c -o Zend/zend_stack.lo 
Zend/zend_variables.lo: /php-5.3.2/Zend/zend_variables.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_variables.c -o Zend/zend_variables.lo 
Zend/zend.lo: /php-5.3.2/Zend/zend.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend.c -o Zend/zend.lo 
Zend/zend_API.lo: /php-5.3.2/Zend/zend_API.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_API.c -o Zend/zend_API.lo 
Zend/zend_extensions.lo: /php-5.3.2/Zend/zend_extensions.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_extensions.c -o Zend/zend_extensions.lo 
Zend/zend_hash.lo: /php-5.3.2/Zend/zend_hash.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_hash.c -o Zend/zend_hash.lo 
Zend/zend_list.lo: /php-5.3.2/Zend/zend_list.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_list.c -o Zend/zend_list.lo 
Zend/zend_indent.lo: /php-5.3.2/Zend/zend_indent.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_indent.c -o Zend/zend_indent.lo 
Zend/zend_builtin_functions.lo: /php-5.3.2/Zend/zend_builtin_functions.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_builtin_functions.c -o Zend/zend_builtin_functions.lo 
Zend/zend_sprintf.lo: /php-5.3.2/Zend/zend_sprintf.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_sprintf.c -o Zend/zend_sprintf.lo 
Zend/zend_ini.lo: /php-5.3.2/Zend/zend_ini.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_ini.c -o Zend/zend_ini.lo 
Zend/zend_qsort.lo: /php-5.3.2/Zend/zend_qsort.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_qsort.c -o Zend/zend_qsort.lo 
Zend/zend_multibyte.lo: /php-5.3.2/Zend/zend_multibyte.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_multibyte.c -o Zend/zend_multibyte.lo 
Zend/zend_ts_hash.lo: /php-5.3.2/Zend/zend_ts_hash.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_ts_hash.c -o Zend/zend_ts_hash.lo 
Zend/zend_stream.lo: /php-5.3.2/Zend/zend_stream.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_stream.c -o Zend/zend_stream.lo 
Zend/zend_iterators.lo: /php-5.3.2/Zend/zend_iterators.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_iterators.c -o Zend/zend_iterators.lo 
Zend/zend_interfaces.lo: /php-5.3.2/Zend/zend_interfaces.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_interfaces.c -o Zend/zend_interfaces.lo 
Zend/zend_exceptions.lo: /php-5.3.2/Zend/zend_exceptions.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_exceptions.c -o Zend/zend_exceptions.lo 
Zend/zend_strtod.lo: /php-5.3.2/Zend/zend_strtod.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_strtod.c -o Zend/zend_strtod.lo 
Zend/zend_gc.lo: /php-5.3.2/Zend/zend_gc.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_gc.c -o Zend/zend_gc.lo 
Zend/zend_closures.lo: /php-5.3.2/Zend/zend_closures.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_closures.c -o Zend/zend_closures.lo 
Zend/zend_float.lo: /php-5.3.2/Zend/zend_float.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_float.c -o Zend/zend_float.lo 
Zend/zend_objects.lo: /php-5.3.2/Zend/zend_objects.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_objects.c -o Zend/zend_objects.lo 
Zend/zend_object_handlers.lo: /php-5.3.2/Zend/zend_object_handlers.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_object_handlers.c -o Zend/zend_object_handlers.lo 
Zend/zend_objects_API.lo: /php-5.3.2/Zend/zend_objects_API.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_objects_API.c -o Zend/zend_objects_API.lo 
Zend/zend_default_classes.lo: /php-5.3.2/Zend/zend_default_classes.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_default_classes.c -o Zend/zend_default_classes.lo 
Zend/zend_execute.lo: /php-5.3.2/Zend/zend_execute.c
	$(LIBTOOL) --mode=compile $(CC)  -IZend/ -I/php-5.3.2/Zend/ $(COMMON_FLAGS) $(CFLAGS_CLEAN) $(EXTRA_CFLAGS) -c /php-5.3.2/Zend/zend_execute.c -o Zend/zend_execute.lo 
