# `SBSystemStatusStatusItemsDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayReferenceModeStatusObserver`, `BSInvalidatable`, `SBWindowSceneAttachmentObserving`
- 8 instance variables, 11 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _displayReferenceModeWindowScenes;
B _alarmEnabled;
@"NSMapTable" _dataProvidersByIdentifier;
@"SBDisplayReferenceModeMonitor" _displayReferenceModeMonitor;
@"SBTelephonyManager" _telephonyManager;
@"SBAirplaneModeController" _airplaneModeController;
@"STTelephonyStatusDomain" _telephonyStatusDomain;
@"STWifiStatusDomain" _wifiStatusDomain;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_dataProvidersByIdentifier) dataProvidersByIdentifier;
@property (T@"SBDisplayReferenceModeMonitor",R,N,V_displayReferenceModeMonitor) displayReferenceModeMonitor;
@property (T@"SBTelephonyManager",R,N,V_telephonyManager) telephonyManager;
@property (T@"SBAirplaneModeController",R,N,V_airplaneModeController) airplaneModeController;
@property (T@"STTelephonyStatusDomain",R,N,V_telephonyStatusDomain) telephonyStatusDomain;
@property (T@"STWifiStatusDomain",R,N,V_wifiStatusDomain) wifiStatusDomain;
@property (TB,N,GisAlarmEnabled,V_alarmEnabled) alarmEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemStatusStatusItemsDataProvider displayReferenceModeStatusDidChangeForDisplayWithConfiguration:newStatus:];
-[SBSystemStatusStatusItemsDataProvider _registerForNotifications];
-[SBSystemStatusStatusItemsDataProvider windowSceneDidDisconnect:];
-[SBSystemStatusStatusItemsDataProvider dealloc];
-[SBSystemStatusStatusItemsDataProvider telephonyManager];
-[SBSystemStatusStatusItemsDataProvider invalidate];
-[SBSystemStatusStatusItemsDataProvider setAlarmEnabled:];
-[SBSystemStatusStatusItemsDataProvider airplaneModeController];
-[SBSystemStatusStatusItemsDataProvider windowSceneDidConnect:];
-[SBSystemStatusStatusItemsDataProvider isAlarmEnabled];
-[SBSystemStatusStatusItemsDataProvider _identifiersForSupportedStatusItems];
-[SBSystemStatusStatusItemsDataProvider _isDisplayWarningItemEnabled];
-[SBSystemStatusStatusItemsDataProvider _isVPNItemEnabled];
-[SBSystemStatusStatusItemsDataProvider _updateAllData];
-[SBSystemStatusStatusItemsDataProvider _updateDataForAirPlay];
-[SBSystemStatusStatusItemsDataProvider _updateDataForAirplaneMode];
-[SBSystemStatusStatusItemsDataProvider _updateDataForAlarm];
-[SBSystemStatusStatusItemsDataProvider _updateDataForCarPlay];
-[SBSystemStatusStatusItemsDataProvider _updateDataForDisplayWarning];
-[SBSystemStatusStatusItemsDataProvider _updateDataForRotationLock];
-[SBSystemStatusStatusItemsDataProvider _updateDataForStatusItemsWithIdentifiers:];
-[SBSystemStatusStatusItemsDataProvider _updateDataForTTY];
-[SBSystemStatusStatusItemsDataProvider _updateDataForVPN];
-[SBSystemStatusStatusItemsDataProvider _wantsAttributionForStatusItemWithIdentifier:];
-[SBSystemStatusStatusItemsDataProvider dataProvidersByIdentifier];
-[SBSystemStatusStatusItemsDataProvider displayReferenceModeMonitor];
-[SBSystemStatusStatusItemsDataProvider initWithServerHandle:telephonyManager:airplaneModeController:];
-[SBSystemStatusStatusItemsDataProvider telephonyStatusDomain];
-[SBSystemStatusStatusItemsDataProvider wifiStatusDomain];
```
