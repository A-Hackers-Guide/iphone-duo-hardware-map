# `IOPortLDCMManagerV4`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 25 properties, 84 instance methods, 0 class methods

## Instance variables

```
C _previousLDCMPortStatus;
B _isReceptacleEmpty;
B _mitigationsEnabled;
B _overrideEnabled;
B _uiActive;
B _waveformExtractionDisabled;
B _behaviorOverrideDisableMitigations;
B _behaviorOverrideDisableUI;
B _behaviorOverrideDisableIntrusiveUI;
B _behaviorOverrideForcePortWet;
C _ovpErrorCount;
B _ovpInterruptsDisabled;
I _notification;
I _ldcmFeatureConnect;
I _measurementQueueNotificationPort;
i _buildType;
i _deviceClass;
i _currentMitigationsStatus;
@"NSObject<OS_dispatch_queue>" _ldcmV4DispatchQueue;
@"LDCMNotificationUIManagerV4" _notificationUIManager;
Q _measurementQueueMappedAddress;
Q _measurementQueueMappedSize;
@"NSObject<OS_dispatch_source>" _measurementQueueDispatchSource;
@"NSString" _measurementInfoOutputString;
@"NSDate" _portAttachedTime;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_ldcmV4DispatchQueue) ldcmV4DispatchQueue;
@property (T@"LDCMNotificationUIManagerV4",&,N,V_notificationUIManager) notificationUIManager;
@property (TI,N,V_notification) notification;
@property (TI,N,V_ldcmFeatureConnect) ldcmFeatureConnect;
@property (TQ,N,V_measurementQueueMappedAddress) measurementQueueMappedAddress;
@property (TQ,N,V_measurementQueueMappedSize) measurementQueueMappedSize;
@property (TI,N,V_measurementQueueNotificationPort) measurementQueueNotificationPort;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_measurementQueueDispatchSource) measurementQueueDispatchSource;
@property (Ti,N,V_buildType) buildType;
@property (Ti,N,V_deviceClass) deviceClass;
@property (TC,N,V_previousLDCMPortStatus) previousLDCMPortStatus;
@property (TB,N,V_isReceptacleEmpty) isReceptacleEmpty;
@property (TB,N,V_mitigationsEnabled) mitigationsEnabled;
@property (TB,N,V_overrideEnabled) overrideEnabled;
@property (T@"NSString",N,V_measurementInfoOutputString) measurementInfoOutputString;
@property (TB,N,V_uiActive) uiActive;
@property (TB,N,V_waveformExtractionDisabled) waveformExtractionDisabled;
@property (TB,N,V_behaviorOverrideDisableMitigations) behaviorOverrideDisableMitigations;
@property (TB,N,V_behaviorOverrideDisableUI) behaviorOverrideDisableUI;
@property (TB,N,V_behaviorOverrideDisableIntrusiveUI) behaviorOverrideDisableIntrusiveUI;
@property (TB,N,V_behaviorOverrideForcePortWet) behaviorOverrideForcePortWet;
@property (Ti,N,V_currentMitigationsStatus) currentMitigationsStatus;
@property (T@"NSDate",N,V_portAttachedTime) portAttachedTime;
@property (TC,N,V_ovpErrorCount) ovpErrorCount;
@property (TB,N,V_ovpInterruptsDisabled) ovpInterruptsDisabled;
```

## Instance methods

```
-[IOPortLDCMManagerV4 setDeviceClass:];
-[IOPortLDCMManagerV4 notification];
-[IOPortLDCMManagerV4 deviceClass];
-[IOPortLDCMManagerV4 setNotification:];
-[IOPortLDCMManagerV4 dealloc];
-[IOPortLDCMManagerV4 setUserOverride:];
-[IOPortLDCMManagerV4 setOverrideEnabled:];
-[IOPortLDCMManagerV4 overrideEnabled];
-[IOPortLDCMManagerV4 setOverride:];
-[IOPortLDCMManagerV4 buildType];
-[IOPortLDCMManagerV4 setBuildType:];
-[IOPortLDCMManagerV4 hideUI];
-[IOPortLDCMManagerV4 showUI];
-[IOPortLDCMManagerV4 setUiActive:];
-[IOPortLDCMManagerV4 setLiquidDetected:];
-[IOPortLDCMManagerV4 mitigationsEnabled];
-[IOPortLDCMManagerV4 setMitigationsEnabled:];
-[IOPortLDCMManagerV4 setMitigations:];
-[IOPortLDCMManagerV4 setMeasurementInfoOutputString:];
-[IOPortLDCMManagerV4 behaviorOverrideDisableIntrusiveUI];
-[IOPortLDCMManagerV4 behaviorOverrideDisableMitigations];
-[IOPortLDCMManagerV4 behaviorOverrideDisableUI];
-[IOPortLDCMManagerV4 behaviorOverrideForcePortWet];
-[IOPortLDCMManagerV4 buildMeasurementHeaderString];
-[IOPortLDCMManagerV4 buildMeasurementOutputString:withMeasurementReason:withMeasurementEvent:];
-[IOPortLDCMManagerV4 checkIsReceptacleEmpty];
-[IOPortLDCMManagerV4 cleanupMeasurementQueue];
-[IOPortLDCMManagerV4 currentMitigationsStatus];
-[IOPortLDCMManagerV4 disableOVPInterrupts];
-[IOPortLDCMManagerV4 extractData::];
-[IOPortLDCMManagerV4 generateLDCMCSVData];
-[IOPortLDCMManagerV4 getCachedWaveform::::];
-[IOPortLDCMManagerV4 getData::];
-[IOPortLDCMManagerV4 getMeasurementOutputString];
-[IOPortLDCMManagerV4 getWaveform::];
-[IOPortLDCMManagerV4 handleAttachEvent];
-[IOPortLDCMManagerV4 handleDetachEvent];
-[IOPortLDCMManagerV4 handleLDCMMitigationsStatusChange:];
-[IOPortLDCMManagerV4 initWithParams:withNotificationPort:withServerRunloop:];
-[IOPortLDCMManagerV4 isReceptacleEmpty];
-[IOPortLDCMManagerV4 ldcmFeatureConnect];
-[IOPortLDCMManagerV4 ldcmV4DispatchQueue];
-[IOPortLDCMManagerV4 logInfo:withMitigationsStatus:];
-[IOPortLDCMManagerV4 measureOccupiedWetPortDuration];
-[IOPortLDCMManagerV4 measurementInfoOutputString];
-[IOPortLDCMManagerV4 measurementQueueDispatchSource];
-[IOPortLDCMManagerV4 measurementQueueMappedAddress];
-[IOPortLDCMManagerV4 measurementQueueMappedSize];
-[IOPortLDCMManagerV4 measurementQueueNotificationPort];
-[IOPortLDCMManagerV4 notificationUIManager];
-[IOPortLDCMManagerV4 ovpErrorCount];
-[IOPortLDCMManagerV4 ovpInterruptsDisabled];
-[IOPortLDCMManagerV4 performLDCMMeasurement:];
-[IOPortLDCMManagerV4 portAttachedTime];
-[IOPortLDCMManagerV4 previousLDCMPortStatus];
-[IOPortLDCMManagerV4 processBehaviorDictionary:];
-[IOPortLDCMManagerV4 processQueuedMeasurements];
-[IOPortLDCMManagerV4 publishAnalytics:withMeasurementReason:withWaveformRawData:withWaveformDataLen:withReceptacleEmpty:];
-[IOPortLDCMManagerV4 setBehaviorOverrideDisableIntrusiveUI:];
-[IOPortLDCMManagerV4 setBehaviorOverrideDisableMitigations:];
-[IOPortLDCMManagerV4 setBehaviorOverrideDisableUI:];
-[IOPortLDCMManagerV4 setBehaviorOverrideForcePortWet:];
-[IOPortLDCMManagerV4 setCurrentMitigationsStatus:];
-[IOPortLDCMManagerV4 setForcePortWet:];
-[IOPortLDCMManagerV4 setIsReceptacleEmpty:];
-[IOPortLDCMManagerV4 setLDCMMeasurementStatus:];
-[IOPortLDCMManagerV4 setLDCMState:];
-[IOPortLDCMManagerV4 setLdcmFeatureConnect:];
-[IOPortLDCMManagerV4 setLdcmV4DispatchQueue:];
-[IOPortLDCMManagerV4 setMeasurementQueueDispatchSource:];
-[IOPortLDCMManagerV4 setMeasurementQueueMappedAddress:];
-[IOPortLDCMManagerV4 setMeasurementQueueMappedSize:];
-[IOPortLDCMManagerV4 setMeasurementQueueNotificationPort:];
-[IOPortLDCMManagerV4 setNotificationUIManager:];
-[IOPortLDCMManagerV4 setOvpErrorCount:];
-[IOPortLDCMManagerV4 setOvpInterruptsDisabled:];
-[IOPortLDCMManagerV4 setPortAttachedTime:];
-[IOPortLDCMManagerV4 setPreviousLDCMPortStatus:];
-[IOPortLDCMManagerV4 setWaveformExtractionDisabled:];
-[IOPortLDCMManagerV4 setWaveformExtractionEnabled:];
-[IOPortLDCMManagerV4 setupMeasurementQueue];
-[IOPortLDCMManagerV4 storeWaveform:withWaveformDataLen:];
-[IOPortLDCMManagerV4 uiActive];
-[IOPortLDCMManagerV4 waveformExtractionDisabled];
```
