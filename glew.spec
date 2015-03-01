Summary:	The OpenGL Extension Wrangler Library
Summary(pl.UTF-8):	Bibliteka OpenGL Extension Wrangler
Name:		glew
Version:	1.10.0
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/glew/%{name}-%{version}.tgz
# Source0-md5:	2f09e5e6cb1b9f3611bcac79bc9c2d5d
URL:		http://glew.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++
extension loading library. GLEW provides efficient run-time mechanisms
for determining which OpenGL extensions are supported on the target
platform. OpenGL core and extension functionality is exposed in a
single header file.

%description -l pl.UTF-8
OpenGL Extension Wrangler Library (GLEW) jest międzyplatformową
biblioteką C/C++ ładującą rozszerzenia. GLEW zapewnia wydajne
mechanizmy rozpoznające które rozszerzenia są dostępne w czasie
wykonywania programu. Funkcjonalność rdzenia OpenGL i rozszerzeń jest
udostępniana w pojedynczym pliku nagłówkowym.

%package devel
Summary:	Header files for glew
Summary(pl.UTF-8):	Pliki nagłówkowe glew
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXmu-devel

%description devel
Header files for glew.

%description devel -l pl.UTF-8
Pliki nagłówkowe glew.

%package static
Summary:	Static glew library
Summary(pl.UTF-8):	Biblioteka statyczna glew
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glew library.

%description static -l pl.UTF-8
Biblioteka statyczna glew.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/GL,%{_pkgconfigdir}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -d lib/* $RPM_BUILD_ROOT%{_libdir}
install include/GL/{glew,glxew}.h $RPM_BUILD_ROOT%{_includedir}/GL
install glew.pc glewmx.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt TODO.txt doc/*.{html,css,png,jpg}
%attr(755,root,root) %{_bindir}/glewinfo
%attr(755,root,root) %{_bindir}/visualinfo
%attr(755,root,root) %{_libdir}/libGLEW.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLEW.so.1.10
%attr(755,root,root) %{_libdir}/libGLEWmx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLEWmx.so.1.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLEW.so
%attr(755,root,root) %{_libdir}/libGLEWmx.so
%{_includedir}/GL/glew.h
%{_includedir}/GL/glxew.h
%{_pkgconfigdir}/glew.pc
%{_pkgconfigdir}/glewmx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libGLEW.a
%{_libdir}/libGLEWmx.a
