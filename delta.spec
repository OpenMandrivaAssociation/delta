%define debug_package %{nil}

Name: delta
Version: 2006.08.03
Release: 1
Source0: http://delta.tigris.org/files/documents/3103/33566/%{name}-%{version}.tar.gz
Summary: Tool for heuristically minimizing interesting files
URL: http://delta.tigris.org/
License: BSD
Group: Development/Tools

%description
Delta assists you in minimizing "interesting" files subject to a test
of their interestingness. A common such situation is when attempting
to isolate a small failure-inducing substring of a large input that
causes your program to exhibit a bug.

This implementation is based on the Delta Debugging algorithm.

%prep
%setup -q

%build
%make CC=%{__cc}

%check
%make check

%install
mkdir -p %{buildroot}%{_bindir}
cp -a delta multidelta topformflat %{buildroot}%{_bindir}/

%files
%{_bindir}/*
