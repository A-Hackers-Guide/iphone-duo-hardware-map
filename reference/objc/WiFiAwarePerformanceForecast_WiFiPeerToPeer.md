# `WiFiAwarePerformanceForecast`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
@"NSData" _localTimestamp;
@"NSNumber" _signalStrength;
@"NSNumber" _localThroughputCeilingMbps;
@"NSNumber" _localThroughputCapacityMbps;
@"NSNumber" _localThroughputCapacityRatio;
@"NSNumber" _localInfrastructureThroughputCapacityRatio;
@"NSMeasurement" _unavailabilityLatencyCeilingMs;
```

## Properties

```
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSData",R,N,V_localTimestamp) localTimestamp;
@property (T@"NSNumber",R,N,V_signalStrength) signalStrength;
@property (T@"NSNumber",R,N,V_localThroughputCeilingMbps) localThroughputCeilingMbps;
@property (T@"NSNumber",R,N,V_localThroughputCapacityMbps) localThroughputCapacityMbps;
@property (T@"NSNumber",R,N,V_localThroughputCapacityRatio) localThroughputCapacityRatio;
@property (T@"NSNumber",R,N,V_localInfrastructureThroughputCapacityRatio) localInfrastructureThroughputCapacityRatio;
@property (T@"NSMeasurement",R,N,V_unavailabilityLatencyCeilingMs) unavailabilityLatencyCeilingMs;
```

## Class methods

```
+[WiFiAwarePerformanceForecast supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePerformanceForecast signalStrength];
-[WiFiAwarePerformanceForecast timestamp];
-[WiFiAwarePerformanceForecast localTimestamp];
-[WiFiAwarePerformanceForecast encodeWithCoder:];
-[WiFiAwarePerformanceForecast hash];
-[WiFiAwarePerformanceForecast description];
-[WiFiAwarePerformanceForecast initWithCoder:];
-[WiFiAwarePerformanceForecast copyWithZone:];
-[WiFiAwarePerformanceForecast isEqual:];
-[WiFiAwarePerformanceForecast localInfrastructureThroughputCapacityRatio];
-[WiFiAwarePerformanceForecast localThroughputCapacityMbps];
-[WiFiAwarePerformanceForecast unavailabilityLatencyCeilingMs];
-[WiFiAwarePerformanceForecast initWithTimestamp:localTimestamp:signalStrength:localThroughputCeilingMbps:localThroughputCapacityMbps:localThroughputCapacityRatio:localInfrastructureThroughputCapacityRatio:unavailabilityLatencyCeilingMs:];
-[WiFiAwarePerformanceForecast localThroughputCapacityRatio];
-[WiFiAwarePerformanceForecast localThroughputCeilingMbps];
```
