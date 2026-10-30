# `CTXPCServiceCarrierBundleInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance methods

```
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValue:key:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface checkForUpdatedBundlesWithAutoInstall:completion:];
-[CTXPCServiceCarrierBundleInterface context:getAttachApnSettingsWithCompletion:];
-[CTXPCServiceCarrierBundleInterface context:modifyAttachApnSettings:completion:];
-[CTXPCServiceCarrierBundleInterface copyBundleIdentifier:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface copyBundleLocation:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface copyBundleVersion:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBookmarks:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleLocation:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValue:keyHierarchy:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValueWithCountryBundleLookup:keyHierarchy:matchingInfo:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValueWithDefault:key:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValueWithDefault:keyHierarchy:bundleType:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValues:keyHierarchies:defaultValues:bundleType:withFallbackBundleCheck:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleValues:keys:defaultValues:bundleType:withFallbackBundleCheck:completion:];
-[CTXPCServiceCarrierBundleInterface copyCarrierBundleVersion:completion:];
-[CTXPCServiceCarrierBundleInterface getCountryBundleIdentifierForCountryCode:completion:];
-[CTXPCServiceCarrierBundleInterface getCountryBundleLocationForBundleIdentifier:completion:];
-[CTXPCServiceCarrierBundleInterface getCountryBundleLocationForMatchingInfo:completion:];
-[CTXPCServiceCarrierBundleInterface getEnglishCarrierNameFor:completion:];
-[CTXPCServiceCarrierBundleInterface getWiFiCallingSettingPreferences:key:completion:];
-[CTXPCServiceCarrierBundleInterface isAttachApnSettingAllowed:completion:];
-[CTXPCServiceCarrierBundleInterface restoreToSystemBundles:];
-[CTXPCServiceCarrierBundleInterface setWiFiCallingSettingPreferences:key:value:completion:];
```
