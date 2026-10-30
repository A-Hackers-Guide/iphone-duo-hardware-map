# `CMARange`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
S _cycleIndex;
d _timestamp;
d _range;
d _rangeError;
d _rssi;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (Td,N,V_range) range;
@property (Td,N,V_rangeError) rangeError;
@property (Td,N,V_rssi) rssi;
@property (TS,N,V_cycleIndex) cycleIndex;
```

## Instance methods

```
-[CMARange rssi];
-[CMARange setTimestamp:];
-[CMARange range];
-[CMARange timestamp];
-[CMARange setRssi:];
-[CMARange setRange:];
-[CMARange cycleIndex];
-[CMARange setCycleIndex:];
-[CMARange rangeError];
-[CMARange setRangeError:];
```
