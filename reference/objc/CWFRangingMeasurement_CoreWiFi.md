# `CWFRangingMeasurement`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _roundTripTime;
q _RSSI;
Q _channel;
q _SNR;
Q _coreID;
```

## Properties

```
@property (Tq,N,V_roundTripTime) roundTripTime;
@property (Tq,N,V_RSSI) RSSI;
@property (TQ,N,V_channel) channel;
@property (Tq,N,V_SNR) SNR;
@property (TQ,N,V_coreID) coreID;
```

## Class methods

```
+[CWFRangingMeasurement supportsSecureCoding];
```

## Instance methods

```
-[CWFRangingMeasurement setSNR:];
-[CWFRangingMeasurement setChannel:];
-[CWFRangingMeasurement channel];
-[CWFRangingMeasurement setRSSI:];
-[CWFRangingMeasurement RSSI];
-[CWFRangingMeasurement encodeWithCoder:];
-[CWFRangingMeasurement hash];
-[CWFRangingMeasurement description];
-[CWFRangingMeasurement initWithCoder:];
-[CWFRangingMeasurement copyWithZone:];
-[CWFRangingMeasurement isEqual:];
-[CWFRangingMeasurement SNR];
-[CWFRangingMeasurement roundTripTime];
-[CWFRangingMeasurement setRoundTripTime:];
-[CWFRangingMeasurement coreID];
-[CWFRangingMeasurement isEqualToRangingMeasurement:];
-[CWFRangingMeasurement setCoreID:];
```
