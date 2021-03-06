%global gitdate 20171108
%global gitversion 0.2.1
%global gitcommit e98bcf0

Name:           neovim
Version:        %{gitversion}
Release:        2.git%{gitdate}.%{gitcommit}%{?dist}
Summary:        Drop-in replacement for Vim

License:        Apache License, Version 2.0; and Vim license
URL:            https://neovim.io
Source0:        neovim.tar.bz2

BuildRequires:  git
BuildRequires:  cmake >= 2.8.7
BuildRequires:  gettext
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(unibilium)
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(vterm)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(msgpack)
BuildRequires:  lua-lpeg
BuildRequires:  lua-mpack
# Tests
BuildRequires:  busted
BuildRequires:  luacheck
BuildRequires:  lua-nvim-client
BuildRequires:  hostname
BuildRequires:  procps-ng
BuildRequires:  gperf

%description
Neovim is a refactor—and sometimes redactor—in the tradition of Vim, which
itself derives from Stevie. It is not a rewrite, but a continuation and
extension of Vim. Many rewrites, clones, emulators and imitators exist; some
are very clever, but none are Vim. Neovim strives to be a superset of Vim,
notwithstanding some intentionally removed misfeatures; excepting those few and
carefully-considered excisions, Neovim is Vim. It is built for users who want
the good parts of Vim, without compromise, and more.


%package        x11
Summary:        The X11 integration parts of %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       xclip
BuildArch:      noarch

%description    x11
%{summary}.


%prep
%setup -q -n %{name}
# Fix possible race between updating this spec and running source fetching
# script in a build system.
git reset --hard %{gitcommit}


%build
mkdir buildrpm
pushd buildrpm
%{cmake} -DCMAKE_BUILD_TYPE=RelWithDebInfo -DUSE_BUNDLED:BOOL=OFF ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd buildrpm
%make_install
popd
%find_lang nvim


%check
pushd buildrpm
make testlint
make unittest
# need to report the failures
make functionaltest || :
popd


%files -f nvim.lang
%doc BACKERS.md CONTRIBUTING.md ISSUE_TEMPLATE.md LICENSE README.md
%{_bindir}/*
%{_datadir}/nvim/
%{_mandir}/man1/*.1*

%files x11
%{_datadir}/applications/nvim.desktop
%{_datadir}/pixmaps/nvim.png


%post x11
update-desktop-database &> /dev/null ||:

%postun x11
update-desktop-database &> /dev/null ||:


%changelog
* Wed Nov 08 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.1-2.git20171108.e98bcf0
- Don't require jemalloc for building

* Wed Nov 08 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.1-1.git20171108.e98bcf0
- Update to latest git snapshot

* Fri Nov 03 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.0-6.git20171103.739bc51
- Update to latest git snapshot

* Sat Oct 28 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.0-5.git20171028.1de5b04
- Update to latest git snapshot
- Require git for building

* Sun Aug 27 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.0-4.git20170827.5566f3000
- Add post/postun scriptlets for neovim-x11

* Sun Aug 27 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.0-3.git20170827.5566f3000
- Update to latest git snapshot

* Thu Jul 20 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.0-2.git20170720.c40093f47
- Update source to c40093f47
- Pass -DCMAKE_BUILD_TYPE=RelWithDebInfo to make :CheckHealth happy

* Wed Jul 12 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.2.0-1.git20170712.837037383
- Update source to 837037383
- Drop upstreamed neovim-busted-force-lua-prg.patch
- Require gperf for building

* Sat Jun 04 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.5-4.git20160604.02e6914
- Update source to 02e6914
- Add patch which forces selected lua program to be used in tests
- Run all available tests

* Thu May 19 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.5-3.git20160519.9c7038c
- Update source to 9c7038c

* Thu May 12 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.5-2.git20160512.d02cfe8
- Update source to d02cfe8

* Fri Apr 29 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.5-1.git20160429.126e475
- Update source to 126e475
- Don't require lua-bitop for build

* Sun Apr 24 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.4-2.git20160424.1cc869f
- Update source to 1cc869f

* Sat Apr 16 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.4-1.git20160416.4eb5827
- Public release
