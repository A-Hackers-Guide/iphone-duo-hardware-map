# `_BCPowerSourceController`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter`](../userland/System__Library__PrivateFrameworks__BatteryCenter.framework__BatteryCenter.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BCBatteryDeviceObservable`
- 10 instance variables, 5 properties, 32 instance methods, 1 class methods

## Instance variables

```
i _powerSourceBatteryChangeNotifyToken;
i _powerSourceTimeRemainingNotifyToken;
i _accPowerSourceNotifyToken;
i _accPowerSourceTimeRemainingNotifyToken;
i _accAttachNotifyToken;
i _lowPowerModeNotifyToken;
i _chargingIconographyStateNotifyToken;
B _lowPowerModeActive;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMapTable" _observersToQueues;
```

## Properties

```
@property (T@"NSArray",R,C,N) connectedDevices;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_BCPowerSourceController initialize];
```

## Instance methods

```
-[_BCPowerSourceController _registerForNotification:token:queue:handler:];
-[_BCPowerSourceController _shouldCoalesceDevices:minimumPercentCharge:];
-[_BCPowerSourceController removeBatteryDeviceObserver:];
-[_BCPowerSourceController _shouldConsiderDeviceWithPowerSourceDescription:];
-[_BCPowerSourceController connectedDevices];
-[_BCPowerSourceController _notifyObserver:block:queue:];
-[_BCPowerSourceController _nameForVendor:accessoryCategory:name:partName:isInternal:];
-[_BCPowerSourceController init];
-[_BCPowerSourceController _updateLowPowerModeState];
-[_BCPowerSourceController _deviceByCoalescingDevice:];
-[_BCPowerSourceController _beginPowerSourceObservingIfNecessary];
-[_BCPowerSourceController _transportTypeFromPowerSourceTransportTypeString:];
-[_BCPowerSourceController _identifierFromPowerSourceDescription:];
-[_BCPowerSourceController dealloc];
-[_BCPowerSourceController _isChargingPaused];
-[_BCPowerSourceController _endPowerSourceObserving];
-[_BCPowerSourceController _accessoryCategoryFromPowerSourceAccessoryCategory:partType:transportType:vendor:productIdentifier:];
-[_BCPowerSourceController addBatteryDeviceObserver:queue:];
-[_BCPowerSourceController _displayChargePercentForCurrentCapacity:andMaxCapacity:updateZeroValue:];
-[_BCPowerSourceController _notifyObserversWithBlock:];
-[_BCPowerSourceController _isLowPowerModeActive];
-[_BCPowerSourceController _isDevicePartOfPair:];
-[_BCPowerSourceController _nameForCurrentDevice];
-[_BCPowerSourceController _partFromPowerSourcePartIdentifier:];
-[_BCPowerSourceController _handleLowPowerModeChanged:];
-[_BCPowerSourceController _vendorFromPowerSourceDescriptionVendorIdentifier:transportType:];
-[_BCPowerSourceController _powerSourceStateFromPowerSourceStateString:];
-[_BCPowerSourceController _queryConnectedDevices];
-[_BCPowerSourceController _lowBatteryLevelForCurrentDevice];
-[_BCPowerSourceController _registerForPowerSourceChangeNotification:token:queue:];
-[_BCPowerSourceController _orderedDevicesFromPowerSourcesBlob:powerSourcesList:];
-[_BCPowerSourceController _lowBatteryLevelForVendor:accessoryCategory:transportType:];
```
