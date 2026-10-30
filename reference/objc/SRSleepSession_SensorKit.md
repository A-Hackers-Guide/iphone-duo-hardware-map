# `SRSleepSession`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSCopying`, `NSSecureCoding`
- 5 instance variables, 9 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _startDate;
d _duration;
@"NSString" _identifier;
q _startReason;
q _endReason;
```

## Properties

```
@property (T@"NSDate",&,N,V_startDate) startDate;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Td,N,V_duration) duration;
@property (Tq,R,N,V_startReason) startReason;
@property (Tq,R,N,V_endReason) endReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRSleepSession supportsSecureCoding];
+[SRSleepSession initialize];
```

## Instance methods

```
-[SRSleepSession startDate];
-[SRSleepSession setStartDate:];
-[SRSleepSession identifier];
-[SRSleepSession dealloc];
-[SRSleepSession endReason];
-[SRSleepSession duration];
-[SRSleepSession setIdentifier:];
-[SRSleepSession encodeWithCoder:];
-[SRSleepSession hash];
-[SRSleepSession description];
-[SRSleepSession initWithCoder:];
-[SRSleepSession setDuration:];
-[SRSleepSession copyWithZone:];
-[SRSleepSession isEqual:];
-[SRSleepSession startReason];
-[SRSleepSession binarySampleRepresentation];
-[SRSleepSession initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRSleepSession initWithStartDate:identifier:duration:];
-[SRSleepSession initWithStartDate:startReason:endReason:identifier:duration:];
```
