%define	vampplugindir	%{_libdir}/vamp
%define srcname	vamp-libxtract-plugins

Summary:	vamp plugins using libxtract
Name:		vamp-plugins-libxtract
Version:	0.4.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/vamp/%{srcname}-%{version}.tar.gz
# Source0-md5:	8e33aef855ae4d4635d32c70c8734daf
Patch0:		%{name}-link.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	libstdc++-devel
BuildRequires:	vamp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of Vamp plugins (http://www.sonicvisualiser.org/vamp.html) for
low-level audio feature extraction using Jamie Bullock's libxtract
(http://sourceforge.net/projects/libxtract/).

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{vampplugindir}
install *.so $RPM_BUILD_ROOT%{vampplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README STATUS
%attr(755,root,root) %{vampplugindir}/*so
