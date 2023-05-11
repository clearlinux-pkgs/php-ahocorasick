#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-ahocorasick
Version  : 0.0.7
Release  : 38
URL      : https://pecl.php.net//get/ahocorasick-0.0.7.tgz
Source0  : https://pecl.php.net//get/ahocorasick-0.0.7.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0 PHP-3.0
Requires: php-ahocorasick-lib = %{version}-%{release}
Requires: php-ahocorasick-license = %{version}-%{release}
BuildRequires : buildreq-php

%description
# php_aho_corasick
[![Build Status](https://travis-ci.org/ph4r05/php_aho_corasick.svg?branch=master)](https://travis-ci.org/ph4r05/php_aho_corasick)
[![Coverity Status](https://scan.coverity.com/projects/7177/badge.svg)](https://scan.coverity.com/projects/ph4r05-php_aho_corasick)

%package lib
Summary: lib components for the php-ahocorasick package.
Group: Libraries
Requires: php-ahocorasick-license = %{version}-%{release}

%description lib
lib components for the php-ahocorasick package.


%package license
Summary: license components for the php-ahocorasick package.
Group: Default

%description license
license components for the php-ahocorasick package.


%prep
%setup -q -n ahocorasick-0.0.7
cd %{_builddir}/ahocorasick-0.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-ahocorasick
cp %{_builddir}/ahocorasick-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-ahocorasick/c09f9595f49b611cb4815dac18057910e5ff66b3
cp %{_builddir}/ahocorasick-%{version}/LICENSE-PECL %{buildroot}/usr/share/package-licenses/php-ahocorasick/b7ee52f82385b0e3e793646d5fc716fa99720abe
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/ahocorasick.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-ahocorasick/b7ee52f82385b0e3e793646d5fc716fa99720abe
/usr/share/package-licenses/php-ahocorasick/c09f9595f49b611cb4815dac18057910e5ff66b3
