# `SBStatusBarStateAggregator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneAttachmentObserving`, `SBAVSystemControllerCacheObserver`, `CBCentralManagerPrivateDelegate`, `SBFSensorActivityObserver`
- 78 instance variables, 27 properties, 134 instance methods, 1 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBTelephonyManager" _telephonyManager;
@"SBStatusBarDefaults" _statusBarDefaults;
@"SBUserSessionController" _userSessionController;
@"SBSensorActivityDataProvider" _sensorActivityDataProvider;
@"SBBluetoothController" _bluetoothController;
@"SBAirplaneModeController" _airplaneModeController;
@"SBThermalController" _thermalController;
@"SBWiFiManager" _wifiManager;
Q _coalescentBlockDepth;
B _hasPostedOnce;
[46Q] _itemPostState;
B _nonItemDataChanged;
{?="itemIsEnabled"[46B]"timeString"[64c]"shortTimeString"[64c]"dateString"[256c]"gsmSignalStrengthRaw"i"secondaryGsmSignalStrengthRaw"i"gsmSignalStrengthBars"i"secondaryGsmSignalStrengthBars"i"serviceString"[100c]"secondaryServiceString"[100c]"serviceCrossfadeString"[100c]"secondaryServiceCrossfadeString"[100c]"serviceImages"[2[100c]]"operatorDirectory"[1024c]"serviceContentType"I"secondaryServiceContentType"I"cellLowDataModeActive"b1"secondaryCellLowDataModeActive"b1"wifiSignalStrengthRaw"i"wifiSignalStrengthBars"i"wifiLowDataModeActive"b1"dataNetworkType"I"secondaryDataNetworkType"I"batteryCapacity"i"batteryState"I"batteryDetailString"[150c]"bluetoothBatteryCapacity"i"thermalColor"i"thermalSunlightMode"b1"slowActivity"b1"syncActivity"b1"activityDisplayId"[256c]"bluetoothConnected"b1"displayRawGSMSignal"b1"displayRawWifiSignal"b1"locationIconType"b2"voiceControlIconType"b2"quietModeInactive"b1"tetheringConnectionCount"I"batterySaverModeActive"b1"deviceIsRTL"b1"lock"b1"breadcrumbTitle"[256c]"breadcrumbSecondaryTitle"[256c]"personName"[100c]"electronicTollCollectionAvailable"b1"radarAvailable"b1"announceNotificationsAvailable"b1"wifiLinkWarning"b1"wifiSearching"b1"backgroundActivityDisplayStartDate"d"shouldShowEmergencyOnlyStatus"b1"emergencyOnly"b1"secondaryCellularConfigured"b1"primaryServiceBadgeString"[100c]"secondaryServiceBadgeString"[100c]"quietModeImage"[256c]"quietModeName"[256c]"serviceSuffixString"[100c]"secondaryServiceSuffixString"[100c]"numberSharingState"b2"secondaryNumberSharingState"b2"localNetworkType"I"localNetworkName"[100c]} _data;
i _actions;
B _performingAtomicUpdate;
[46Q] _atomicUpdateItemPostState;
{?="itemIsEnabled"[46B]"timeString"[64c]"shortTimeString"[64c]"dateString"[256c]"gsmSignalStrengthRaw"i"secondaryGsmSignalStrengthRaw"i"gsmSignalStrengthBars"i"secondaryGsmSignalStrengthBars"i"serviceString"[100c]"secondaryServiceString"[100c]"serviceCrossfadeString"[100c]"secondaryServiceCrossfadeString"[100c]"serviceImages"[2[100c]]"operatorDirectory"[1024c]"serviceContentType"I"secondaryServiceContentType"I"cellLowDataModeActive"b1"secondaryCellLowDataModeActive"b1"wifiSignalStrengthRaw"i"wifiSignalStrengthBars"i"wifiLowDataModeActive"b1"dataNetworkType"I"secondaryDataNetworkType"I"batteryCapacity"i"batteryState"I"batteryDetailString"[150c]"bluetoothBatteryCapacity"i"thermalColor"i"thermalSunlightMode"b1"slowActivity"b1"syncActivity"b1"activityDisplayId"[256c]"bluetoothConnected"b1"displayRawGSMSignal"b1"displayRawWifiSignal"b1"locationIconType"b2"voiceControlIconType"b2"quietModeInactive"b1"tetheringConnectionCount"I"batterySaverModeActive"b1"deviceIsRTL"b1"lock"b1"breadcrumbTitle"[256c]"breadcrumbSecondaryTitle"[256c]"personName"[100c]"electronicTollCollectionAvailable"b1"radarAvailable"b1"announceNotificationsAvailable"b1"wifiLinkWarning"b1"wifiSearching"b1"backgroundActivityDisplayStartDate"d"shouldShowEmergencyOnlyStatus"b1"emergencyOnly"b1"secondaryCellularConfigured"b1"primaryServiceBadgeString"[100c]"secondaryServiceBadgeString"[100c]"quietModeImage"[256c]"quietModeName"[256c]"serviceSuffixString"[100c]"secondaryServiceSuffixString"[100c]"numberSharingState"b2"secondaryNumberSharingState"b2"localNetworkType"I"localNetworkName"[100c]} _atomicUpdateData;
@"NSHashTable" _postObservers;
B _notifyingPostObservers;
q _showsRecordingOverrides;
@"SBFOverridableDateProvider" _dateTimeProvider;
@ _dateTimeProviderToken;
@"NSDateFormatter" _timeItemDateFormatter;
@"NSDateFormatter" _shortTimeItemDateFormatter;
@"NSDateFormatter" _dateItemDateFormatter;
@"NSString" _timeItemTimeString;
@"NSString" _shortTimeItemTimeString;
@"NSString" _dateItemTimeString;
@"NSString" _serviceString;
@"NSString" _serviceCrossfadeString;
@"NSString" _serviceSuffixString;
@"NSString" _secondaryServiceString;
@"NSString" _secondaryServiceCrossfadeString;
@"NSString" _secondaryServiceSuffixString;
@"NSString" _serviceBadgeString;
@"NSString" _secondaryServiceBadgeString;
@"NSString" _localNetworkName;
Q _airplaneTransitionToken;
B _suppressCellServiceForAirplaneModeTransition;
B _cachedShowRSSI;
B _cachedShowThermalWarning;
B _showsActivityIndicatorOnHomeScreen;
q _activityIndicatorEverywhereCount;
q _syncActivityIndicatorCount;
@"NSString" _activityDisplayIdentifier;
@"NSString" _batteryDetailString;
B _shouldShowBluetoothHeadphoneGlyph;
B _shouldShowBluetoothHeadphoneBatteryPercent;
B _alarmEnabled;
B _prominentLocationOverride;
@"NSTimer" _prominentLocationTimer;
B _hasReceivedBatteryDataFromSystemStatus;
@"NSMutableDictionary" _callingBackgroundActivityAssertionsByDescriptor;
@"SBSBackgroundActivityAssertion" _mediaBackgroundActivityAssertion;
@"SBSBackgroundActivityAssertion" _playgroundsBackgroundActivityAssertion;
@"SBSBackgroundActivityAssertion" _satelliteSOSBackgroundActivityAssertion;
@"SBSBackgroundActivityAssertion" _tetheringBackgroundActivityAssertion;
@"NSString" _personName;
@"NSString" _overridePersonName;
@"NSString" _callToActionIdentifier;
@"SBSystemStatusBatteryDataProvider" _batteryDataProvider;
@"SBSystemStatusStatusItemsDataProvider" _statusItemsDataProvider;
@"STTelephonyStatusDomainDataProvider" _telephonyDataProvider;
@"SBSystemStatusWifiDataProvider" _wifiDataProvider;
@"SBSystemStatusStatusBarOverridesArchiver" _statusBarOverridesObserver;
@"STBatteryStatusDomain" _batteryDomain;
@"STCallingStatusDomain" _callingDomain;
@"STFocusStatusDomain" _focusDomain;
@"STPlaygroundsStatusDomain" _playgroundsDomain;
@"STStatusItemsStatusDomain" _statusItemsDomain;
@"STStewieStatusDomain" _stewieDomain;
@"STTelephonyStatusDomain" _telephonyDomain;
@"STVoiceControlStatusDomain" _voiceControlDomain;
@"STWifiStatusDomain" _wifiDomain;
@"NSArray" _systemApertureVisibleElementIdentifiers;
@"<SAInvalidatable>" _systemApertureChargingElementAssertion;
Q _batteryChargingState;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBSensorActivityDataProvider",R,N,V_sensorActivityDataProvider) sensorActivityDataProvider;
@property (T@"SBUserSessionController",R,N,V_userSessionController) userSessionController;
@property (T@"SBSystemStatusBatteryDataProvider",R,N,V_batteryDataProvider) batteryDataProvider;
@property (T@"SBSystemStatusStatusItemsDataProvider",R,N,V_statusItemsDataProvider) statusItemsDataProvider;
@property (T@"STTelephonyStatusDomainDataProvider",R,N,V_telephonyDataProvider) telephonyDataProvider;
@property (T@"SBSystemStatusWifiDataProvider",R,N,V_wifiDataProvider) wifiDataProvider;
@property (T@"SBSystemStatusStatusBarOverridesArchiver",R,N,V_statusBarOverridesObserver) statusBarOverridesObserver;
@property (T@"STBatteryStatusDomain",&,N,V_batteryDomain) batteryDomain;
@property (T@"STCallingStatusDomain",&,N,V_callingDomain) callingDomain;
@property (T@"STFocusStatusDomain",&,N,V_focusDomain) focusDomain;
@property (T@"STPlaygroundsStatusDomain",&,N,V_playgroundsDomain) playgroundsDomain;
@property (T@"STStatusItemsStatusDomain",&,N,V_statusItemsDomain) statusItemsDomain;
@property (T@"STStewieStatusDomain",&,N,V_stewieDomain) stewieDomain;
@property (T@"STTelephonyStatusDomain",&,N,V_telephonyDomain) telephonyDomain;
@property (T@"STVoiceControlStatusDomain",&,N,V_voiceControlDomain) voiceControlDomain;
@property (T@"STWifiStatusDomain",&,N,V_wifiDomain) wifiDomain;
@property (T@"NSArray",&,N,V_systemApertureVisibleElementIdentifiers) systemApertureVisibleElementIdentifiers;
@property (T@"<SAInvalidatable>",&,N,V_systemApertureChargingElementAssertion) systemApertureChargingElementAssertion;
@property (TQ,N,V_batteryChargingState) batteryChargingState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBStatusBarStateAggregator _thermalColorForLevel:];
```

## Instance methods

```
-[SBStatusBarStateAggregator activityDidChangeForSensorActivityDataProvider:];
-[SBStatusBarStateAggregator userSessionController];
-[SBStatusBarStateAggregator setShouldShowBluetoothHeadphoneGlyph:andShouldShowBluetoothHeadphoneBatteryPercent:];
-[SBStatusBarStateAggregator _restartTimeItemTimer];
-[SBStatusBarStateAggregator systemApertureLayoutDidChange:];
-[SBStatusBarStateAggregator sensorActivityDataProvider];
-[SBStatusBarStateAggregator statusBarOverridesObserver];
-[SBStatusBarStateAggregator _stopTimeItemTimer];
-[SBStatusBarStateAggregator _updateCallForwardingItem];
-[SBStatusBarStateAggregator centralManagerDidUpdateState:];
-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:];
-[SBStatusBarStateAggregator _updateTimeItemsWithDate:];
-[SBStatusBarStateAggregator _registerForNotifications];
-[SBStatusBarStateAggregator cache:didUpdatePickableRoutes:];
-[SBStatusBarStateAggregator telephonyDataProvider];
-[SBStatusBarStateAggregator _postItem:withState:inList:];
-[SBStatusBarStateAggregator _updateSignalStrengthItem];
-[SBStatusBarStateAggregator _updateCarPlayItem];
-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:];
-[SBStatusBarStateAggregator _updateVPNItem];
-[SBStatusBarStateAggregator setShowsActivityIndicatorOnHomeScreen:];
-[SBStatusBarStateAggregator _removePlaygroundsBackgroundActivityAssertion];
-[SBStatusBarStateAggregator _updatePersonNameItem];
-[SBStatusBarStateAggregator _systemApertureElementIsVisibleForStatusBarItem:];
-[SBStatusBarStateAggregator focusDomain];
-[SBStatusBarStateAggregator _updateDataNetworkItem:withData:primary:dataNetworkTypeGetter:dataNetworkTypeSetter:];
-[SBStatusBarStateAggregator _statusBarData];
-[SBStatusBarStateAggregator _updateRotationLockItem];
-[SBStatusBarStateAggregator _updateStewieItem];
-[SBStatusBarStateAggregator setBatteryChargingState:];
-[SBStatusBarStateAggregator windowSceneDidDisconnect:];
-[SBStatusBarStateAggregator systemApertureVisibleElementIdentifiers];
-[SBStatusBarStateAggregator _updateDataNetworkItem];
-[SBStatusBarStateAggregator _updateBluetoothItem];
-[SBStatusBarStateAggregator _notifyNonItemDataChanged];
-[SBStatusBarStateAggregator _updateStatusBarForSystemStatusDomainName:data:];
-[SBStatusBarStateAggregator _updateStatusBarItemsWithRelatedSystemApertureElements];
-[SBStatusBarStateAggregator dealloc];
-[SBStatusBarStateAggregator stewieDomain];
-[SBStatusBarStateAggregator _shouldShowPersonName];
-[SBStatusBarStateAggregator _updateLockItem];
-[SBStatusBarStateAggregator _updateSignalStrengthItem:withData:SIMInfo:barsGetter:barsSetter:];
-[SBStatusBarStateAggregator removePostingObserver:];
-[SBStatusBarStateAggregator _updateActiveAudioRecordingBackgroundActivityAssertionsForActiveSensorActivityAttributions:];
-[SBStatusBarStateAggregator cache:didUpdateActiveAudioRoute:];
-[SBStatusBarStateAggregator callingDomain];
-[SBStatusBarStateAggregator _setItem:enabled:inList:itemPostState:];
-[SBStatusBarStateAggregator setStewieDomain:];
-[SBStatusBarStateAggregator _removeTetheringBackgroundActivityAssertion];
-[SBStatusBarStateAggregator _updateAirplaneMode];
-[SBStatusBarStateAggregator _backgroundActivityDescriptorsForCallDescriptors:];
-[SBStatusBarStateAggregator _updateDisplayWarningItem];
-[SBStatusBarStateAggregator wifiDomain];
-[SBStatusBarStateAggregator _updateOverrideDate];
-[SBStatusBarStateAggregator _statusBarBatteryStateForSystemStatusChargingState:];
-[SBStatusBarStateAggregator _invalidateSystemApertureChargingElementAssertionForReason:];
-[SBStatusBarStateAggregator setVoiceControlDomain:];
-[SBStatusBarStateAggregator statusItemsDataProvider];
-[SBStatusBarStateAggregator _updateRingerItem];
-[SBStatusBarStateAggregator _updateStateAtomicallyWithoutAnimationUsingBlock:];
-[SBStatusBarStateAggregator setCallingDomain:];
-[SBStatusBarStateAggregator setFocusDomain:];
-[SBStatusBarStateAggregator statusItemsDomain];
-[SBStatusBarStateAggregator _updateSecondaryDataNetworkItem];
-[SBStatusBarStateAggregator _locationAttributionsForSensorActivityAttributions:includeRecent:];
-[SBStatusBarStateAggregator initWithSystemStatusServerHandle:sensorActivityDataProvider:telephonyStateProvider:telephonyManager:userSessionController:applicationController:bluetoothController:airplaneModeController:thermalController:wifiManager:];
-[SBStatusBarStateAggregator updateStatusBarItem:];
-[SBStatusBarStateAggregator _temporarilyOverrideLocationItemForProminentIndication];
-[SBStatusBarStateAggregator _updateLocationItemForLocationAttributions:];
-[SBStatusBarStateAggregator batteryDataProvider];
-[SBStatusBarStateAggregator _batteryDomainData];
-[SBStatusBarStateAggregator setWifiDomain:];
-[SBStatusBarStateAggregator _requestActions:];
-[SBStatusBarStateAggregator _updateBluetoothHeadphonesItem];
-[SBStatusBarStateAggregator _updateSecondarySignalStrengthItem];
-[SBStatusBarStateAggregator playgroundsDomain];
-[SBStatusBarStateAggregator setAlarmEnabled:];
-[SBStatusBarStateAggregator _tickRefCount:up:withTransitionBlock:];
-[SBStatusBarStateAggregator _updateSecondaryCallForwardingItem];
-[SBStatusBarStateAggregator initWithSystemStatusServerHandle:sensorActivityDataProvider:telephonyStateProvider:telephonyManager:userSessionController:applicationController:bluetoothController:airplaneModeController:thermalController:wifiManager:registerForNotifications:];
-[SBStatusBarStateAggregator setSystemApertureChargingElementAssertion:];
-[SBStatusBarStateAggregator centralManager:didUpdatePeripheralConnectionState:];
-[SBStatusBarStateAggregator _setItem:enabled:];
-[SBStatusBarStateAggregator _updateCallToActionItem];
-[SBStatusBarStateAggregator _notifyItemChanged:];
-[SBStatusBarStateAggregator _noteAirplaneModeChanged];
-[SBStatusBarStateAggregator _updateTTYItem];
-[SBStatusBarStateAggregator voiceControlDomain];
-[SBStatusBarStateAggregator _updateLocationItem];
-[SBStatusBarStateAggregator _updateSecondaryServiceItem];
-[SBStatusBarStateAggregator _updateServiceItem:withData:SIMInfo:otherSIMInfo:serviceStringGetter:serviceStringSetter:serviceCrossfadeStringGetter:serviceCrossfadeStringSetter:serviceContentTypeGetter:serviceContentTypeSetter:serviceBadgeStringGetter:serviceBadgeStringSetter:serviceStringSuffixGetter:serviceStringSuffixSetter:numberSharingStateGetter:numberSharingStateSetter:];
-[SBStatusBarStateAggregator setUserNameOverride:];
-[SBStatusBarStateAggregator _updateAirplayItem];
-[SBStatusBarStateAggregator beginCoalescentBlock];
-[SBStatusBarStateAggregator setShowsActivityIndicatorEverywhere:];
-[SBStatusBarStateAggregator setTelephonyDomain:];
-[SBStatusBarStateAggregator _removeSatelliteSOSBackgroundActivityAssertion];
-[SBStatusBarStateAggregator setStatusItemsDomain:];
-[SBStatusBarStateAggregator _updateDataNetworkItemsForRSSIChange];
-[SBStatusBarStateAggregator wifiDataProvider];
-[SBStatusBarStateAggregator _updateStudentItem];
-[SBStatusBarStateAggregator _updateLiquidDetectionItem];
-[SBStatusBarStateAggregator _updateStatusBarItemsForSystemStatusDomain:andData:];
-[SBStatusBarStateAggregator batteryDomain];
-[SBStatusBarStateAggregator telephonyDomain];
-[SBStatusBarStateAggregator _isInAirplaneMode];
-[SBStatusBarStateAggregator _updateCallForwardingItem:withInfo:];
-[SBStatusBarStateAggregator windowSceneDidConnect:];
-[SBStatusBarStateAggregator _updateTetheringState];
-[SBStatusBarStateAggregator _updateSensorActivityItem];
-[SBStatusBarStateAggregator setShowsSyncActivityIndicator:];
-[SBStatusBarStateAggregator systemApertureChargingElementAssertion];
-[SBStatusBarStateAggregator _updateBatteryItems];
-[SBStatusBarStateAggregator _updateBluetoothBatteryItem];
-[SBStatusBarStateAggregator _updateActivityItem];
-[SBStatusBarStateAggregator _shouldShowEmergencyOnlyStatusForInfo:];
-[SBStatusBarStateAggregator _updateThermalColorItem];
-[SBStatusBarStateAggregator setBatteryDomain:];
-[SBStatusBarStateAggregator setShowsOverridesForRecording:];
-[SBStatusBarStateAggregator _handleShowRSSIDefaultChange];
-[SBStatusBarStateAggregator _resetTimeItemFormatter];
-[SBStatusBarStateAggregator _updateQuietModeItem];
-[SBStatusBarStateAggregator _updateServiceItem];
-[SBStatusBarStateAggregator setSystemApertureVisibleElementIdentifiers:];
-[SBStatusBarStateAggregator setPlaygroundsDomain:];
-[SBStatusBarStateAggregator _updateAlarmItem];
-[SBStatusBarStateAggregator _activeAudioRecordingAttributionsForSensorActivityAttributions:];
-[SBStatusBarStateAggregator _updateTimeItems];
-[SBStatusBarStateAggregator sendStatusBarActions:];
-[SBStatusBarStateAggregator addPostingObserver:];
-[SBStatusBarStateAggregator batteryChargingState];
-[SBStatusBarStateAggregator endCoalescentBlock];
-[SBStatusBarStateAggregator _updateVoiceControlItem];
-[SBStatusBarStateAggregator _systemApertureElementIdentifiersForStatusBarItem:];
```
