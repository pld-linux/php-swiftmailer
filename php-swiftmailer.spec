%define		pkgname	swiftmailer
%define		php_min_version 5.2.1
%include	/usr/lib/rpm/macros.php
Summary:	Component-based library for sending e-mails
Name:		php-%{pkgname}
Version:	5.4.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/swiftmailer/swiftmailer/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	46ae34e60060087a7e01c01afc5bc731
URL:		http://swiftmailer.org/
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(bcmath)
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(hash)
Requires:	php(mbstring)
Requires:	php(openssl)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{pkgname}

%description
Swift Mailer is component based mailing solution for PHP 5. Send
emails using SMTP, sendmail, postfix or a custom Transport
implementation of your own. It Supports servers that require username
and password and/or encryption.

Features:
- SMTP authentication
- event-driven plugins to customize the library
- MIME compliant HTML/multipart emails
- large attachments and inline/embedded images with low memory use

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a lib/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES LICENSE VERSION
%{_appdir}
