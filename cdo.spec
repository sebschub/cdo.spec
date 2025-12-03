Name:           cdo
Version:        2.5.4
Release:        1%{?dist}
Summary:        A program for manipulating GRIB/NetCDF/SERVICE/EXTRA files
Group:          Applications/Engineering
License:        GPLv2
URL:            https://code.mpimet.mpg.de/projects/cdo
Source0:        https://code.mpimet.mpg.de/attachments/download/30128/cdo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  eccodes-devel,netcdf-devel,udunits2-devel,proj-devel,gcc-c++,python3

%description
CDO (Climate Data Operatores) is a collection of command line Operators
to manipulate and analyse Climate and NWP model Data.
Supported data formats are GRIB 1/2, netCDF 3/4, SERVICE, EXTRA and IEG.
There are more than 600 operators available.

%prep
%setup -q -n %{name}-%{version}

%build
export CPPFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/netcdf -I%{_includedir}/hdf5 -I%{_includedir}/proj -I%{_includedir}/udunits2/"
# export LDFLAGS=-L%{_libdir}/netcdf-3
%configure --with-eccodes --with-netcdf --with-hdf5 --with-udunits2=/usr/include --with-proj=/usr/include --with-zlib
make %{?_smp_mflags}
unset CPPFLAGS LDFLAGS

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root,-)
%doc README OPERATORS doc/cdo.pdf doc/cdo_refcard.pdf
%{_bindir}/*


%changelog
* Mi Dez 03 2025 Sebastian Schubert <schubert.seb@gmail.com> - 2.5.4-1
- Update to 2.5.4

* Wed May 14 2025 Sebastian Schubert <schubert.seb@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Sun May 26 2024 Sebastian Schubert <schubert.seb@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Sat Feb 24 2024 Sebastian Schubert <schubert.seb@gmail.com> - 2.4.0-2
- Add eccodes support

* Sat Feb 24 2024 Sebastian Schubert <schubert.seb@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Mon Jul 3 2023 Sebastian Schubert <schubert.seb@gmail.com> - 2.2.2-1
- Update to 2.2.0

* Tue Jan 10 2023 Sebastian Schubert <schubert.seb@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Thu Nov 17 2022 Sebastian Schubert - 2.1.0
- Update to 2.1.0

* Tue Oct 4 2022 Jeroen Wouters - 2.0.6
- Update to 2.0.6

* Thu Jun 25 2020 Jeroen Wouters - 1.9.8
- Update to 1.9.8

* Wed Sep 14 2016 Nicolas Piaget - 1.7.2-1
- Update to 1.7.2

* Wed Apr 6 2011 Orion Poplawski <orion@cora.nwra.com> - 1.5.0-1
- Update to 1.5.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Mar 2 2010 Orion Poplawski <orion@cora.nwra.com> - 1.4.3-1
- Update to 1.4.3
- New URL

* Fri Jan 8 2010 Orion Poplawski <orion@cora.nwra.com> - 1.4.1-1
- Update to 1.4.1

* Wed Nov 25 2009 Orion Poplawski <orion@cora.nwra.com> - 1.0.8-7
- Rebuild for netcdf 4.1.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> - 1.0.8-5
- Corrected the used header include path for netcdf 4 slightly

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 23 2008 Jon Stanley <jonstanley@gmail.com> - 1.0.8-3
- Fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.8-2
- Autorebuild for GCC 4.3

* Sat Aug 26 2007 Ed Hill <ed@eh3.com> - 1.0.8-1
- new upstream 1.0.8

* Sat Sep  2 2006 Ed Hill <ed@eh3.com> - 1.0.1-2
- fix %{_libdir} mistake

* Sat Sep  2 2006 Ed Hill <ed@eh3.com> - 1.0.1-1
- new upstream 1.0.1

* Thu Feb 16 2006 Ed Hill <ed@eh3.com> - 0.9.6-5
- rebuild for new gcc

* Fri Jun 17 2005 Ed Hill <ed@eh3.com> - 0.9.6-4
- rebuild

* Mon May  9 2005 Ed Hill <ed@eh3.com> - 0.9.6-3
- add dist to release

* Sat Apr 23 2005 Ed Hill <ed@eh3.com> - 0.9.6-2
- fix CPPFLAGS per Tom Callaway's review

* Thu Apr 21 2005 Ed Hill <ed@eh3.com> - 0.9.6-1
- initial version

