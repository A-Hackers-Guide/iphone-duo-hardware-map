# `CWFRangingResult`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
i _status;
@"NSString" _MACAddress;
@"NSData" _identifier;
d _distance;
d _standardDeviation;
Q _numberOfValidMeasurements;
@"NSArray" _measurements;
```

## Properties

```
@property (T@"NSString",C,N,V_MACAddress) MACAddress;
@property (T@"NSData",C,N,V_identifier) identifier;
@property (Td,N,V_distance) distance;
@property (Td,N,V_standardDeviation) standardDeviation;
@property (Ti,N,V_status) status;
@property (TQ,N,V_numberOfValidMeasurements) numberOfValidMeasurements;
@property (T@"NSArray",C,N,V_measurements) measurements;
```

## Class methods

```
+[CWFRangingResult supportsSecureCoding];
```

## Instance methods

```
-[CWFRangingResult MACAddress];
-[CWFRangingResult distance];
-[CWFRangingResult setDistance:];
-[CWFRangingResult identifier];
-[CWFRangingResult status];
-[CWFRangingResult setIdentifier:];
-[CWFRangingResult encodeWithCoder:];
-[CWFRangingResult hash];
-[CWFRangingResult description];
-[CWFRangingResult standardDeviation];
-[CWFRangingResult initWithCoder:];
-[CWFRangingResult setStatus:];
-[CWFRangingResult copyWithZone:];
-[CWFRangingResult isEqual:];
-[CWFRangingResult setStandardDeviation:];
-[CWFRangingResult measurements];
-[CWFRangingResult isEqualToRangingResult:];
-[CWFRangingResult numberOfValidMeasurements];
-[CWFRangingResult setMACAddress:];
-[CWFRangingResult setMeasurements:];
-[CWFRangingResult setNumberOfValidMeasurements:];
```
