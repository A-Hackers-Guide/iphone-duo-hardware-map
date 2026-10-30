# `CMSkiData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 10 properties, 19 instance methods, 1 class methods

## Instance variables

```
Q fRecordId;
@"NSUUID" fSourceId;
@"NSUUID" fSessionId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
d fRunDistance;
d fRunAvgSpeed;
d fRunMaxSpeed;
d fRunSlope;
d fRunElevationDescent;
```

## Properties

```
@property (TQ,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
@property (T@"NSUUID",R,N) sessionId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (Td,R,N) runDistance;
@property (Td,R,N) runAvgSpeed;
@property (Td,R,N) runMaxSpeed;
@property (Td,R,N) runSlope;
@property (Td,R,N) runElevationDescent;
```

## Class methods

```
+[CMSkiData supportsSecureCoding];
```

## Instance methods

```
-[CMSkiData startDate];
-[CMSkiData sourceId];
-[CMSkiData sessionId];
-[CMSkiData recordId];
-[CMSkiData dealloc];
-[CMSkiData endDate];
-[CMSkiData encodeWithCoder:];
-[CMSkiData description];
-[CMSkiData initWithCoder:];
-[CMSkiData copyWithZone:];
-[CMSkiData convertToSkiEntry:];
-[CMSkiData initWithRecordId:sourceId:sessionId:startDate:endDate:runDistance:runAvgSpeed:runMaxSpeed:runSlope:runElevationDescent:];
-[CMSkiData initWithSessionId:];
-[CMSkiData initWithSkiEntry:];
-[CMSkiData runAvgSpeed];
-[CMSkiData runDistance];
-[CMSkiData runElevationDescent];
-[CMSkiData runMaxSpeed];
-[CMSkiData runSlope];
```
