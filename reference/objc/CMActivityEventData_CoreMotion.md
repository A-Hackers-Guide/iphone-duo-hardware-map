# `CMActivityEventData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `SRSampling`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 15 properties, 18 instance methods, 4 class methods

## Instance variables

```
@"NSDate" _startDate;
q _eventType;
q _action;
q _reason;
q _workoutType;
d _heartRateRecoveryStartTime;
d _heartRateRecoveryEndTime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (Tq,R,N,V_eventType) eventType;
@property (Tq,R,N,V_action) action;
@property (Tq,R,N,V_reason) reason;
@property (Tq,R,N,V_workoutType) workoutType;
@property (Td,N,V_heartRateRecoveryStartTime) heartRateRecoveryStartTime;
@property (Td,N,V_heartRateRecoveryEndTime) heartRateRecoveryEndTime;
```

## Class methods

```
+[CMActivityEventData supportsSecureCoding];
+[CMActivityEventData actionName:];
+[CMActivityEventData eventTypeName:];
+[CMActivityEventData reasonName:];
```

## Instance methods

```
-[CMActivityEventData startDate];
-[CMActivityEventData eventType];
-[CMActivityEventData dealloc];
-[CMActivityEventData action];
-[CMActivityEventData encodeWithCoder:];
-[CMActivityEventData workoutType];
-[CMActivityEventData description];
-[CMActivityEventData initWithCoder:];
-[CMActivityEventData reason];
-[CMActivityEventData copyWithZone:];
-[CMActivityEventData binarySampleRepresentation];
-[CMActivityEventData heartRateRecoveryEndTime];
-[CMActivityEventData heartRateRecoveryStartTime];
-[CMActivityEventData initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMActivityEventData initWithStartDate:eventType:action:reason:workoutType:];
-[CMActivityEventData setHeartRateRecoveryEndTime:];
-[CMActivityEventData setHeartRateRecoveryStartTime:];
-[CMActivityEventData sr_dictionaryRepresentation];
```
