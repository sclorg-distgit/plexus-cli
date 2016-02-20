%global pkg_name plexus-cli
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global parent plexus
%global subname cli

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.2
Release:        20.10%{?dist}
Epoch:          0
Summary:        Command Line Interface facilitator for Plexus
License:        ASL 2.0
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/archive/plexus-tools/tags/plexus-cli-1.2
# tar czf plexus-cli-%{version}-src.tar.gz plexus-cli-%{version}
# Note: Exported revision 8188.
Source0:        %{pkg_name}-%{version}-src.tar.gz
Source1:        LICENSE-2.0.txt

# License headers missing from some files
# http://jira.codehaus.org/browse/PLX-418
Patch0:         plexus-cli-licenseheaders.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-compiler-plugin
BuildRequires:  maven30-maven-install-plugin
BuildRequires:  maven30-maven-jar-plugin
BuildRequires:  maven30-maven-javadoc-plugin
BuildRequires:  maven30-maven-resources-plugin
BuildRequires:  maven30-maven-release
BuildRequires:  maven30-plexus-classworlds
BuildRequires:  maven30-plexus-containers-container-default
BuildRequires:  maven30-plexus-utils
BuildRequires:  %{?scl_prefix_java_common}apache-commons-cli

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
find . -name "*.jar" -exec rm -f {} \;

%patch0 -p3

cp -p %{SOURCE1} .

%mvn_file : %{parent}/%{subname}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0:1.2-20.10
- maven33 rebuild

* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 0:1.2-20.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.2-20.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:1.2-20.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-20.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-20.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-20.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-20.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-20.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-20.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.2-20
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 0:1.2-19
- Migrate away from mvn-rpmbuild (Resolves: #997492)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-18
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 28 2013 Mat Booth <fedora@matbooth.co.uk> - 0:1.2-17
- Remove unneeded BRs, rhbz #915617

* Thu Feb 28 2013 Mat Booth <fedora@matbooth.co.uk> - 0:1.2-16
- Include a copy of the licence, rhbz #880282

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.2-14
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 16 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.2-13
- Fix license tag to be ASL 2.0 (no plexus licensing anywhere)
- Update to new guidelines

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 12 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-10
- Build with maven 3.x

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-8
- Add jakarta-commons-cli BR

* Thu Aug 20 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-7
- Remove gcj support
- Default to building with ant
- Add patch to include fixed file headers
  (http://jira.codehaus.org/browse/PLX-418)

* Sun May 17 2009 Fernando Nasser <fnasser@redhat.com> 0:1.2-6
- Fix license and source URL

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 0:1.2-5
- Add BRs maven-doxia*
- Rebuild with new maven2 2.0.8 built in non-bootstrap mode

* Tue Mar 17 2009 Yong Yang <yyang@redhat.com> 0:1.2-4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> 0:1.2-3
- fix release tag

* Wed Jan 14 2009 Yong Yang <yyang@redhat.com> 0:1.2-2jpp.2
-re-build with gcj

* Wed Jan 14 2009 Yong Yang <yyang@redhat.com> 0:1.2-2jpp.1
- Import from maven 2.0.8 packages, initial bulding

* Wed Jan 30 2008 Deepak Bhole <dbhole@redhat.com> 0:1.2-1jpp.1
- Initial build with merge from JPackage
