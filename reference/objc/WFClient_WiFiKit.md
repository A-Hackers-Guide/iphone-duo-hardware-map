# `WFClient`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 33 properties, 114 instance methods, 1 class methods

## Instance variables

```
B _networkRestrictionActive;
B _powered;
B _isKnownNetworkUIEnabled;
B _WAPIEnabled;
B _diagnosticsEnabled;
B _WPA3PersonalEnabled;
B _WPA3EnterpriseEnabled;
B _mfpCapable;
B _powerModificationDisabled;
B _managedAppleID;
B _showAllHS20Networks;
B _wiFiHealthUIDisabled;
B _extraLoggingEnabled;
B _diagnosticsModeEnabled;
B _nanUIEnabled;
B _userAutoJoinState;
B _lockdownModeEnabled;
i _cellularOutrankWiFiNotificationToken;
Q _airplaneModeBehavior;
@"NSString" _whitelistingUUID;
Q _wifiUIStateFlags;
q _askToJoinMode;
q _autoInstantHotspotJoinOption;
@"WFInterface" _interface;
@"CWFInterface" _cInterface;
^{__WiFiManagerClient=} _manager;
@"NSRunLoop" _callbackRunLoop;
@"NSNumber" _rssiThresholdNumber;
@"NSObject<OS_dispatch_queue>" _serialClientQueue;
@"NSObject<OS_dispatch_queue>" _stateMonitorQueue;
Q _cellularOutrankWiFiSymtpomsState;
Q _cellularOutrankState;
```

## Properties

```
@property (T@"WFInterface",&,N,V_interface) interface;
@property (T@"CWFInterface",&,N,V_cInterface) cInterface;
@property (T^{__WiFiManagerClient=},V_manager) manager;
@property (T@"NSRunLoop",&,V_callbackRunLoop) callbackRunLoop;
@property (TB,V_showAllHS20Networks) showAllHS20Networks;
@property (TB,GisWiFiHealthUIDisabled,V_wiFiHealthUIDisabled) wiFiHealthUIDisabled;
@property (TB,V_extraLoggingEnabled) extraLoggingEnabled;
@property (TB,GisDiagnosticsModeEnabled,V_diagnosticsModeEnabled) diagnosticsModeEnabled;
@property (TB,GisNANUIEnabled,V_nanUIEnabled) nanUIEnabled;
@property (TB,N,GisNetworkRestrictionActive,V_networkRestrictionActive) networkRestrictionActive;
@property (T@"NSNumber",&,V_rssiThresholdNumber) rssiThresholdNumber;
@property (TB,R,N,V_isKnownNetworkUIEnabled) isKnownNetworkUIEnabled;
@property (TQ,N,V_airplaneModeBehavior) airplaneModeBehavior;
@property (TB,N,V_userAutoJoinState) userAutoJoinState;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_serialClientQueue) serialClientQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_stateMonitorQueue) stateMonitorQueue;
@property (T@"NSString",R,N,V_whitelistingUUID) whitelistingUUID;
@property (TB,N,GisWPA3PersonalEnabled,V_WPA3PersonalEnabled) WPA3PersonalEnabled;
@property (TB,N,GisWPA3EnterpriseEnabled,V_WPA3EnterpriseEnabled) WPA3EnterpriseEnabled;
@property (TB,N,GisMfpCapable,V_mfpCapable) mfpCapable;
@property (TB,N,GisManagedAppleID,V_managedAppleID) managedAppleID;
@property (TB,N,V_lockdownModeEnabled) lockdownModeEnabled;
@property (Ti,N,V_cellularOutrankWiFiNotificationToken) cellularOutrankWiFiNotificationToken;
@property (TQ,N,V_cellularOutrankWiFiSymtpomsState) cellularOutrankWiFiSymtpomsState;
@property (TQ,N,V_cellularOutrankState) cellularOutrankState;
@property (TB,V_powered) powered;
@property (TQ,V_wifiUIStateFlags) wifiUIStateFlags;
@property (T@"NSString",R) hardwareMACAddress;
@property (TB,N,GisWAPIEnabled,V_WAPIEnabled) WAPIEnabled;
@property (TB,N,GisDiagnosticsEnabled,V_diagnosticsEnabled) diagnosticsEnabled;
@property (Tq,N,V_askToJoinMode) askToJoinMode;
@property (TB,R,N,GisPowerModificationDisabled,V_powerModificationDisabled) powerModificationDisabled;
@property (Tq,N,V_autoInstantHotspotJoinOption) autoInstantHotspotJoinOption;
```

## Class methods

```
+[WFClient sharedInstance];
```

## Instance methods

```
-[WFClient hardwareMACAddress];
-[WFClient powered];
-[WFClient isManagedAppleID];
-[WFClient setManagedAppleID:];
-[WFClient _hotspotJoinOptionFromCoreWiFiAutoHotspotMode:];
-[WFClient setPowered:];
-[WFClient setUserAutoJoinState:];
-[WFClient _notifyWiFiPropertyChanged:value:];
-[WFClient setWPA3EnterpriseEnabled:];
-[WFClient askToJoinMode];
-[WFClient airplaneModeBehavior];
-[WFClient _setupDefaultInterfaceWithManager:coreWiFiInterface:];
-[WFClient setMISDiscoveryState:immediateDisable:];
-[WFClient setPoweredToggle:handler:];
-[WFClient setWPA3PersonalEnabled:];
-[WFClient dispatchJoinRecommendationAction:profile:];
-[WFClient wifiUIStateFlags];
-[WFClient setCellularOutrankState:];
-[WFClient setPowerModificationDisableState:];
-[WFClient isNANUIEnabled];
-[WFClient serialClientQueue];
-[WFClient setAutoJoinEnabled:];
-[WFClient setHasShownSBPickerDontAsk:];
-[WFClient isPowerModificationDisabled];
-[WFClient setStateMonitorQueue:];
-[WFClient asyncPowered:];
-[WFClient _askToJoinModeFromCoreWiFiAskToJoinMode:];
-[WFClient _updateWithDeviceAttachment:];
-[WFClient isInfraAssociationAllowed];
-[WFClient setAskToJoinMode:];
-[WFClient isWAPIEnabled];
-[WFClient setExtraLoggingEnabled:];
-[WFClient init];
-[WFClient _registerForCellularRankingStateNotification];
-[WFClient _updateAirplaneModeStickiness];
-[WFClient setManager:];
-[WFClient setAutoInstantHotspotJoinOption:];
-[WFClient setCallbackRunLoop:];
-[WFClient dealloc];
-[WFClient asyncMISState:];
-[WFClient isWPA3PersonalEnabled];
-[WFClient userAutoJoinState];
-[WFClient _userAutoJoinStateDidChange:info:];
-[WFClient _updatePowerState];
-[WFClient asyncUserAutoJoinState:];
-[WFClient cellularOutrankWiFiSymtpomsState];
-[WFClient setInterface:];
-[WFClient setNetworkRestrictionActive:];
-[WFClient extraLoggingEnabled];
-[WFClient manager];
-[WFClient initWithCallbackRunLoop:];
-[WFClient _coreWiFiAskToJoinModeFromAskToJoinMode:];
-[WFClient setMfpCapable:];
-[WFClient setCellularOutrankWiFiSymtpomsState:];
-[WFClient cellularOutrankWiFiNotificationToken];
-[WFClient setCInterface:];
-[WFClient setUserAutoJoinState:completion:];
-[WFClient _managedConfigurationDidChange:];
-[WFClient lockdownModeEnabled];
-[WFClient _askToJoinNotification:];
-[WFClient isWiFiHealthUIDisabled];
-[WFClient _unscheduleCallbacksWithManager:];
-[WFClient interface];
-[WFClient dispatchCertificateTrustAction:profile:];
-[WFClient setSerialClientQueue:];
-[WFClient rssiThresholdNumber];
-[WFClient showAllHS20Networks];
-[WFClient stateMonitorQueue];
-[WFClient setDiagnosticsModeEnabled:];
-[WFClient setRandomAddressModeForNetwork:mode:randomMAC:];
-[WFClient setNanUIEnabled:];
-[WFClient _updatePowerModificationDisableState];
-[WFClient isWPA3EnterpriseEnabled];
-[WFClient _managedAppleIDStateDidChange:];
-[WFClient cInterface];
-[WFClient _joinRecommendationWithID:network:];
-[WFClient autoInstantHotspotJoinOption];
-[WFClient asyncMISDiscoveryState:];
-[WFClient _trustNotificationWithID:network:data:];
-[WFClient _updateNetworkRestrictionActive];
-[WFClient setWAPIEnabled:];
-[WFClient _updateOSSpecificAttributes:];
-[WFClient isMfpCapable];
-[WFClient _updateWPA3Properties:];
-[WFClient _updateCellularRankingState];
-[WFClient cellularOutrankState];
-[WFClient _coreWiFiHotspotJoinOptionFromAutoHotspotMode:];
-[WFClient isNetworkRestrictionActive];
-[WFClient setShowAllHS20Networks:];
-[WFClient setAirplaneModeBehavior:];
-[WFClient isDiagnosticsEnabled];
-[WFClient isDiagnosticsModeEnabled];
-[WFClient reloadConfiguration];
-[WFClient setWifiUIStateFlags:];
-[WFClient isCellularOutrankingWiFi];
-[WFClient _startMonitoringCoreWiFiEventsWithInterface:];
-[WFClient whitelistingUUID];
-[WFClient _logWiFiManagerPropertyChange:value:];
-[WFClient newRandomMACAddressForSSID:];
-[WFClient setDiagnosticsEnabled:];
-[WFClient callbackRunLoop];
-[WFClient setClientTypeAsForeground];
-[WFClient setMISState:];
-[WFClient setCellularOutrankWiFiNotificationToken:];
-[WFClient isKnownNetworkUIEnabled];
-[WFClient hasShownSBPickerDontAsk];
-[WFClient _scheduleCallbacksWithManager:runLoop:];
-[WFClient setWiFiHealthUIDisabled:];
-[WFClient setEnableRandomMACForNetwork:enable:randomMAC:];
-[WFClient setRssiThresholdNumber:];
-[WFClient dispatchAskToJoinAction:notificationId:network:];
-[WFClient setLockdownModeEnabled:];
-[WFClient _updateWiFiUIFlagsState];
-[WFClient _updateManagedAppleIDState];
```
