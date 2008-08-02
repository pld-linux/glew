Summary:	The OpenGL Extension Wrangler Library
Summary(pl.UTF-8):	Bibliteka OpenGL Extension Wrangler
Name:		glew
Version:	1.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/glew/%{name}-%{version}-src.tgz
# Source0-md5:	3fececda0151b060c08ffd8a12892741
Patch0:		%{name}-dynamic-progs.patch
URL:		http://glew.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform
C/C++ extension loading library. GLEW provides efficient run-time
mechanisms for determining which OpenGL extensions are supported on
the target platform. OpenGL core and extension functionality is
exposed in a single header file.

%description -l pl.UTF-8
OpenGL Extension Wrangler Library (GLEW) jest międzyplatformową
biblioteką C/C++ ładującą rozszerzenia. GLEW zapewnia wydajne
mechanizmy rozpoznające które rozszerzenia są dostępne w czasie
wykonywania programu. Funkcjonalność rdzenia OpenGL i rozszerzeń
jest udostępniana w pojedynczym pliku nagłówkowym.

%package devel
Summary:	Header files for glew
Summary(pl.UTF-8):	Pliki nagłówkowe glew
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
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
%setup -q -n glew
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/GL}

install bin/* $RPM_BUILD_ROOT%{_bindir}
cp -d lib/* $RPM_BUILD_ROOT%{_libdir}
install include/GL/* $RPM_BUILD_ROOT%{_includedir}/GL

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libGLEW.so.*.*.*
%ghost %attr(755,root,root) %{_libdir}/libGLEW.so.?.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLEW.so
%{_includedir}/GL/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libGLEW.a
