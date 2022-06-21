#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : ksshaskpass
Version  : 5.25.1
Release  : 64
URL      : https://download.kde.org/stable/plasma/5.25.1/ksshaskpass-5.25.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.1/ksshaskpass-5.25.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.1/ksshaskpass-5.25.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: ksshaskpass-bin = %{version}-%{release}
Requires: ksshaskpass-license = %{version}-%{release}
Requires: ksshaskpass-locales = %{version}-%{release}
Requires: ksshaskpass-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev

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
%setup -q -n ksshaskpass-5.25.1
cd %{_builddir}/ksshaskpass-5.25.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655826613
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1655826613
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ksshaskpass
cp %{_builddir}/ksshaskpass-5.25.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ksshaskpass/3e8971c6c5f16674958913a94a36b1ea7a00ac46
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
/usr/share/package-licenses/ksshaskpass/3e8971c6c5f16674958913a94a36b1ea7a00ac46

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ksshaskpass.1

%files locales -f ksshaskpass.lang
%defattr(-,root,root,-)

