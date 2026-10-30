# `SADeviceUpdateEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 4 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _lastEvent;
@"SADevice" _device;
Q _eventType;
@"NSDate" _date;
```

## Properties

```
@property (T@"SADevice",R,C,N,V_device) device;
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
+[SADeviceUpdateEvent supportsSecureCoding];
```

## Instance methods

```
-[SADeviceUpdateEvent eventType];
-[SADeviceUpdateEvent device];
-[SADeviceUpdateEvent date];
-[SADeviceUpdateEvent getDate];
-[SADeviceUpdateEvent descriptionDictionary];
-[SADeviceUpdateEvent encodeWithCoder:];
-[SADeviceUpdateEvent lastEvent];
-[SADeviceUpdateEvent description];
-[SADeviceUpdateEvent initWithCoder:];
-[SADeviceUpdateEvent copyWithZone:];
-[SADeviceUpdateEvent isEqual:];
-[SADeviceUpdateEvent encodeWithOSLogCoder:options:maxLength:];
-[SADeviceUpdateEvent initWithDevice:eventType:lastEvent:date:];
```
