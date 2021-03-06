Name:           nvidia-modprobe
Version:        340.107
Release:        1%{?dist}
Summary:        NVIDIA kernel module loader
Epoch:          2
License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  %{ix86} x86_64

Source0:        https://github.com/NVIDIA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  m4

%description
This utility is used by user-space NVIDIA driver components to make sure the
NVIDIA kernel modules are loaded and that the NVIDIA character device files are
present.

%prep
%setup -q
# Remove additional CFLAGS added when enabling DEBUG
sed -i '/+= -O0 -g/d' utils.mk

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags} \
    DEBUG=1 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%install
%make_install \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%files
%license COPYING
%attr(4755, root, root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Aug 12 2018 Jemma Denson <jdenson@gmail.com> - 2:340.107-1
- Update to 340.107

* Sat Dec 23 2017 Jemma Denson <jdenson@gmail.com> - 2:340.104-2
- Merge in negativo17 to date

* Fri Dec 22 2017 Jemma Denson <jdenson@gmail.com> - 2:340.104-1
- Update to 340.104.

* Thu Feb 23 2017 Simone Caronni <negativo17@gmail.com> - 2:340.102-1
- Udpate to 340.102.

* Thu Dec 15 2016 Simone Caronni <negativo17@gmail.com> - 2:340.101-1
- Update to 340.101.

* Sun Oct 02 2016 Simone Caronni <negativo17@gmail.com> - 2:340.98-1
- Update to 340.98.

* Tue Nov 17 2015 Simone Caronni <negativo17@gmail.com> - 2:340.96-1
- Update to 340.96.

* Tue Sep 08 2015 Simone Caronni <negativo17@gmail.com> - 2:340.93-1
- Update to 340.93.

* Wed Jan 28 2015 Simone Caronni <negativo17@gmail.com> - 2:340.76-1
- Update to 340.76.

* Mon Dec 08 2014 Simone Caronni <negativo17@gmail.com> - 2:340.65-1
- Update to 340.65.

* Wed Nov 05 2014 Simone Caronni <negativo17@gmail.com> - 2:340.58-1
- Update to 340.58.

* Wed Oct 01 2014 Simone Caronni <negativo17@gmail.com> - 2:340.46-1
- Update to 340.46.
- Switched to GitHub sources.

* Sun Aug 17 2014 Simone Caronni <negativo17@gmail.com> - 2:340.32-1
- Update to 340.32.

* Sun Jul 13 2014 Simone Caronni <negativo17@gmail.com> - 2:340.24-2
- Make nvidia-modprobe setuid.

* Tue Jul 08 2014 Simone Caronni <negativo17@gmail.com> - 2:340.24-1
- Update to 340.24.

* Mon Jun 09 2014 Simone Caronni <negativo17@gmail.com> - 2:340.17-1
- Update to 340.17.

* Mon Jun 02 2014 Simone Caronni <negativo17@gmail.com> - 2:337.25-1
- Update to 337.25.

* Tue May 06 2014 Simone Caronni <negativo17@gmail.com> - 2:337.19-1
- Update to 337.19.

* Tue Apr 08 2014 Simone Caronni <negativo17@gmail.com> - 2:337.12-1
- Update to 337.12.

* Tue Mar 04 2014 Simone Caronni <negativo17@gmail.com> - 2:334.21-1
- Update to 334.21.

* Sat Feb 08 2014 Simone Caronni <negativo17@gmail.com> - 2:334.16-1
- First build.
