# `NIBluetoothHostTimeSyncResponse`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
C _uwbDeviceTimeUncertainty;
C _uwbClockSkewMeasurementAvailable;
C _success;
S _deviceMaxPpm;
S _retryDelay;
Q _deviceEventCount;
Q _uwbDeviceTimeUs;
```

## Properties

```
@property (TQ,R,N,V_deviceEventCount) deviceEventCount;
@property (TQ,R,N,V_uwbDeviceTimeUs) uwbDeviceTimeUs;
@property (TC,R,N,V_uwbDeviceTimeUncertainty) uwbDeviceTimeUncertainty;
@property (TC,R,N,V_uwbClockSkewMeasurementAvailable) uwbClockSkewMeasurementAvailable;
@property (TS,R,N,V_deviceMaxPpm) deviceMaxPpm;
@property (TC,R,N,V_success) success;
@property (TS,R,N,V_retryDelay) retryDelay;
```

## Class methods

```
+[NIBluetoothHostTimeSyncResponse supportsSecureCoding];
```

## Instance methods

```
-[NIBluetoothHostTimeSyncResponse success];
-[NIBluetoothHostTimeSyncResponse encodeWithCoder:];
-[NIBluetoothHostTimeSyncResponse description];
-[NIBluetoothHostTimeSyncResponse initWithCoder:];
-[NIBluetoothHostTimeSyncResponse copyWithZone:];
-[NIBluetoothHostTimeSyncResponse retryDelay];
-[NIBluetoothHostTimeSyncResponse uwbDeviceTimeUs];
-[NIBluetoothHostTimeSyncResponse deviceEventCount];
-[NIBluetoothHostTimeSyncResponse deviceMaxPpm];
-[NIBluetoothHostTimeSyncResponse initWithDeviceEventCount:uwbDeviceTimeUs:uwbDeviceTimeUncertainty:uwbClockSkewMeasurementAvailable:deviceMaxPpm:success:retryDelay:];
-[NIBluetoothHostTimeSyncResponse uwbClockSkewMeasurementAvailable];
-[NIBluetoothHostTimeSyncResponse uwbDeviceTimeUncertainty];
```
