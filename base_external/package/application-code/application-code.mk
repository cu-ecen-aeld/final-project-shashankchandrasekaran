#TODO: Fill up the contents below in order to reference your assignment 3 git contents
APPLICATION_CODE_VERSION = 'be8615253eb02fef82f5f11631aeb3cbd4aefce6'
# Note: Be sure to reference the *ssh* repository URL here (not https) to work properly
# with ssh keys and the automated build/test system.
# Your site should start with git@github.com:
APPLICATION_CODE_SITE = 'git@github.com:cu-ecen-aeld/final-project-harshberiwal.git'
APPLICATION_CODE_SITE_METHOD = git
APPLICATION_CODE_GIT_SUBMODULES = YES

define APPLICATION_CODE_BUILD_CMDS
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D)/server all
	$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D)/client all
endef

define APPLICATION_CODE_INSTALL_TARGET_CMDS
	$(INSTALL) -m 0755 $(@D)/client/client $(TARGET_DIR)/usr/bin/
	$(INSTALL) -m 0755 $(@D)/server/server $(TARGET_DIR)/usr/bin/
	#Uncomment the below line when building the server image to run the server on startup 
	#$(INSTALL) -m 0755 $(@D)/'init'/S90server.sh $(TARGET_DIR)/etc/init.d/S90server.sh
	#Uncomment the below line when building the client image to run the client on startup 
	#$(INSTALL) -m 0755 $(@D)/init/S91client.sh $(TARGET_DIR)/etc/init.d/S91client.sh
endef

$(eval $(generic-package))
