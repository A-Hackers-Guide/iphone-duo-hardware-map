# `SASafeLocationUpdateEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 4 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _lastEvent;
@"SASafeLocation" _safeLocation;
Q _eventType;
@"NSDate" _date;
```

## Properties

```
@property (T@"SASafeLocation",R,C,N,V_safeLocation) safeLocation;
@property (TQ,R,N,V_eventType) eventType;
@property (TB,R,N,V_lastEvent) lastEvent;
@property (T@"NSDate",R,C,N,V_date) date;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SASafeLocationUpdateEvent supportsSecureCoding];
```

## Instance methods

```
-[SASafeLocationUpdateEvent eventType];
-[SASafeLocationUpdateEvent date];
-[SASafeLocationUpdateEvent getDate];
-[SASafeLocationUpdateEvent descriptionDictionary];
-[SASafeLocationUpdateEvent encodeWithCoder:];
-[SASafeLocationUpdateEvent lastEvent];
-[SASafeLocationUpdateEvent description];
-[SASafeLocationUpdateEvent initWithCoder:];
-[SASafeLocationUpdateEvent copyWithZone:];
-[SASafeLocationUpdateEvent isEqual:];
-[SASafeLocationUpdateEvent encodeWithOSLogCoder:options:maxLength:];
-[SASafeLocationUpdateEvent initWithSafeLocation:eventType:lastEvent:date:];
-[SASafeLocationUpdateEvent safeLocation];
```
