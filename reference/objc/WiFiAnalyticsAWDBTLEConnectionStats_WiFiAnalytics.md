# `WiFiAnalyticsAWDBTLEConnectionStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 11 instance variables, 20 properties, 49 instance methods, 0 class methods

## Instance variables

```
I _complete;
I _dc0;
I _dc1;
I _dc2;
I _dc3;
I _dc4;
I _dc5;
I _peakOutage;
I _start;
I _totalDuration;
{?="complete"b1"dc0"b1"dc1"b1"dc2"b1"dc3"b1"dc4"b1"dc5"b1"peakOutage"b1"start"b1"totalDuration"b1} _has;
```

## Properties

```
@property (TB,N) hasStart;
@property (TI,N,V_start) start;
@property (TB,N) hasComplete;
@property (TI,N,V_complete) complete;
@property (TB,N) hasPeakOutage;
@property (TI,N,V_peakOutage) peakOutage;
@property (TB,N) hasTotalDuration;
@property (TI,N,V_totalDuration) totalDuration;
@property (TB,N) hasDc0;
@property (TI,N,V_dc0) dc0;
@property (TB,N) hasDc1;
@property (TI,N,V_dc1) dc1;
@property (TB,N) hasDc2;
@property (TI,N,V_dc2) dc2;
@property (TB,N) hasDc3;
@property (TI,N,V_dc3) dc3;
@property (TB,N) hasDc4;
@property (TI,N,V_dc4) dc4;
@property (TB,N) hasDc5;
@property (TI,N,V_dc5) dc5;
```

## Instance methods

```
-[WiFiAnalyticsAWDBTLEConnectionStats writeTo:];
-[WiFiAnalyticsAWDBTLEConnectionStats mergeFrom:];
-[WiFiAnalyticsAWDBTLEConnectionStats start];
-[WiFiAnalyticsAWDBTLEConnectionStats complete];
-[WiFiAnalyticsAWDBTLEConnectionStats setComplete:];
-[WiFiAnalyticsAWDBTLEConnectionStats totalDuration];
-[WiFiAnalyticsAWDBTLEConnectionStats setStart:];
-[WiFiAnalyticsAWDBTLEConnectionStats hash];
-[WiFiAnalyticsAWDBTLEConnectionStats copyTo:];
-[WiFiAnalyticsAWDBTLEConnectionStats description];
-[WiFiAnalyticsAWDBTLEConnectionStats readFrom:];
-[WiFiAnalyticsAWDBTLEConnectionStats copyWithZone:];
-[WiFiAnalyticsAWDBTLEConnectionStats isEqual:];
-[WiFiAnalyticsAWDBTLEConnectionStats dictionaryRepresentation];
-[WiFiAnalyticsAWDBTLEConnectionStats hasStart];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasStart:];
-[WiFiAnalyticsAWDBTLEConnectionStats hasTotalDuration];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasTotalDuration:];
-[WiFiAnalyticsAWDBTLEConnectionStats setTotalDuration:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasComplete:];
-[WiFiAnalyticsAWDBTLEConnectionStats hasComplete];
-[WiFiAnalyticsAWDBTLEConnectionStats dc1];
-[WiFiAnalyticsAWDBTLEConnectionStats dc3];
-[WiFiAnalyticsAWDBTLEConnectionStats dc5];
-[WiFiAnalyticsAWDBTLEConnectionStats setDc0:];
-[WiFiAnalyticsAWDBTLEConnectionStats setDc2:];
-[WiFiAnalyticsAWDBTLEConnectionStats setDc4:];
-[WiFiAnalyticsAWDBTLEConnectionStats dc0];
-[WiFiAnalyticsAWDBTLEConnectionStats dc2];
-[WiFiAnalyticsAWDBTLEConnectionStats dc4];
-[WiFiAnalyticsAWDBTLEConnectionStats setDc1:];
-[WiFiAnalyticsAWDBTLEConnectionStats setDc3:];
-[WiFiAnalyticsAWDBTLEConnectionStats setDc5:];
-[WiFiAnalyticsAWDBTLEConnectionStats hasDc0];
-[WiFiAnalyticsAWDBTLEConnectionStats hasDc1];
-[WiFiAnalyticsAWDBTLEConnectionStats hasDc2];
-[WiFiAnalyticsAWDBTLEConnectionStats hasDc3];
-[WiFiAnalyticsAWDBTLEConnectionStats hasDc4];
-[WiFiAnalyticsAWDBTLEConnectionStats hasDc5];
-[WiFiAnalyticsAWDBTLEConnectionStats hasPeakOutage];
-[WiFiAnalyticsAWDBTLEConnectionStats peakOutage];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasDc0:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasDc1:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasDc2:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasDc3:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasDc4:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasDc5:];
-[WiFiAnalyticsAWDBTLEConnectionStats setHasPeakOutage:];
-[WiFiAnalyticsAWDBTLEConnectionStats setPeakOutage:];
```
