#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	up		# don't build UP module
%bcond_without	smp		# don't build SMP module
%bcond_without	userspace	# don't build userspace module
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	grsec_kernel	# build for kernel-grsecurity

%ifarch sparc
%undefine	with_smp
%endif

%if %{without kernel}
%undefine	with_dist_kernel
%endif
%if %{with kernel} && %{with dist_kernel} && %{with grsec_kernel}
%define	alt_kernel	grsecurity
%endif
%if "%{_alt_kernel}" != "%{nil}"
%undefine	with_userspace
%endif

%define	iptables_ver	1.3.3
%define		_rel	56
%define		pname	ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtra pakietów identyfikuj±ce ruch P2P
Name:		%{pname}%{_alt_kernel}
Version:	0.8.2
Release:	%{_rel}
Epoch:		1
License:	GPL
Group:		Base/Kernel
Source0:	http://www.ipp2p.org/downloads/%{pname}-%{version}.tar.gz
# Source0-md5:	9dd745830f302d70d0b728013c1d6a0c
URL:		http://www.ipp2p.org/
%{?with_userspace:BuildRequires:	iptables-devel >= 1.3.3}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.7}
BuildRequires:	rpmbuild(macros) >= 1.330
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

%description -l pl
IPP2P to rozszerzenie netfiltra s³u¿±ce do identyfikowania ruchu
zwi±zanego z dzieleniem plików P2P. G³ównym celem tworzenia IPP2P jest
udostêpnienie administratorowi dynamicznego narzêdzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie ca³ego ruchu
P2P, ale umo¿liwienie ograniczenia tego ruchu do danej przepustowo¶ci.
W tym celu IPP2P przeszukuje zawarto¶æ (payload) pakietów TCP pod
k±tem wzorców sygnalizuj±cych sieci P2P. Je¶li tych wzorców nie ma w
pakietach, musz± byæ u¿yte inne rozszerzenia netfiltra, aby IPP2P
dzia³a³o zgodnie z opisem. IPP2P wspó³pracuje ze ¶ledzeniem oraz
znakowaniem po³±czeñ - w ten sposób mo¿na wychwyciæ wiêksz± czê¶æ
pakietów P2P i ograniczyæ wykorzystanie ³±cza przez nie.

%package -n kernel%{_alt_kernel}-net-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtra pakietów identyfikuj±ce ruch P2P
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
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

%description -n kernel%{_alt_kernel}-net-ipp2p -l pl
IPP2P to rozszerzenie netfiltra s³u¿±ce do identyfikowania ruchu
zwi±zanego z dzieleniem plików P2P. G³ównym celem tworzenia IPP2P jest
udostêpnienie administratorowi dynamicznego narzêdzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie ca³ego ruchu
P2P, ale umo¿liwienie ograniczenia tego ruchu do danej przepustowo¶ci.
W tym celu IPP2P przeszukuje zawarto¶æ (payload) pakietów TCP pod
k±tem wzorców sygnalizuj±cych sieci P2P. Je¶li tych wzorców nie ma w
pakietach, musz± byæ u¿yte inne rozszerzenia netfiltra, aby IPP2P
dzia³a³o zgodnie z opisem. IPP2P wspó³pracuje ze ¶ledzeniem oraz
znakowaniem po³±czeñ - w ten sposób mo¿na wychwyciæ wiêksz± czê¶æ
pakietów P2P i ograniczyæ wykorzystanie ³±cza przez nie.

Ten pakiet zawiera modu³ j±dra Linuksa.

%package -n kernel%{_alt_kernel}-smp-net-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtra pakietów identyfikuj±ce ruch P2P
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel%{_alt_kernel}-smp-net-ipp2p
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

This package contains Linux SMP kernel module.

%description -n kernel%{_alt_kernel}-smp-net-ipp2p -l pl
IPP2P to rozszerzenie netfiltra s³u¿±ce do identyfikowania ruchu
zwi±zanego z dzieleniem plików P2P. G³ównym celem tworzenia IPP2P jest
udostêpnienie administratorowi dynamicznego narzêdzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie ca³ego ruchu
P2P, ale umo¿liwienie ograniczenia tego ruchu do danej przepustowo¶ci.
W tym celu IPP2P przeszukuje zawarto¶æ (payload) pakietów TCP pod
k±tem wzorców sygnalizuj±cych sieci P2P. Je¶li tych wzorców nie ma w
pakietach, musz± byæ u¿yte inne rozszerzenia netfiltra, aby IPP2P
dzia³a³o zgodnie z opisem. IPP2P wspó³pracuje ze ¶ledzeniem oraz
znakowaniem po³±czeñ - w ten sposób mo¿na wychwyciæ wiêksz± czê¶æ
pakietów P2P i ograniczyæ wykorzystanie ³±cza przez nie.

Ten pakiet zawiera modu³ j±dra Linuksa SMP.

%package -n iptables-ipp2p
Summary:	IPP2P - a netfilter extension to identify P2P filesharing traffic
Summary(pl):	IPP2P - rozszerzenie filtra pakietów identyfikuj±ce ruch P2P
Release:	%{_rel}
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

%description -n iptables-ipp2p -l pl
IPP2P to rozszerzenie netfiltra s³u¿±ce do identyfikowania ruchu
zwi±zanego z dzieleniem plików P2P. G³ównym celem tworzenia IPP2P jest
udostêpnienie administratorowi dynamicznego narzêdzia do filtrowania
ruchu w inteligentny sposób. Nie jest nim zablokowanie ca³ego ruchu
P2P, ale umo¿liwienie ograniczenia tego ruchu do danej przepustowo¶ci.
W tym celu IPP2P przeszukuje zawarto¶æ (payload) pakietów TCP pod
k±tem wzorców sygnalizuj±cych sieci P2P. Je¶li tych wzorców nie ma w
pakietach, musz± byæ u¿yte inne rozszerzenia netfiltra, aby IPP2P
dzia³a³o zgodnie z opisem. IPP2P wspó³pracuje ze ¶ledzeniem oraz
znakowaniem po³±czeñ - w ten sposób mo¿na wychwyciæ wiêksz± czê¶æ
pakietów P2P i ograniczyæ wykorzystanie ³±cza przez nie.

Ten pakiet zawiera modu³ iptables potrzebny do sterowania modu³em
j±dra IPP2P.

%prep
%setup -q -n %{pname}-%{version}

%build
%if %{with userspace}
%{__cc} %{rpmcflags} -DIPTABLES_VERSION='"%{iptables_ver}"' -fPIC -c libipt_ipp2p.c
ld %{rpmldflags} -shared -o libipt_ipp2p.so libipt_ipp2p.o
%endif

%if %{with kernel}
# kernel module(s)
%build_kernel_modules -m ipt_%{pname}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/iptables
install libipt_%{pname}.so $RPM_BUILD_ROOT%{_libdir}/iptables
%endif

%if %{with kernel}
%install_kernel_modules -m ipt_%{pname} -d kernel/net/ipv4/netfilter
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel%{_alt_kernel}-net-ipp2p
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-net-ipp2p
%depmod %{_kernel_ver}

%post -n kernel%{_alt_kernel}-smp-net-ipp2p
%depmod %{_kernel_ver}smp

%postun -n kernel%{_alt_kernel}-smp-net-ipp2p
%depmod %{_kernel_ver}smp

%if %{with kernel}
%if %{with up} || %{without dist_kernel}
%files -n kernel%{_alt_kernel}-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/net/ipv4/netfilter/ipt_%{pname}.ko*
%endif

%if %{with smp} && %{with dist_kernel}
%files -n kernel%{_alt_kernel}-smp-net-ipp2p
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/kernel/net/ipv4/netfilter/ipt_%{pname}.ko*
%endif
%endif

%if %{with userspace}
%files -n iptables-ipp2p
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/iptables/*.so
%endif
