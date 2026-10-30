# `CLMonitoringRecord`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"CLCondition" _condition;
@"CLMonitoringEvent" _lastEvent;
Q _options;
```

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (TQ,R,N,V_options) options;
@property (T@"CLCondition",R) constraint;
@property (T@"CLCondition",R,V_condition) condition;
@property (T@"CLMonitoringEvent",R,V_lastEvent) lastEvent;
```

## Class methods

```
+[CLMonitoringRecord supportsSecureCoding];
```

## Instance methods

```
-[CLMonitoringRecord constraint];
-[CLMonitoringRecord condition];
-[CLMonitoringRecord identifier];
-[CLMonitoringRecord dealloc];
-[CLMonitoringRecord encodeWithCoder:];
-[CLMonitoringRecord hash];
-[CLMonitoringRecord lastEvent];
-[CLMonitoringRecord description];
-[CLMonitoringRecord initWithCoder:];
-[CLMonitoringRecord options];
-[CLMonitoringRecord isEqual:];
-[CLMonitoringRecord initRecordWithMonitoringRecord:];
-[CLMonitoringRecord initRecordWithCondition:identifier:];
-[CLMonitoringRecord initRecordWithCondition:identifier:options:];
-[CLMonitoringRecord initRecordWithCondition:identifier:options:initialState:];
-[CLMonitoringRecord initRecordWithCondition:options:event:];
-[CLMonitoringRecord updateEvent:];
```
