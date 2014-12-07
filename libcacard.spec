%define major	0
%define libname	%mklibname cacard %major
%define devname	%mklibname -d cacard

Summary:	Common Access Card (CAC) Emulation
Name:		libcacard
Version:	0.1.2
Release:	8
Group:		System/Libraries
License:	LGPLv2+
Url:		http://www.spice-space.org/download
Source0:	http://www.spice-space.org/download/libcacard/libcacard-%{version}.tar.bz2
BuildRequires:	pkgconfig(nss) >= 3.12.8

%description
Common Access Card (CAC) emulation library.

%package -n %{libname}
Summary:	Common Access Card (CAC) Emulation
Group:		System/Libraries
Suggests:	%{name}-tools = %{version}-%{release}

%description -n %{libname}
Common Access Card (CAC) emulation library.

%package tools
Summary:	CAC Emulation tools
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description tools
CAC emulation tools.

%package -n %{devname}
Summary:	CAC Emulation devel
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
CAC emulation development files.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING README
%{_libdir}/libcacard.so.%{major}*

%files -n %{devname}
%{_includedir}/cacard
%{_libdir}/pkgconfig/libcacard.pc
%{_libdir}/libcacard.so

%files tools
%{_bindir}/vscclient

