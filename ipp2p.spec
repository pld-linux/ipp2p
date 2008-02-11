#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	grsec_kernel	# build for kernel-grsecurity
#
%if %{with kernel} && %{with dist_kernel} && %{with grsec_kernel}
%define	alt_kernel	grsecurity
%endif
#
%define	iptables_ver	1.3.3

%define		rel	12
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl.UTF-8):	IPP2P - rozszerzenie filtra pakietów identyfikujące ruch P2P
Name:		ipp2p
Version:	0.8.2
Release:	%{rel}
Epoch:		1
License:	GPL
Group:		Base/Kernel
Source0:	http://www.ipp2p.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	9dd745830f302d70d0b728013c1d6a0c
Patch0:		%{name}-2.6.19.patch
Patch1:		%{name}-2.6.21.patch
URL:		http://www.ipp2p.org/
%{?with_userspace:BuildRequires:	iptables-devel >= 1.3.3}
%if %{with kernel}
%if %{with dist_kernel}
BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.379
BuildRequires:	sed >= 4.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IPP2P is a netfilter extension to identify P2P filesharing traffic.
The main goal for developing IPP2P was giving the adminstrator a
dynamic tool to filter the traffic in an intelligent way. So it
doesn't aim at prohibiting all P2P traffic but make it possible to
shape this traffic to a given rate. For this purpose IPP2P searchs the
payload of TCP packets for signaling patterns of P2P networks. As
these patterns are not being present in all P2P packets we had to use
some other netfilter extensions in order to get the whole IPP2P
package working as already described. IPP2P works together with
connection tracking and connection marking - in that way you can catch
the bigger part of all P2P packets and limit the bandwidth rate.

%description -l pl.UTF-8
IPP2P to rozszerzenie netfiltra służące do identyfikowania ruchu
związanego z dzieleniem plików P2P. Głównym celem tworzenia IPP2P jest
udostępnienie administratorowi dynamicznego narzędzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie całego ruchu
P2P, ale umożliwienie ograniczenia tego ruchu do danej przepustowości.
W tym celu IPP2P przeszukuje zawartość (payload) pakietów TCP pod
kątem wzorców sygnalizujących sieci P2P. Jeśli tych wzorców nie ma w
pakietach, muszą być użyte inne rozszerzenia netfiltra, aby IPP2P
działało zgodnie z opisem. IPP2P współpracuje ze śledzeniem oraz
znakowaniem połączeń - w ten sposób można wychwycić większą część
pakietów P2P i ograniczyć wykorzystanie łącza przez nie.

%package -n kernel%{_alt_kernel}-net-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl.UTF-8):	IPP2P - rozszerzenie filtra pakietów identyfikujące ruch P2P
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel}
Requires(post,postun):	/sbin/depmod

%description -n kernel%{_alt_kernel}-net-ipp2p
IPP2P is a netfilter extension to identify P2P filesharing traffic.
The main goal for developing IPP2P was giving the adminstrator a
dynamic tool to filter the traffic in an intelligent way. So it
doesn't aim at prohibiting all P2P traffic but make it possible to
shape this traffic to a given rate. For this purpose IPP2P searchs the
payload of TCP packets for signaling patterns of P2P networks. As
these patterns are not being present in all P2P packets we had to use
some other netfilter extensions in order to get the whole IPP2P
package working as already described. IPP2P works together with
connection tracking and connection marking - in that way you can catch
the bigger part of all P2P packets and limit the bandwidth rate.

This package contains Linux kernel module.

%description -n kernel%{_alt_kernel}-net-ipp2p -l pl.UTF-8
IPP2P to rozszerzenie netfiltra służące do identyfikowania ruchu
związanego z dzieleniem plików P2P. Głównym celem tworzenia IPP2P jest
udostępnienie administratorowi dynamicznego narzędzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie całego ruchu
P2P, ale umożliwienie ograniczenia tego ruchu do danej przepustowości.
W tym celu IPP2P przeszukuje zawartość (payload) pakietów TCP pod
kątem wzorców sygnalizujących sieci P2P. Jeśli tych wzorców nie ma w
pakietach, muszą być użyte inne rozszerzenia netfiltra, aby IPP2P
działało zgodnie z opisem. IPP2P współpracuje ze śledzeniem oraz
znakowaniem połączeń - w ten sposób można wychwycić większą część
pakietów P2P i ograniczyć wykorzystanie łącza przez nie.

Ten pakiet zawiera moduł jądra Linuksa.

%package -n iptables-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl.UTF-8):	IPP2P - rozszerzenie filtra pakietów identyfikujące ruch P2P
Release:	%{rel}
Group:		Base/Kernel
Requires:	iptables

%description -n iptables-ipp2p
IPP2P is a netfilter extension to identify P2P filesharing traffic.
The main goal for developing IPP2P was giving the adminstrator a
dynamic tool to filter the traffic in an intelligent way. So it
doesn't aim at prohibiting all P2P traffic but make it possible to
shape this traffic to a given rate. For this purpose IPP2P searchs the
payload of TCP packets for signaling patterns of P2P networks. As
these patterns are not being present in all P2P packets we had to use
some other netfilter extensions in order to get the whole IPP2P
package working as already described. IPP2P works together with
connection tracking and connection marking - in that way you can catch
the bigger part of all P2P packets and limit the bandwidth rate.

This package contains iptables module needed to control IPP2P kernel
module.

%description -n iptables-ipp2p -l pl.UTF-8
IPP2P to rozszerzenie netfiltra służące do identyfikowania ruchu
związanego z dzieleniem plików P2P. Głównym celem tworzenia IPP2P jest
udostępnienie administratorowi dynamicznego narzędzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie całego ruchu
P2P, ale umożliwienie ograniczenia tego ruchu do danej przepustowości.
W tym celu IPP2P przeszukuje zawartość (payload) pakietów TCP pod
kątem wzorców sygnalizujących sieci P2P. Jeśli tych wzorców nie ma w
pakietach, muszą być użyte inne rozszerzenia netfiltra, aby IPP2P
działało zgodnie z opisem. IPP2P współpracuje ze śledzeniem oraz
znakowaniem połączeń - w ten sposób można wychwycić większą część
pakietów P2P i ograniczyć wykorzystanie łącza przez nie.

Ten pakiet zawiera moduł iptables potrzebny do sterowania modułem
jądra IPP2P.

%prep
%setup -q
sed -i "s:shell iptables:shell %{_sbindir}/iptables:" Makefile
%patch0 -p1
%patch1 -p1

%build
%if %{with userspace}
IPTABLES_VERSION="%{iptables_ver}"
%{__cc} %{rpmcflags} -DIPTABLES_VERSION=\"$IPTABLES_VERSION\" -fPIC -c libipt_ipp2p.c
#vim: "
ld --as-needed -shared -o libipt_ipp2p.so libipt_ipp2p.o
%endif

%if %{with kernel}
# kernel module(s)
%build_kernel_modules -m ipt_%{name}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/iptables
install libipt_%{name}.so $RPM_BUILD_ROOT%{_libdir}/iptables
%endif

%if %{with kernel}
%install_kernel_modules -m ipt_%{name} -d kernel/net/ipv4/netfilter
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel%{_alt_kernel}-net-ipp2p
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-net-ipp2p
%depmod %{_kernel_ver}

%if %{with kernel}
%files -n kernel%{_alt_kernel}-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/net/ipv4/netfilter/ipt_%{name}.ko*
%endif

%if %{with userspace}
%files -n iptables-ipp2p
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/iptables/*.so
%endif
