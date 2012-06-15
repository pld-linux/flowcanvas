Summary:	Interactive Gtkmm/Gnomecanvasmm widget for graph-based interfaces
Summary(pl.UTF-8):	Interaktywny widget Gtkmm/Gnomecanvasmm do interfejsów opartych na rysunkach
Name:		flowcanvas
Version:	0.7.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	a4908f6385ce9fd2ce97c8caa823f053
URL:		http://drobilla.net/software/flowcanvas/
BuildRequires:	boost-devel
BuildRequires:	graphviz-devel >= 2.8
BuildRequires:	gtkmm-devel >= 2.10.0
BuildRequires:	libgnomecanvasmm-devel >= 2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	python
Requires:	graphviz >= 2.8
Requires:	gtkmm >= 2.10.0
Requires:	libgnomecanvasmm >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for
graph-based interfaces (patchers, modular synthesizers, finite state
automata, interactive graphs, etc).

%description -l pl.UTF-8
FlowCanvas to interaktywny widget Gtkmm/Gnomecanvasmm do interfejsów
opartych na rysunkach (syntezatory modułowe, automaty skończone,
wykresy interaktywne itp.).

%package devel
Summary:	Header files for flowcanvas library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki flowcanvas
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	boost-devel
Requires:	graphviz-devel >= 2.8
Requires:	gtkmm-devel >= 2.10.0
Requires:	libgnomecanvasmm-devel >= 2.6.0

%description devel
Header files for flowcanvas library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki flowcanvas.

%prep
%setup -q

%build
CXX="%{__cxx}" \
CXXFLAGS="%{rpmcxxflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

# let rpm autogenerate dependencies
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libflowcanvas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflowcanvas.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflowcanvas.so
%{_includedir}/flowcanvas
%{_pkgconfigdir}/flowcanvas.pc
