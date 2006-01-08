Summary:	Streamable kanji code filter and converter
Summary(pl):	Strumieniowy filtr i konwerter kodu kanji
Name:		libmbfl
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	%{name}.tar.bz2
# Source0-md5:	6c74e119c341ca655e05222175442722
Source1:	ftp://ftp.unicode.org/Public/UNIDATA/EastAsianWidth.txt
# Source1-md5:	ab95687111a50d4375725c0b9dade8d9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is Libmbfl, a streamable multibyte character code filter and
converter library.

%description -l pl
libmbfl to biblioteka strumieniowego filtra i konwertera
wielobajtowych kod�w znak�w.

%package devel
Summary:	Header files for libmbfl library
Summary(pl):	Pliki nag��wkowe biblioteki libmbfl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libmbfl library.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe biblioteki libmbfl.

%package static
Summary:	Static libmbfl library
Summary(pl):	Statyczna biblioteka libmbfl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmbfl library.

%description static -l pl
Statyczna biblioteka libmbfl.

%prep
%setup -q -n %{name}
cp %{SOURCE1} mbfl

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmbfl.so
%{_libdir}/libmbfl.la
%{_includedir}/mbfl

%files static
%defattr(644,root,root,755)
%{_libdir}/libmbfl.a
