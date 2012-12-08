%define major 0
%define libname %mklibname cacard %major
%define develname %mklibname -d cacard

Name: libcacard
Version: 0.1.2
Release: 1
Summary: Common Access Card (CAC) Emulation
Group: System/Libraries
License: LGPLv2+
URL: http://www.spice-space.org/download
Source0: http://www.spice-space.org/download/libcacard/libcacard-%{version}.tar.bz2
BuildRequires: pkgconfig(nss) >= 3.12.8

%description
Common Access Card (CAC) emulation library.

%package -n %libname
Summary: Common Access Card (CAC) Emulation
Group: System/Libraries
Suggests: %{name}-tools = %{version}-%{release}

%description -n %libname
Common Access Card (CAC) emulation library.

%package tools
Summary: CAC Emulation tools
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description tools
CAC emulation tools.

%package -n %develname
Summary: CAC Emulation devel
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
CAC emulation development files.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
find %buildroot -name '*.la' | xargs rm -f

%files -n %libname
%doc COPYING README
%{_libdir}/libcacard.so.%{major}*

%files -n %develname
%{_includedir}/cacard
%{_libdir}/pkgconfig/libcacard.pc
%{_libdir}/libcacard.so

%files tools
%{_bindir}/vscclient


%changelog
* Wed Feb 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.1.2-1
+ Revision: 772212
- imported package libcacard

