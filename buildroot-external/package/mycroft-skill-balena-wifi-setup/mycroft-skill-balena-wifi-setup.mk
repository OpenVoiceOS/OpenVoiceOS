################################################################################
#
# mycroft-skill-balena-wifi-setup
#
################################################################################

MYCROFT_SKILL_BALENA_WIFI_SETUP_VERSION = ee7a2f985967c7bd8ed912fb37375c8046bb2230
MYCROFT_SKILL_BALENA_WIFI_SETUP_SITE = git://github.com/OpenVoiceOS/skill-balena-wifi-setup
MYCROFT_SKILL_BALENA_WIFI_SETUP_SITE_METHOD = git
MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRLOCATION = opt/mycroft/skills
MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRNAME = skill-balena-wifi-setup

define MYCROFT_SKILL_BALENA_WIFI_SETUP_INSTALL_TARGET_CMDS
	mkdir -p $(TARGET_DIR)/$(MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRLOCATION)/$(MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRNAME)
	cp -dpfr $(@D)/* $(TARGET_DIR)/$(MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRLOCATION)/$(MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRNAME)
	cp -dpfr $(MYCROFT_SKILL_BALENA_WIFI_SETUP_DL_DIR)/git/.git* \
		$(TARGET_DIR)/$(MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRLOCATION)/$(MYCROFT_SKILL_BALENA_WIFI_SETUP_DIRNAME)
endef

$(eval $(generic-package))
