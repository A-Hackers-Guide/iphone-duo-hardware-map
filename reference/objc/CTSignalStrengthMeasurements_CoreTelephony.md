# `CTSignalStrengthMeasurements`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 8 instance variables, 10 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _rssi;
@"NSNumber" _rscp;
@"NSNumber" _ecn0;
@"NSNumber" _rsrp;
@"NSNumber" _rsrq;
@"NSNumber" _snr;
@"NSNumber" _ecio;
@"NSNumber" _rxagc;
```

## Properties

```
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
@property (T@"NSNumber",&,N,V_rssi) rssi;
@property (T@"NSNumber",&,N,V_rscp) rscp;
@property (T@"NSNumber",&,N,V_ecn0) ecn0;
@property (T@"NSNumber",&,N,V_rsrp) rsrp;
@property (T@"NSNumber",&,N,V_rsrq) rsrq;
@property (T@"NSNumber",&,N,V_snr) snr;
@property (T@"NSNumber",&,N,V_ecio) ecio;
@property (T@"NSNumber",&,N,V_rxagc) rxagc;
```

## Class methods

```
+[CTSignalStrengthMeasurements supportsSecureCoding];
```

## Instance methods

```
-[CTSignalStrengthMeasurements rssi];
-[CTSignalStrengthMeasurements rscp];
-[CTSignalStrengthMeasurements setSnr:];
-[CTSignalStrengthMeasurements snr];
-[CTSignalStrengthMeasurements ct_shortDescription];
-[CTSignalStrengthMeasurements ct_shortName];
-[CTSignalStrengthMeasurements setRssi:];
-[CTSignalStrengthMeasurements encodeWithCoder:];
-[CTSignalStrengthMeasurements description];
-[CTSignalStrengthMeasurements initWithCoder:];
-[CTSignalStrengthMeasurements setRscp:];
-[CTSignalStrengthMeasurements copyWithZone:];
-[CTSignalStrengthMeasurements isEqual:];
-[CTSignalStrengthMeasurements setEcn0:];
-[CTSignalStrengthMeasurements ecn0];
-[CTSignalStrengthMeasurements rsrp];
-[CTSignalStrengthMeasurements rsrq];
-[CTSignalStrengthMeasurements ecio];
-[CTSignalStrengthMeasurements rxagc];
-[CTSignalStrengthMeasurements setEcio:];
-[CTSignalStrengthMeasurements setRsrp:];
-[CTSignalStrengthMeasurements setRsrq:];
-[CTSignalStrengthMeasurements setRxagc:];
```
