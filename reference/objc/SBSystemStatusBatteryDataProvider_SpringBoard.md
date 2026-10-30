# `SBSystemStatusBatteryDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BCBatteryDeviceObserving`, `BSInvalidatable`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _shouldExposeNotChargingState;
@"STBatteryStatusDomainData" _lastPublishedData;
@"STBatteryStatusDomainPublisher" _batteryDataPublisher;
@"BCBatteryDeviceController" _batteryDeviceController;
```

## Properties

```
@property (T@"STBatteryStatusDomainPublisher",R,N,V_batteryDataPublisher) batteryDataPublisher;
@property (T@"BCBatteryDeviceController",R,N,V_batteryDeviceController) batteryDeviceController;
@property (TB,N,V_shouldExposeNotChargingState) shouldExposeNotChargingState;
@property (T@"STBatteryStatusDomainData",R,N,V_lastPublishedData) lastPublishedData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemStatusBatteryDataProvider _registerForNotifications];
-[SBSystemStatusBatteryDataProvider init];
-[SBSystemStatusBatteryDataProvider dealloc];
-[SBSystemStatusBatteryDataProvider invalidate];
-[SBSystemStatusBatteryDataProvider connectedDevicesDidChange:];
-[SBSystemStatusBatteryDataProvider _updateData];
-[SBSystemStatusBatteryDataProvider batteryDeviceController];
-[SBSystemStatusBatteryDataProvider _isInNotChargingState];
-[SBSystemStatusBatteryDataProvider _noteNotChargingStatusChanged];
-[SBSystemStatusBatteryDataProvider _updateShouldExposeNotChargingState];
-[SBSystemStatusBatteryDataProvider batteryDataPublisher];
-[SBSystemStatusBatteryDataProvider lastPublishedData];
-[SBSystemStatusBatteryDataProvider setShouldExposeNotChargingState:];
-[SBSystemStatusBatteryDataProvider shouldExposeNotChargingState];
```
