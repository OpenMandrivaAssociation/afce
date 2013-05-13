%define		original_release	51
Name:		afce
Version:	0.9.0
Release:	2
Summary:	Algorithm Flowchart Editor
License:	GPL
Group:		Education
URL:		http://vicking.narod.ru/flowchart/
Source:		%{name}-%{version}-%{original_release}.tar.gz
Source2:	%{name}.desktop
BuildRequires:	pkgconfig(Qt3Support)

%description
Algorithm Flowchart Editor

%prep
%setup -q -n %{name}-%{version}-%{original_release}

%build
qmake
%make

%install
rm -rf %{buildroot}
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -dm 0755 %{buildroot}%{_datadir}/%{name}
install -dm 0755 %{buildroot}%{_datadir}/pixmaps
install -dm 0755 %{buildroot}%{_docdir}/%{name}
install -dm 0755 %{buildroot}%{_datadir}/applications
install -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -m 0644 %{name}_en_US.ts %{buildroot}%{_datadir}/%{name}/%{name}_en_US.ts
install -m 0644 %{name}_ru_RU.ts %{buildroot}%{_datadir}/%{name}/%{name}_ru_RU.ts
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%defattr (-,root,root)
%doc README.RU.txt LICENSE.TXT doc/index.html
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%clean
rm -rf %{buildroot}

%changelog
* Thu Aug 11 2011 Sergey Zhemoitel <serg@mandriva.org> 0.9.0-1
+ Revision: 693921
- fix spec
- fix spec
- fix spec
- fix spec
- imported package afce

