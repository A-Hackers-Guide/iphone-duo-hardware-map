# `CWFAutoJoinThrottle`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _trigger;
@"NSDictionary" _intervals;
@"NSDictionary" _intervalsBasedOnTriggerTimestamp;
```

## Properties

```
@property (Tq,N,V_trigger) trigger;
@property (T@"NSDictionary",&,N,V_intervals) intervals;
@property (T@"NSDictionary",&,N,V_intervalsBasedOnTriggerTimestamp) intervalsBasedOnTriggerTimestamp;
```

## Class methods

```
+[CWFAutoJoinThrottle autoJoinThrottleWithTrigger:intervals:];
```

## Instance methods

```
-[CWFAutoJoinThrottle trigger];
-[CWFAutoJoinThrottle description];
-[CWFAutoJoinThrottle copyWithZone:];
-[CWFAutoJoinThrottle setTrigger:];
-[CWFAutoJoinThrottle intervals];
-[CWFAutoJoinThrottle setIntervals:];
-[CWFAutoJoinThrottle intervalsBasedOnTriggerTimestamp];
-[CWFAutoJoinThrottle setIntervalsBasedOnTriggerTimestamp:];
```
