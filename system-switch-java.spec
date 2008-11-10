Name: system-switch-java
Version: 1.1.4
Epoch: 0
Release: %mkrel 0.1.1
Summary: A tool for changing the default Java toolset

Group: System/Configuration/Other
License: GPLv2+
URL: ftp://sources.redhat.com/pub/rhug/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: python-devel

Requires: chkconfig
Requires: libuser
# for snack.py python module:
Requires: newt
Requires: pygtk2.0
Requires: pygtk2.0-libglade
Requires: python
Requires: usermode-consoleonly
Requires: usermode

Obsoletes: system-switch-java-gui <= 1.0.0-1.fc7
Provides: system-switch-java-gui = %{version}-%{release}

%description
The system-switch-java package provides an easy-to-use tool to select
the default Java toolset for the system.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%find_lang %{name}
%{_bindir}/desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README COPYING COPYING.icon
%{_bindir}/%{name}
%{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/switch_java_functions.py*
%{_datadir}/%{name}/switch_java_gui.py*
%{_datadir}/%{name}/switch_java_tui.py*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/system-switch-java.glade
%config(noreplace) /etc/pam.d/%{name}
%config(noreplace) /etc/security/console.apps/%{name}
