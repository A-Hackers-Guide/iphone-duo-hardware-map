# `CMElevationData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `NSSecureCoding`, `NSCopying`
- 7 instance variables, 11 properties, 16 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSUUID" fSourceId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
Q fElevationAscended;
Q fElevationDescended;
q fSource;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
@property (Tq,R,N) source;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (TQ,R,N) elevationAscended;
@property (TQ,R,N) elevationDescended;
```

## Class methods

```
+[CMElevationData supportsSecureCoding];
+[CMElevationData sourceName:];
```

## Instance methods

```
-[CMElevationData startDate];
-[CMElevationData sourceId];
-[CMElevationData recordId];
-[CMElevationData dealloc];
-[CMElevationData endDate];
-[CMElevationData encodeWithCoder:];
-[CMElevationData description];
-[CMElevationData initWithCoder:];
-[CMElevationData copyWithZone:];
-[CMElevationData source];
-[CMElevationData binarySampleRepresentation];
-[CMElevationData elevationAscended];
-[CMElevationData elevationDescended];
-[CMElevationData initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMElevationData initWithSignificantElevationSample:];
-[CMElevationData initWithStartDate:endDate:elevationAscended:elevationDescended:source:recordId:sourceId:];
```
