%global commit 4eb5827
%global vermagic 0.1.4
%global gitdescribe %{vermagic}-40-g%{commit}
%global snapshot .git20160416.%{commit}

Name:           neovim
Version:        %{vermagic}
Release:        1%{snapshot}%{?dist}
Summary:        Drop-in replacement for Vim

License:        Apache License, Version 2.0; and Vim license
URL:            https://neovim.io/

# git clone https://github.com/neovim/neovim
# cd neovim
# git archive --prefix=neovim/ master | bzip2 >../neovim.tar.bz2
Source0:        neovim.tar.bz2

BuildRequires:  cmake >= 2.8.7
BuildRequires:  gettext
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(unibilium)
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(vterm)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(msgpack)
BuildRequires:  lua-lpeg
BuildRequires:  lua-mpack
BuildRequires:  lua-bitop

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


%build
mkdir buildrpm
pushd buildrpm
%{cmake} -DUSE_BUNDLED:BOOL=OFF ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd buildrpm
%make_install
popd
%find_lang nvim


%files -f nvim.lang
%doc BACKERS.md CONTRIBUTING.md ISSUE_TEMPLATE.md LICENSE README.md
%{_bindir}/*
%{_datadir}/nvim/
%{_mandir}/man1/*.1*

%files x11


%changelog
* Sat Apr 16 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.4-1.git20160416.4eb5827
- Public release
