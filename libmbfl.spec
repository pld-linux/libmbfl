#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Streamable kanji code filter and converter
Summary(pl.UTF-8):	Strumieniowy filtr i konwerter kodu kanji
Name:		libmbfl
Version:	1.3.1
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	https://github.com/moriyoshi/libmbfl/tarball/%{name}-%{version}#/%{name}-%{version}.tgz
# Source0-md5:	daac832e6579643fb85121ffdaa8d30a
Source1:	ftp://ftp.unicode.org/Public/UNIDATA/EastAsianWidth.txt
# Source1-md5:	e2ec8af9070c1fb3a069e5c76f3ce939
Source2:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-1.TXT
# Source2-md5:	12e09bd6c9c501b55e0f27acaf60c672
Source3:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-2.TXT
# Source3-md5:	9c338678a16843fd60fcd12602f767e5
Source4:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-3.TXT
# Source4-md5:	508e6e6c9944169639d3110e0b973ce0
Source5:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-4.TXT
# Source5-md5:	de68d2887e903b683ac7de31fcf86e04
Source6:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-5.TXT
# Source6-md5:	4c2e46c0b5c710935c6d48a96a930f55
Source7:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-6.TXT
# Source7-md5:	0b6fca3cf6ced7832ec98bd83e9d8573
Source8:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-7.TXT
# Source8-md5:	e6b859201a1a2a4ef070877389351a60
Source9:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-8.TXT
# Source9-md5:	c77336d026dc44cb4bfa23dd89fa9dde
Source10:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-9.TXT
# Source10-md5:	dc12e2b5e874edc397380ffd8ae55ed2
Source11:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-10.TXT
# Source11-md5:	1756fe8a4076a0acbaa84f31f73a5e18
Source12:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-11.TXT
# Source12-md5:	4b5563bdf9716200e25827da7f95580c
Source13:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-13.TXT
# Source13-md5:	f97c84a786088bd85262f57df05408fd
Source14:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-14.TXT
# Source14-md5:	b3d2634fb31883aae57fcfeb06436e2b
Source15:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-15.TXT
# Source15-md5:	f807052642f93374e506682793924df0
Source16:	ftp://ftp.unicode.org/Public/MAPPINGS/ISO8859/8859-16.TXT
# Source16-md5:	f905f3043c0b8265c64fb80ec9e747c3
Source17:	ftp://ftp.unicode.org/Public/UNIDATA/EmojiSources.txt
# Source17-md5:	6dc97737e77191ec1db766d9d55cb7c1
URL:		https://github.com/moriyoshi/libmbfl
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Libmbfl, a streamable multibyte character code filter and
converter library.

%description -l pl.UTF-8
libmbfl to biblioteka strumieniowego filtra i konwertera
wielobajtowych kodów znaków.

%package devel
Summary:	Header files for libmbfl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmbfl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libmbfl library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libmbfl.

%package static
Summary:	Static libmbfl library
Summary(pl.UTF-8):	Statyczna biblioteka libmbfl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmbfl library.

%description static -l pl.UTF-8
Statyczna biblioteka libmbfl.

%prep
%setup -qc
mv moriyoshi-libmbfl-*/* .
cp -p %{SOURCE1} mbfl
cp -p %{SOURCE2} filters
cp -p %{SOURCE3} filters
cp -p %{SOURCE4} filters
cp -p %{SOURCE5} filters
cp -p %{SOURCE6} filters
cp -p %{SOURCE7} filters
cp -p %{SOURCE8} filters
cp -p %{SOURCE9} filters
cp -p %{SOURCE10} filters
cp -p %{SOURCE11} filters
cp -p %{SOURCE12} filters
cp -p %{SOURCE13} filters
cp -p %{SOURCE14} filters
cp -p %{SOURCE15} filters
cp -p %{SOURCE16} filters
cp -p %{SOURCE17} filters

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS DISCLAIMER README
%attr(755,root,root) %{_libdir}/libmbfl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmbfl.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmbfl.so
%{_libdir}/libmbfl.la
%{_includedir}/mbfl

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmbfl.a
%endif
