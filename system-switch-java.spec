Name: system-switch-java
Version: 1.1.4
Epoch: 0
Release: 0.1.3
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


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:1.1.4-0.1.2mdv2010.0
+ Revision: 445345
- rebuild

* Mon Nov 10 2008 David Walluck <walluck@mandriva.org> 0:1.1.4-0.1.1mdv2009.1
+ Revision: 301874
- 1.1.4

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.1.2-2.1.1mdv2009.0
+ Revision: 269403
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.1.2-0.1.1mdv2009.0
+ Revision: 195631
- fix group
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 21 2007 David Walluck <walluck@mandriva.org> 0:1.1.0-3.1mdv2008.0
+ Revision: 54209
- Import system-switch-java



* Sat Jul 14 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-3
- Use Fedora 8 desktop file categories.
- Use desktop-file-install.
- Bump release number.

* Thu Jul  5 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-2
- Bump release number.

* Thu Jul  5 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-1
- Do not use desktop-file-install.

* Wed Jul  4 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-1
- Add categories when installing desktop file.

* Tue Jun 27 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.1.0-1
- Import system-switch-java 1.1.0.
- Merge gui subpackage into base package.

* Tue Jan 23 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - 1.0.0-1
- Initial release.
