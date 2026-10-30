# `CMLiveSkiData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _date;
d _distance;
d _averageSpeed;
d _verticalDescent;
i _runCount;
d _maximumSpeed;
```

## Properties

```
@property (T@"NSDate",R,N) date;
@property (Td,R,N) distance;
@property (Td,R,N) averageSpeed;
@property (Td,R,N) verticalDescent;
@property (TQ,R,N) runCount;
@property (Td,R,N) maximumSpeed;
```

## Class methods

```
+[CMLiveSkiData supportsSecureCoding];
```

## Instance methods

```
-[CMLiveSkiData distance];
-[CMLiveSkiData dealloc];
-[CMLiveSkiData date];
-[CMLiveSkiData encodeWithCoder:];
-[CMLiveSkiData description];
-[CMLiveSkiData initWithCoder:];
-[CMLiveSkiData copyWithZone:];
-[CMLiveSkiData verticalDescent];
-[CMLiveSkiData averageSpeed];
-[CMLiveSkiData initWithDate:distance:averageSpeed:verticalDescent:runCount:maximumSpeed:];
-[CMLiveSkiData maximumSpeed];
-[CMLiveSkiData runCount];
```
