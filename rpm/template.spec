Name:           ros-kinetic-librealsense
Version:        0.9.2
Release:        2%{?dist}
Summary:        ROS librealsense package

Group:          Development/Libraries
License:        Apache License, Version 2.0
URL:            https://github.com/IntelRealSense/librealsense/
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx-devel
BuildRequires:  libusbx-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-kinetic-catkin

%description
This project is a cross-platform library (Linux, OSX, Windows) for capturing
data from the Intel(R) RealSense(TM) F200, SR300 and R200 cameras. This effort
was initiated to better support researchers, creative coders, and app developers
in domains such as robotics, virtual reality, and the internet of things.
Several often-requested features of RealSense(TM); devices are implemented in
this project, including multi-camera capture.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jul 11 2016 Sergey Dorodnicov <sergey.dorodnicov@intel.com> - 0.9.2-2
- Autogenerated by Bloom

* Thu Jun 30 2016 Sergey Dorodnicov <sergey.dorodnicov@intel.com> - 0.9.2-1
- Autogenerated by Bloom

* Mon Jun 27 2016 Sergey Dorodnicov <sergey.dorodnicov@intel.com> - 0.9.2-0
- Autogenerated by Bloom

