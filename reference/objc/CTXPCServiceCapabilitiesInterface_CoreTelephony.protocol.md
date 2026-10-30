# `CTXPCServiceCapabilitiesInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance methods

```
-[CTXPCServiceCapabilitiesInterface context:getSystemCapabilities:];
-[CTXPCServiceCapabilitiesInterface context:addPhoneServicesDevice:withCompletion:];
-[CTXPCServiceCapabilitiesInterface context:canSetCapability:completion:];
-[CTXPCServiceCapabilitiesInterface context:getCapability:completion:];
-[CTXPCServiceCapabilitiesInterface context:isMandatoryDisabledVoLTE:];
-[CTXPCServiceCapabilitiesInterface context:mandatoryDisableVoLTE:withCompletion:];
-[CTXPCServiceCapabilitiesInterface context:recheckPhoneServicesAccountStatus:completion:];
-[CTXPCServiceCapabilitiesInterface context:removePhoneServicesDevice:withCompletion:];
-[CTXPCServiceCapabilitiesInterface context:setCapability:enabled:info:completion:];
-[CTXPCServiceCapabilitiesInterface getPhoneServicesDeviceInfo:];
-[CTXPCServiceCapabilitiesInterface getPhoneServicesDeviceList:];
-[CTXPCServiceCapabilitiesInterface getSupports5G:completion:];
-[CTXPCServiceCapabilitiesInterface wifiCallingCTFollowUpComplete:withCompletion:];
```
