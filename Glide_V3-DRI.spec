Summary:	Glide runtime for 3Dfx Voodoo Banshee and Voodoo3 boards
Name:		Glide_V3-DRI
Version:	2002.04.10
Release:	 %mkrel 1
Epoch:		1
Source0:        glide3x.2002.04.10.tar.bz2
Source1:        swlibs.2001.01.26.tar.bz2
#Debian patches
Patch20:        swlibs-000-makefile-000.bz2
Patch21:        swlibs-001-mcpu-flag.bz2
Patch22:        swlibs-002-automake.bz2
Patch23:        swlibs-003-libm.bz2
Patch24:	swlibs-nomore-csh.bz2
Patch25:	swlibs-004-ioctl.bz2
Patch26:	swlibs-000-fix-warnings.bz2

Patch30:        glide3x-autoconf-update.bz2
Patch31:        glide3x-comments-warnings.bz2
Patch32:        glide3x-libtool-patch.bz2
Patch33:        glide3x-build-multiargs.bz2
Patch34:        glide3x-debug-vaargs.bz2
Patch35:        glide3x-preprocessor.bz2
Patch36:	glide3x-build-fix.bz2
Patch37:	glide3x-build-with-voodoo5.bz2
Patch38:	glide3x-fix-warnings.bz2

Patch50:	z01-64bit-port.bz2
Patch51:	z02-64bit-port.bz2
Patch52:	z03-amd64-port.bz2
Patch53:	z04-gcc34-port.bz2
Patch54:	z05-gcc4-fix.bz2

License:        3dfx Glide General Public License
Group:          System/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:  %{ix86} ia64 alpha x86_64
BuildRequires:	X11-devel automake1.7 autoconf2.5
URL:		http://glide.sourceforge.net/

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
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1

%patch30 -p2
%patch31 -p2
%patch32 -p2
%patch33 -p2
%patch34 -p2
%patch35 -p2
%patch36 -p2
%patch37 -p2
%patch38 -p2

%patch50 -p2
%patch51 -p2
%patch52 -p2
%patch53 -p2
%patch54 -p2

%build
aclocal-1.7
libtoolize --copy --force
automake-1.7 -a
autoconf
# Build for V3 with DRI
%configure2_5x	--enable-fx-glide-hw=h3 \
		--enable-fx-dri-build \
		--enable-fx-debug=no
make -f makefile.autoconf all CFLAGS="$RPM_OPT_FLAGS -ffast-math -fexpensive-optimizations -funroll-loops -O3"

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} -f makefile.autoconf
#we don't want these
rm -f $RPM_BUILD_ROOT%{_libdir}/libglide3.*a

%postun -p /sbin/ldconfig

%post -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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

