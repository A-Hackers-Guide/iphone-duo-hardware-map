# `CMPedestrianGrade`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
f fGrade;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Tf,R,N) grade;
```

## Class methods

```
+[CMPedestrianGrade supportsSecureCoding];
+[CMPedestrianGrade inputFromPreparedStatement:];
```

## Instance methods

```
-[CMPedestrianGrade startDate];
-[CMPedestrianGrade grade];
-[CMPedestrianGrade recordId];
-[CMPedestrianGrade dealloc];
-[CMPedestrianGrade encodeWithCoder:];
-[CMPedestrianGrade description];
-[CMPedestrianGrade initWithCoder:];
-[CMPedestrianGrade copyWithZone:];
-[CMPedestrianGrade isEqual:];
-[CMPedestrianGrade initWithSample:];
-[CMPedestrianGrade binarySampleRepresentation];
-[CMPedestrianGrade initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMPedestrianGrade initWithRecordId:startDate:grade:];
-[CMPedestrianGrade sr_dictionaryRepresentation];
```
