#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hold
Version  : 0.1.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/a4/b7/86fdc306647d16e6e1f1a69b25c95a42ee30e7efb83a48c27d543c5edf8a/hold-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a4/b7/86fdc306647d16e6e1f1a69b25c95a42ee30e7efb83a48c27d543c5edf8a/hold-0.1.0.tar.gz
Summary  : Hold methods for effective works
Group    : Development/Tools
License  : MIT
Requires: hold-python3
Requires: hold-python
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the hold package.
Group: Default
Requires: hold-python3

%description python
python components for the hold package.


%package python3
Summary: python3 components for the hold package.
Group: Default
Requires: python3-core

%description python3
python3 components for the hold package.


%prep
%setup -q -n hold-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537291207
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
