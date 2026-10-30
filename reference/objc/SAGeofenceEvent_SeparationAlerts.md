# `SAGeofenceEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
Q _eventType;
@"CLRegion" _region;
@"NSDate" _eventDate;
```

## Properties

```
@property (T@"CLRegion",R,C,N,V_region) region;
@property (TQ,R,N,V_eventType) eventType;
@property (T@"NSDate",R,C,N,V_eventDate) eventDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SAGeofenceEvent supportsSecureCoding];
```

## Instance methods

```
-[SAGeofenceEvent eventDate];
-[SAGeofenceEvent region];
-[SAGeofenceEvent eventType];
-[SAGeofenceEvent getDate];
-[SAGeofenceEvent descriptionDictionary];
-[SAGeofenceEvent encodeWithCoder:];
-[SAGeofenceEvent description];
-[SAGeofenceEvent initWithCoder:];
-[SAGeofenceEvent copyWithZone:];
-[SAGeofenceEvent isEqual:];
-[SAGeofenceEvent encodeWithOSLogCoder:options:maxLength:];
-[SAGeofenceEvent initWithRegion:eventType:eventDate:];
```
