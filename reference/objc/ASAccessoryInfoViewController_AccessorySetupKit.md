# `ASAccessoryInfoViewController`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 10 instance variables, 0 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"DASession" _session;
@"DADevice" _device;
B _useAsHeader;
@"ASAccessoryInfoHeaderCell" _headerCell;
B _supportsWAPI;
B _didDismiss;
B _companionAppLoaded;
q _companionResolution;
B _companionResolutionStarted;
@"ASAccessoryCompanionAppInfo" _resolvedCompanionAppInfo;
```

## Class methods

```
+[ASAccessoryInfoViewController companionSpecifiersFromList:insertIndex:];
```

## Instance methods

```
-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:];
-[ASAccessoryInfoViewController initWithDevice:];
-[ASAccessoryInfoViewController init];
-[ASAccessoryInfoViewController viewDidLoad];
-[ASAccessoryInfoViewController viewWillAppear:];
-[ASAccessoryInfoViewController unpairDevice:];
-[ASAccessoryInfoViewController preferredContentSize];
-[ASAccessoryInfoViewController specifiers];
-[ASAccessoryInfoViewController forgetDevice:];
-[ASAccessoryInfoViewController isAppAllowed:];
-[ASAccessoryInfoViewController setAppAllowed:specifier:];
-[ASAccessoryInfoViewController shouldReloadSpecifiersOnResume];
-[ASAccessoryInfoViewController specifiersForHeader];
-[ASAccessoryInfoViewController buildSpecifiers];
-[ASAccessoryInfoViewController specifiersForForgetDeviceButton];
-[ASAccessoryInfoViewController specifiersForUnpairedDisclaimer];
-[ASAccessoryInfoViewController specifiersForUnpairDeviceButton];
-[ASAccessoryInfoViewController specifiersForWiFiSharingSection];
-[ASAccessoryInfoViewController unpairedString:];
-[ASAccessoryInfoViewController companionAppSpecifiers:];
-[ASAccessoryInfoViewController deviceName:];
-[ASAccessoryInfoViewController footerStringForAccessoryForwardingWithNotificationsEnabled:andLiveActivitiesEnabled:];
-[ASAccessoryInfoViewController getAudioRoutingEnabled:];
-[ASAccessoryInfoViewController handleDAEvent:];
-[ASAccessoryInfoViewController isDeviceArchived];
-[ASAccessoryInfoViewController notificationsAuthString:];
-[ASAccessoryInfoViewController openApp:];
-[ASAccessoryInfoViewController openNotificationsSettings:];
-[ASAccessoryInfoViewController pushForwardingSettings:];
-[ASAccessoryInfoViewController resetWiFiIdentifier:];
-[ASAccessoryInfoViewController resolveCompanionAppIfNeeded:];
-[ASAccessoryInfoViewController revealCompanionSectionAnimated];
-[ASAccessoryInfoViewController setAudioRoutingEnabled:specifier:];
-[ASAccessoryInfoViewController specifiersForAccessoryForwardingSection];
-[ASAccessoryInfoViewController specifiersForAppAccessSection];
-[ASAccessoryInfoViewController specifiersForArchivedDevice];
-[ASAccessoryInfoViewController specifiersForAudioRoutingSection];
-[ASAccessoryInfoViewController specifiersForOpenAppButton:];
-[ASAccessoryInfoViewController specifiersForPairedDevice];
-[ASAccessoryInfoViewController specifiersForRenameSection];
-[ASAccessoryInfoViewController specifiersForResetWiFiButton];
-[ASAccessoryInfoViewController viewCompanionAppInBrowser:];
-[ASAccessoryInfoViewController wifiSharingAuthString:];
```
