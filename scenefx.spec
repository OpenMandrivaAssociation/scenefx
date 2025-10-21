%define api 4
%define libname %mklibname scenefx
%define devname %mklibname -d scenefx

Name:     scenefx
Version:  0.4.1
Release:  1
Summary:  A drop-in wlroots replacement that allows eye-candy effects
License:  MIT
Group:    System/Libraries

Url:      https://github.com/wlrfx/scenefx
Source0: https://github.com/wlrfx/scenefx/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires: pkgconfig(wayland-protocols) >= 1.27
BuildRequires: pkgconfig(wayland-server) >= 1.22.0
BuildRequires: pkgconfig(wlroots-0.19)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb-ewmh)

%description
%summary.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/%{name}-0.%{api}.so

%files -n %{devname}
%{_includedir}/scenefx-0.%{api}/
%{_libdir}/pkgconfig/scenefx-0.%{api}.pc
