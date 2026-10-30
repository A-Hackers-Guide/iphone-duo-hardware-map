# `CMVO2MaxClassificationThreshold`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _biologicalSex;
q _ageLowerBound;
q _ageUpperBound;
q _thresholdType;
d _slope;
d _intercept;
```

## Properties

```
@property (Tq,R,N,V_biologicalSex) biologicalSex;
@property (Tq,R,N,V_ageLowerBound) ageLowerBound;
@property (Tq,R,N,V_ageUpperBound) ageUpperBound;
@property (Tq,R,N,V_thresholdType) thresholdType;
@property (Td,R,N,V_slope) slope;
@property (Td,R,N,V_intercept) intercept;
```

## Class methods

```
+[CMVO2MaxClassificationThreshold supportsSecureCoding];
```

## Instance methods

```
-[CMVO2MaxClassificationThreshold dealloc];
-[CMVO2MaxClassificationThreshold encodeWithCoder:];
-[CMVO2MaxClassificationThreshold description];
-[CMVO2MaxClassificationThreshold initWithCoder:];
-[CMVO2MaxClassificationThreshold copyWithZone:];
-[CMVO2MaxClassificationThreshold biologicalSex];
-[CMVO2MaxClassificationThreshold ageLowerBound];
-[CMVO2MaxClassificationThreshold ageUpperBound];
-[CMVO2MaxClassificationThreshold intercept];
-[CMVO2MaxClassificationThreshold slope];
-[CMVO2MaxClassificationThreshold thresholdType];
-[CMVO2MaxClassificationThreshold initWithBiologicalSex:ageLowerBound:ageUpperBound:thresholdType:slope:intercept:];
```
