# `CMDisplayAngle`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _angleStable;
f _angleDegrees;
d _timestamp;
```

## Properties

```
@property (Tf,R,N,V_angleDegrees) angleDegrees;
@property (TB,R,N,GisAngleStable,V_angleStable) angleStable;
@property (Td,R,N,V_timestamp) timestamp;
```

## Class methods

```
+[CMDisplayAngle supportsSecureCoding];
```

## Instance methods

```
-[CMDisplayAngle dealloc];
-[CMDisplayAngle timestamp];
-[CMDisplayAngle encodeWithCoder:];
-[CMDisplayAngle description];
-[CMDisplayAngle initWithCoder:];
-[CMDisplayAngle copyWithZone:];
-[CMDisplayAngle isEqual:];
-[CMDisplayAngle angleDegrees];
-[CMDisplayAngle initWithDisplayAngle:timestamp:];
-[CMDisplayAngle isAngleStable];
```
