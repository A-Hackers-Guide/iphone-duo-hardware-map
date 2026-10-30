# `CMWorkoutMetsData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDate" fStartDate;
@"NSDate" fEndDate;
@"NSNumber" fMets;
@"NSUUID" fSourceId;
@"NSUUID" fSessionId;
```

## Properties

```
@property (T@"NSNumber",R,N) mets;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (T@"NSUUID",R,N) sessionId;
@property (T@"NSUUID",R,N) sourceId;
```

## Class methods

```
+[CMWorkoutMetsData supportsSecureCoding];
```

## Instance methods

```
-[CMWorkoutMetsData startDate];
-[CMWorkoutMetsData sourceId];
-[CMWorkoutMetsData sessionId];
-[CMWorkoutMetsData dealloc];
-[CMWorkoutMetsData endDate];
-[CMWorkoutMetsData encodeWithCoder:];
-[CMWorkoutMetsData description];
-[CMWorkoutMetsData initWithCoder:];
-[CMWorkoutMetsData copyWithZone:];
-[CMWorkoutMetsData initWithCLWorkoutMets:];
-[CMWorkoutMetsData initWithSessionId:sourceId:startDate:endDate:mets:];
-[CMWorkoutMetsData mets];
```
