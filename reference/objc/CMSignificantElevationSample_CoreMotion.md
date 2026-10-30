# `CMSignificantElevationSample`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
Q fRecordId;
@"NSUUID" fSourceId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
@"NSNumber" fElevationAscended;
@"NSNumber" fElevationDescended;
```

## Properties

```
@property (TQ,R,N,VfRecordId) recordId;
@property (T@"NSUUID",R,N,VfSourceId) sourceId;
@property (T@"NSDate",R,N,VfStartDate) startDate;
@property (T@"NSDate",R,N,VfEndDate) endDate;
@property (T@"NSNumber",R,N,VfElevationAscended) elevationAscended;
@property (T@"NSNumber",R,N,VfElevationDescended) elevationDescended;
```

## Class methods

```
+[CMSignificantElevationSample supportsSecureCoding];
```

## Instance methods

```
-[CMSignificantElevationSample startDate];
-[CMSignificantElevationSample sourceId];
-[CMSignificantElevationSample recordId];
-[CMSignificantElevationSample dealloc];
-[CMSignificantElevationSample endDate];
-[CMSignificantElevationSample encodeWithCoder:];
-[CMSignificantElevationSample description];
-[CMSignificantElevationSample initWithCoder:];
-[CMSignificantElevationSample copyWithZone:];
-[CMSignificantElevationSample elevationAscended];
-[CMSignificantElevationSample elevationDescended];
-[CMSignificantElevationSample initWithFilteredElevation:];
-[CMSignificantElevationSample initWithRecordId:sourceId:startDate:endDate:elevationAscended:elevationDescended:];
-[CMSignificantElevationSample initWithSignificantElevation:];
```
