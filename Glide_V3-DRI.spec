Summary:	Glide runtime for 3Dfx Voodoo Banshee and Voodoo3 boards
Name:		Glide_V3-DRI
Version:	2002.04.10
Release:	%mkrel 3
Epoch:		1
Group:          System/Libraries
License:        3dfx Glide General Public License
URL:		http://glide.sourceforge.net/
Source0:	glide3x.2002.04.10.tar.bz2
Source1:	swlibs.2001.01.26.tar.bz2
#Debian patches
Patch6:		glide3x-autoconf-update
Patch7:		glide3x-build-fix
Patch8:		glide3x-build-multiargs
Patch9:		glide3x-build-with-voodoo5
Patch10:	glide3x-comments-warnings
Patch11:	glide3x-debug-vaargs
Patch12:	glide3x-fix-warnings
Patch13:	glide3x-libtool-patch
Patch14:	glide3x-link-libm
Patch15:	glide3x-link-unresolved
Patch16:	glide3x-preprocessor
Patch17:	swlibs-000-fix-warnings
Patch18:	swlibs-000-makefile-000
Patch19:	swlibs-001-mcpu-flag
Patch20:	swlibs-002-automake
Patch21:	swlibs-003-libm
Patch22:	swlibs-004-ioctl
Patch23:	swlibs-nomore-csh
Patch24:	z01-64bit-port
Patch25:	z02-64bit-port
Patch26:	z03-amd64-port
Patch27:	z04-gcc34-port
Patch28:	z05-gcc4-fix
Patch29:	z06-gcc401-fix
Patch30:	z07-cpudetect-no-ia32
ExclusiveArch:	%{ix86} ia64 alpha x86_64
BuildRequires:	X11-devel automake1.7 autoconf2.5 libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
This library allows the user to use a 3dfx Interactive Voodoo Banshee
or Voodoo3 card under Linux with DRI support.  The source support DRI
versions of Glide.

# Glide3 DRI
%package devel
Summary:	Development headers for Glide 3.x
Group:		Development/C
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes the headers files necessary for developing
applications that use the 3Dfx Interactive Voodoo3 card.

%prep

%setup -q -n glide3x -a1
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0
%patch19 -p0
%patch20 -p0
%patch21 -p0
%patch22 -p0
%patch23 -p0
%patch24 -p0
%patch25 -p0
%patch26 -p0
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0

# lib64 fixes
find -type f -name "makefile*" | xargs perl -pi -e "s|/usr/X11R6/lib\b|/usr/X11R6/%{_lib}|g"

%build
libtoolize --copy --force
aclocal-1.7
automake-1.7 -a
autoconf

# Build for V3 with DRI
%configure2_5x \
    --enable-fx-glide-hw=h3 \
    --enable-fx-dri-build \
    --enable-fx-debug=no

make -f makefile.autoconf all CFLAGS="%{optflags} -ffast-math -fexpensive-optimizations -funroll-loops"

%install
rm -rf %{buildroot}

%makeinstall_std -f makefile.autoconf

#we don't want these
rm -f %{buildroot}%{_libdir}/libglide3.*a

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README COPYING INSTALL
%{_libdir}/libglide3.so.3.10.0
%{_libdir}/libglide3.so.3

%files devel
%defattr(-, root, root)
%dir %{_includedir}/glide3
%{_includedir}/glide3/*
%{_libdir}/libglide3.so
