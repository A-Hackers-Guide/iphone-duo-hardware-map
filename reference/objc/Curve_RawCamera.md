# `Curve`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 16 instance methods, 8 class methods

## Instance variables

```
@? _function;
@? _inverse;
d _domainMin;
d _domainMax;
d _rangeMin;
d _rangeMax;
```

## Properties

```
@property (T@?,C,V_function) function;
@property (T@?,C,V_inverse) inverse;
@property (Td,R,V_domainMin) domainMin;
@property (Td,R,V_domainMax) domainMax;
@property (Td,R,V_rangeMin) rangeMin;
@property (Td,R,V_rangeMax) rangeMax;
```

## Class methods

```
+[Curve curve];
+[Curve curveWithCount:xvalues:yvalues:];
+[Curve curveWithGamma:];
+[Curve curveWith:of:];
+[Curve curveWithBlock:andInverse:];
+[Curve curveWithBlock:domainMin:domainMax:];
+[Curve curveWithCount:domainMin:domainMax:values:];
+[Curve curveWithInverseOf:];
```

## Instance methods

```
-[Curve function];
-[Curve init];
-[Curve setFunction:];
-[Curve rangeMax];
-[Curve rangeMin];
-[Curve inverse];
-[Curve setInverse:];
-[Curve domainMax];
-[Curve domainMin];
-[Curve initWith:of:];
-[Curve initWithBlock:andInverse:];
-[Curve initWithBlock:domainMin:domainMax:];
-[Curve initWithCount:domainMin:domainMax:values:];
-[Curve initWithCount:xvalues:yvalues:];
-[Curve initWithGamma:];
-[Curve initWithInverseOf:];
```
