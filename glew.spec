Summary:	The OpenGL Extension Wrangler Library
Summary(pl):	Bibliteka OpenGL Extension Wrangler
Name:		glew
Version:	1.3.4
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.sourceforge.net/glew/%{name}-%{version}-src.tgz
# Source0-md5:	9c3911bf30b0ae48fd97d508b21811ca
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

%description -l pl
OpenGL Extension Wrangler Library (GLEW) jest miêdzyplatformow±
bibliotek± C/C++ ³aduj±c± rozszerzenia. GLEW zapewnia wydajne
mechanizmy rozpoznaj±ce które rozszerzenia s± dostêpne w czasie
wykonywania programu. Funkcjonalno¶æ rdzenia OpenGL i rozszerzeñ
jest udostêpniana w pojedynczym pliku nag³ówkowym.

%package devel
Summary:	Header files for glew
Summary(pl):	Pliki nag³ówkowe glew
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXmu-devel

%description devel
Header files for glew.

%description devel -l pl
Pliki nag³ówkowe glew.

%package static
Summary:	Static glew library
Summary(pl):	Biblioteka statyczna glew
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static glew library.

%description static -l pl
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
%doc ChangeLog doc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libGLEW.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLEW.so
%{_includedir}/GL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libGLEW.a
