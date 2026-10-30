# `CMVO2MaxClassificationData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _biologicalSex;
q _ageLowerBound;
q _ageUpperBound;
q _classificationType;
d _vo2MaxLowerBound;
d _vo2MaxUpperBound;
```

## Properties

```
@property (Tq,R,N,V_biologicalSex) biologicalSex;
@property (Tq,R,N,V_ageLowerBound) ageLowerBound;
@property (Tq,R,N,V_ageUpperBound) ageUpperBound;
@property (Tq,R,N,V_classificationType) classificationType;
@property (Td,R,N,V_vo2MaxLowerBound) vo2MaxLowerBound;
@property (Td,R,N,V_vo2MaxUpperBound) vo2MaxUpperBound;
```

## Class methods

```
+[CMVO2MaxClassificationData supportsSecureCoding];
```

## Instance methods

```
-[CMVO2MaxClassificationData dealloc];
-[CMVO2MaxClassificationData classificationType];
-[CMVO2MaxClassificationData encodeWithCoder:];
-[CMVO2MaxClassificationData description];
-[CMVO2MaxClassificationData initWithCoder:];
-[CMVO2MaxClassificationData copyWithZone:];
-[CMVO2MaxClassificationData biologicalSex];
-[CMVO2MaxClassificationData ageLowerBound];
-[CMVO2MaxClassificationData ageUpperBound];
-[CMVO2MaxClassificationData vo2MaxLowerBound];
-[CMVO2MaxClassificationData vo2MaxUpperBound];
-[CMVO2MaxClassificationData initWithBiologicalSex:ageLowerBound:ageUpperBound:classificationType:vo2MaxLowerBound:vo2MaxUpperBound:];
```
