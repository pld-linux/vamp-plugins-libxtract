%define		vampplugindir	%{_libdir}/vamp
%define		srcname		vamp-libxtract-plugins

Summary:	Vamp plugins using libxtract
Summary(pl.UTF-8):	Wtyczki Vampa wykorzystujące libxtract
Name:		vamp-plugins-libxtract
Version:	0.4.5.20081202
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/vamp/%{srcname}-%{version}.tar.gz
# Source0-md5:	62015fe0d8822f79bcff579c17202810
Patch0:		gcc44.patch
URL:		http://www.vamp-plugins.org/
BuildRequires:	libstdc++-devel
BuildRequires:	libxtract-devel
BuildRequires:	vamp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of Vamp plugins (http://www.sonicvisualiser.org/vamp.html) for
low-level audio feature extraction using Jamie Bullock's libxtract
(http://sourceforge.net/projects/libxtract/).

%description -l pl.UTF-8
Zestaw wtyczek Vampa (http://www.sonicvisualiser.org/vamp.html) do
wydobywania niskopoziomowych cech dźwięku pzry użyciu libxtract Jamie
Bullocka (http://sourceforge.net/projects/libxtract/).

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} -DNDEBUG -ffast-math -Wall -I/usr/include/vamp-sdk -I." \
	LDFLAGS="%{rpmldflags}" \
	PLUGIN_LIBS="-lvamp-sdk -lxtract" \
	PLUGIN_LDFLAGS="-shared -Wl,-Bsymbolic %{rpmldflags}"

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
