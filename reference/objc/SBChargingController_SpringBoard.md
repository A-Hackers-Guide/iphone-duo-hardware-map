# `SBChargingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BCBatteryDeviceObserving`, `SBAccessoryConnectionInfoProviderObserver`, `SBFMotionAlarmDelegate`, `BSDescriptionProviding`, `CSMagSafeAccessoryStatusProviding`, `CSPowerStatusProviding`
- 42 instance variables, 13 properties, 76 instance methods, 0 class methods

## Instance variables

```
@"SBRestartManager" _restartManager;
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"BCBatteryDeviceController" _batteryDeviceController;
@"BIBatteryAnalysisClient" _batteryAnalysisClient;
@"NSObject<OS_dispatch_queue>" _batteryEstimateFetchQueue;
b1 _isBatteryCharging;
b1 _isFullyCharged;
b1 _isBatteryCritical;
b1 _isOnAC;
b1 _isConnectedToExternalChargingAccessory;
b1 _isConnectedToPoweredExternalChargingAccessory;
b1 _isConnectedToUnsupportedChargingAccessory;
b1 _isConnectedToChargeIncapablePowerSource;
b1 _isConnectedToQiPower;
b1 _wasConnectedToWirelessChargingAccessory;
b1 _isConnectedToWirelessInternalCharger;
b1 _isConnectedToWirelessInternalChargingAccessory;
b1 _isConnectedToWirelessInternalAccessory;
b1 _hasSeenEdgeCompensationCaseAttachedAlertSinceBoot;
f _batteryCapacity;
B _supportsDetailedBatteryCapacity;
i _powerStateUpdateToken;
@"NSMutableDictionary" _powerSourceHasChimed;
i _batteryLoggingStartCapacity;
@"NSString" _connectedWirelessChargerId;
@"SBDismissOnlyAlertItem" _unsupportedChargerAlert;
i _firmwareUpdateStateToken;
@"SBAccessoryConnectionInfoProvider" _accessoryConnectionInfoProvider;
@"BSAbsoluteMachTimer" _accessoryAttachmentAnimationBlockingTimer;
@"NSString" _attachedEdgeOccludingCaseUUID;
@"SBFMotionAlarmController" _motionAlarmController;
B _disableChimeForWirelessCharging;
B _disableScreenWakeForWirelessCharging;
@"SWWakingTimer" _debounceWirelessChargingTimer;
B _isAccessoryAnimationAllowed;
@"CSMagSafeAccessory" _lastAttachedAccessory;
@"CSMagSafeAccessory" _lastDetachedAccessory;
@"NSMutableDictionary" _accessoriesAttachedByUUID;
@"NSMutableDictionary" _accessoriesSuppressedByUUID;
@"SBScreenLongevityController" _screenLongevityController;
B _chargingChimeEnabled;
```

## Properties

```
@property (TB,N,V_chargingChimeEnabled) chargingChimeEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CSMagSafeAccessory",R,N) lastAttachedAccessory;
@property (T@"CSMagSafeAccessory",R,N) lastDetachedAccessory;
@property (TB,R,N) isAccessoryAnimationAllowed;
@property (TB,R,N,GisOnAC) onAC;
@property (TB,R,N,GisConnectedToExternalChargingSource) connectedToExternalChargingSource;
@property (TB,R,N,GisConnectedToWirelessInternalCharger) connectedToWirelessInternalCharger;
@property (TB,R,N,GisConnectedToWirelessInternalChargingAccessory) connectedToWirelessInternalChargingAccessory;
@property (TB,R,N,GisConnectedToQiPower) connectedToQiPower;
```

## Instance methods

```
-[SBChargingController isConnectedToQiPower];
-[SBChargingController _removeSuppressedAccessory:];
-[SBChargingController updateBatteryState:];
-[SBChargingController isFullyCharged];
-[SBChargingController _disableWirelessChargingChimeAndScreenWakeForDuration:];
-[SBChargingController isHeadsetBatteryCharging];
-[SBChargingController playChargingChimeIfAppropriate];
-[SBChargingController ACPowerChanged];
-[SBChargingController accessoryConnectionInfoProvider:accessoryEndpointAttached:transportType:protocol:properties:forConnection:];
-[SBChargingController removeDetachedAccessory:];
-[SBChargingController setLastDetachedAccessory:];
-[SBChargingController isEdgeOccludingCaseAttached];
-[SBChargingController _playAccessoryChimeIfAppropriateForAccessory:attaching:withDelay:];
-[SBChargingController lastDetachedAccessory];
-[SBChargingController succinctDescriptionBuilder];
-[SBChargingController isConnectedToChargeIncapablePowerSource];
-[SBChargingController _powerSourceWantsToPlayChime];
-[SBChargingController localizedBatteryDetailTextForBatteryLevel:];
-[SBChargingController isConnectedToWirelessInternalChargingAccessory];
-[SBChargingController _shouldInitiateAnimationForAccessory:];
-[SBChargingController dealloc];
-[SBChargingController internalBatteryDevice];
-[SBChargingController accessoryConnectionInfoProvider:accessoryEndpointInfoPropertyChanged:properties:forConnection:];
-[SBChargingController _animationBlockingTimerFired];
-[SBChargingController supportsDetailedBatteryCapacity];
-[SBChargingController _accessoryEndpointAttached:properties:reportToLockScreen:];
-[SBChargingController _setAccessoryAttachmentAnimationBlockingTimerWithDuration:];
-[SBChargingController storeAttachedAccessory:];
-[SBChargingController connectedWirelessChargerIdentifier];
-[SBChargingController descriptionWithMultilinePrefix:];
-[SBChargingController _resetWirelessChargingState];
-[SBChargingController _setDebounceWirelessChargingTimerWithDuration:];
-[SBChargingController lastAttachedAccessory];
-[SBChargingController _enumeratePowerSourcesWithBlock:];
-[SBChargingController succinctDescription];
-[SBChargingController _accessoryEndpointAttached:];
-[SBChargingController _debounceWirelessChargingTimerFired];
-[SBChargingController _disableWirelessChargingChimeAndScreenWakeForDuration:withMotionAlarm:];
-[SBChargingController chargingChimeEnabled];
-[SBChargingController isConnectedToWirelessInternalCharger];
-[SBChargingController _accessoryEndpointDetached:];
-[SBChargingController _cancelDebounceWirelessChargingTimer];
-[SBChargingController initWithRestartManager:backlightCoordinator:lockScreenCoordinator:screenLongevityController:];
-[SBChargingController setLastAttachedAccessory:];
-[SBChargingController dismissAnyAttachedWindowedAccessory];
-[SBChargingController _blocksAnimationForAccessoryType:];
-[SBChargingController isBatteryCharging];
-[SBChargingController didDetectDeviceMotion];
-[SBChargingController setIsAccessoryAnimationAllowed:];
-[SBChargingController batteryCapacity];
-[SBChargingController isConnectedToWirelessInternalAccessory];
-[SBChargingController supportsDetailedBatteryMetrics];
-[SBChargingController isOnAC];
-[SBChargingController _treatsAccessoryAsSupported:];
-[SBChargingController fetchFormattedChargeTimeEstimateWithCompletion:];
-[SBChargingController suppressChimeForConnectedPowerSources];
-[SBChargingController connectedDevicesDidChange:];
-[SBChargingController description];
-[SBChargingController isAccessoryAnimationAllowed];
-[SBChargingController setChargingChimeEnabled:];
-[SBChargingController headsetBatteryCapacity];
-[SBChargingController possiblyWakeForPowerStatusChangeWithUnlockSource:];
-[SBChargingController accessoryConnectionInfoProvider:accessoryEndpointDetached:forConnection:];
-[SBChargingController isConnectedToUnsupportedChargingAccessory];
-[SBChargingController _isConnectedToWirelessCharging];
-[SBChargingController _dismissAccessory:playChime:];
-[SBChargingController isHeadsetDocked];
-[SBChargingController _updatesHomeScreenForAccessoryWithType:];
-[SBChargingController _isAppropriateToReactToAccessoryEvent];
-[SBChargingController _storeSuppressedAccessory:];
-[SBChargingController batteryCapacityAsPercentage];
-[SBChargingController _setAttachedEdgeOccludingCaseUUID:];
-[SBChargingController isConnectedToExternalChargingSource];
-[SBChargingController descriptionBuilderWithMultilinePrefix:];
-[SBChargingController setIsConnectedToUnsupportedChargingAccessory:];
-[SBChargingController _shouldShowAnimationForAccessory:];
```
