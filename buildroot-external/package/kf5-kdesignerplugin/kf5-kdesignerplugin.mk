################################################################################
#
# kf5-kdesignerplugin
#
################################################################################

KF5_KDESIGNERPLUGIN_VERSION = $(KF5_VERSION)
KF5_KDESIGNERPLUGIN_SITE = $(KF5_SITE)/portingAids
KF5_KDESIGNERPLUGIN_SOURCE = kdesignerplugin-$(KF5_KDESIGNERPLUGIN_VERSION).tar.xz
KF5_KDESIGNERPLUGIN_LICENSE = BSD-3-Clause
KF5_KDESIGNERPLUGIN_LICENSE_FILES = COPYING-CMAKE-SCRIPTS

KF5_KDESIGNERPLUGIN_DEPENDENCIES = host-pkgconf host-kf5-kdesignerplugin
KF5_KDESIGNERPLUGIN_INSTALL_STAGING = YES
KF5_KDESIGNERPLUGIN_SUPPORTS_IN_SOURCE_BUILD = NO

KF5_KDESIGNERPLUGIN_CONF_OPTS += -DKF5_HOST_TOOLING="$(HOST_DIR)/lib/x86_64-linux-gnu/cmake"

$(eval $(cmake-package))

HOST_KF5_KDESIGNERPLUGIN_DEPENDENCIES = host-kf5-extra-cmake-modules
HOST_KF5_KDESIGNERPLUGIN_CXXFLAGS = $(HOST_CXXFLAGS)
HOST_KF5_KDESIGNERPLUGIN_CONF_OPTS = -DCMAKE_CXX_FLAGS="$(HOST_KF5_KDESIGNERPLUGIN_CXXFLAGS)"

$(eval $(host-cmake-package))
