# `WiFiAwareDatapathPerformanceReport`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
@"NSData" _localTimestamp;
@"NSNumber" _throughputCeilingMbps;
@"NSNumber" _throughputCapacityMbps;
@"NSDictionary" _txLatency;
@"NSNumber" _signalStrength;
d _durationActive;
```

## Properties

```
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSData",R,N,V_localTimestamp) localTimestamp;
@property (T@"NSNumber",R,N,V_throughputCeilingMbps) throughputCeilingMbps;
@property (T@"NSNumber",R,N,V_throughputCapacityMbps) throughputCapacityMbps;
@property (T@"NSDictionary",R,N,V_txLatency) txLatency;
@property (T@"NSNumber",R,N,V_signalStrength) signalStrength;
@property (Td,R,N,V_durationActive) durationActive;
```

## Class methods

```
+[WiFiAwareDatapathPerformanceReport supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDatapathPerformanceReport signalStrength];
-[WiFiAwareDatapathPerformanceReport timestamp];
-[WiFiAwareDatapathPerformanceReport localTimestamp];
-[WiFiAwareDatapathPerformanceReport encodeWithCoder:];
-[WiFiAwareDatapathPerformanceReport description];
-[WiFiAwareDatapathPerformanceReport initWithCoder:];
-[WiFiAwareDatapathPerformanceReport copyWithZone:];
-[WiFiAwareDatapathPerformanceReport durationActive];
-[WiFiAwareDatapathPerformanceReport throughputCapacityMbps];
-[WiFiAwareDatapathPerformanceReport throughputCeilingMbps];
-[WiFiAwareDatapathPerformanceReport txLatency];
-[WiFiAwareDatapathPerformanceReport initWithTimestamp:localTimestamp:throughputCeilingMbps:throughputCapacityMbps:txLatency:signalStrength:durationActive:];
```
