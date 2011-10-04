Name:		afce
Version:	0.9.0
Release:	%mkrel 2
Summary:	Algorithm Flowchart Editor
License:	GPL
Group:		Education
URL:		http://vicking.narod.ru/flowchart/
#Source:		%{name}-%{version}-%{original_release}.tar.gz
Source2:	%{name}.desktop
Source:		afce-095-nntc-edition.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	libqt4-devel

%description
Algorithm Flowchart Editor

%prep
%setup -q -n %{name}
sed -i 's@/usr/share/doc/packages/afce@%_datadir/%name@g' thelpwindow.cpp
mv doc/primer.PNG doc/primer.png

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
install -m 0644 *.ts %{buildroot}%{_datadir}/%{name}/
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop
install doc/* %buildroot%_datadir/%name/

%files
%defattr (-,root,root)
%doc README.RU.txt LICENSE.TXT
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%clean
rm -rf %{buildroot}
