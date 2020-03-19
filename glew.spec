Summary:	The OpenGL Extension Wrangler Library
Summary(pl.UTF-8):	Bibliteka OpenGL Extension Wrangler
Name:		glew
Version:	2.2.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/glew/%{name}-%{version}.tgz
# Source0-md5:	3579164bccaef09e36c0af7f4fd5c7c7
Patch0:		%{name}-eglew.patch
Patch1:		%{name}-const.patch
URL:		http://glew.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	xorg-lib-libX11-devel
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
Requires:	xorg-lib-libX11-devel

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
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	INCDIR=%{_includedir}/GL \
	LIBDIR=%{_libdir} \
	PKGDIR=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install.all \
	DESTDIR=$RPM_BUILD_ROOT \
	INCDIR=%{_includedir}/GL \
	LIBDIR=%{_libdir} \
	PKGDIR=%{_pkgconfigdir}

# Win32-specific
%{__rm} $RPM_BUILD_ROOT%{_includedir}/GL/wglew.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md doc/*.{html,css,png,jpg}
%attr(755,root,root) %{_bindir}/glewinfo
%attr(755,root,root) %{_bindir}/visualinfo
%attr(755,root,root) %{_libdir}/libGLEW.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLEW.so.2.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLEW.so
%{_includedir}/GL/eglew.h
%{_includedir}/GL/glew.h
%{_includedir}/GL/glxew.h
%{_pkgconfigdir}/glew.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libGLEW.a
