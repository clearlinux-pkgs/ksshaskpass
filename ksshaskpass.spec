#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : ksshaskpass
Version  : 5.15.3
Release  : 13
URL      : https://download.kde.org/stable/plasma/5.15.3/ksshaskpass-5.15.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.15.3/ksshaskpass-5.15.3.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.15.3/ksshaskpass-5.15.3.tar.xz.sig
Summary  : ssh-add helper that uses kwallet and kpassworddialog
Group    : Development/Tools
License  : GPL-2.0
Requires: ksshaskpass-bin = %{version}-%{release}
Requires: ksshaskpass-license = %{version}-%{release}
Requires: ksshaskpass-locales = %{version}-%{release}
Requires: ksshaskpass-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
Ksshaskpass is a front-end for ssh-add which stores the password of the
sh key in KWallet.
Ksshaskpass is not meant to be executed directly, you need to tell
ssh-add about it. ssh-add will then call it if it is not associated
to a terminal.
From the ssh-add manpage:
/----------------
|  DISPLAY and SSH_ASKPASS
|    If ssh-add needs a passphrase, it will read the passphrase from the
|     current terminal if it was run from a terminal.  If ssh-add does not
|     have a terminal associated with it but DISPLAY and SSH_ASKPASS are
|     set, it will execute the program specified by SSH_ASKPASS and open
|     an X11 window to read the passphrase. This is particularly useful
|     when calling ssh-add from a .xsession or related script.  (Note that
|     on some machines it may be necessary to redirect the input from
|     /dev/null to make this work.)
\----------------

%package bin
Summary: bin components for the ksshaskpass package.
Group: Binaries
Requires: ksshaskpass-license = %{version}-%{release}

%description bin
bin components for the ksshaskpass package.


%package license
Summary: license components for the ksshaskpass package.
Group: Default

%description license
license components for the ksshaskpass package.


%package locales
Summary: locales components for the ksshaskpass package.
Group: Default

%description locales
locales components for the ksshaskpass package.


%package man
Summary: man components for the ksshaskpass package.
Group: Default

%description man
man components for the ksshaskpass package.


%prep
%setup -q -n ksshaskpass-5.15.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552412194
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1552412194
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksshaskpass
cp COPYING %{buildroot}/usr/share/package-licenses/ksshaskpass/COPYING
pushd clr-build
%make_install
popd
%find_lang ksshaskpass

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ksshaskpass

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ksshaskpass/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ksshaskpass.1

%files locales -f ksshaskpass.lang
%defattr(-,root,root,-)

