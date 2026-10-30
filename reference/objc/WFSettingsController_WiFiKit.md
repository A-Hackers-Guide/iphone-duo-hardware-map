# `WFSettingsController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFNetworkSettingsViewControllerDataCoordinator`
- 11 instance variables, 15 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _monitorIPChanges;
B _cloudSyncRunning;
B _currentNetwork;
@"WFNetworkSettingsViewController" _settingsViewController;
@"WFNetworkSettingsConfig" _config;
@"WFIPMonitor" _ipMonitor;
@"NSOperationQueue" _queue;
@"WFDetailsContext" _detailsContext;
@"WFNetworkScanRecord" _network;
@"NSString" _hardwareMACAddress;
@"WFAppearanceProxy" _appearanceProxy;
```

## Properties

```
@property (T@"WFNetworkSettingsConfig",&,N,V_config) config;
@property (T@"WFNetworkSettingsViewController",&,N,V_settingsViewController) settingsViewController;
@property (TB,N,V_monitorIPChanges) monitorIPChanges;
@property (T@"WFIPMonitor",&,N,V_ipMonitor) ipMonitor;
@property (T@"NSOperationQueue",&,N,V_queue) queue;
@property (TB,N,V_cloudSyncRunning) cloudSyncRunning;
@property (T@"WFDetailsContext",&,N,V_detailsContext) detailsContext;
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (TB,N,GisCurrentNetwork,V_currentNetwork) currentNetwork;
@property (T@"NSString",&,N,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"WFAppearanceProxy",&,N,V_appearanceProxy) appearanceProxy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFSettingsController hardwareMACAddress];
-[WFSettingsController setCurrentNetwork:];
-[WFSettingsController setSettingsViewController:];
-[WFSettingsController config];
-[WFSettingsController setConfig:];
-[WFSettingsController network];
-[WFSettingsController dealloc];
-[WFSettingsController queue];
-[WFSettingsController appearanceProxy];
-[WFSettingsController settingsViewController];
-[WFSettingsController setIpMonitor:];
-[WFSettingsController setQueue:];
-[WFSettingsController ipMonitor];
-[WFSettingsController setNetwork:];
-[WFSettingsController _applySetupAppearances];
-[WFSettingsController _baseConfigForNetwork:current:];
-[WFSettingsController _currentNetworkDidChange:];
-[WFSettingsController _ipStateDidChange:];
-[WFSettingsController _refreshSettingsConfig:];
-[WFSettingsController _startMontoringIPChanges];
-[WFSettingsController _stopMonitoringIPChanges];
-[WFSettingsController cloudSyncRunning];
-[WFSettingsController detailsContext];
-[WFSettingsController initWithDetailsContext:];
-[WFSettingsController initWithDetailsContext:appearanceProxy:];
-[WFSettingsController isCurrentNetwork];
-[WFSettingsController monitorIPChanges];
-[WFSettingsController networkSettingsViewController:saveConfig:errorHandler:];
-[WFSettingsController setAppearanceProxy:];
-[WFSettingsController setCloudSyncRunning:];
-[WFSettingsController setDetailsContext:];
-[WFSettingsController setHardwareMACAddress:];
-[WFSettingsController setMonitorIPChanges:];
```
