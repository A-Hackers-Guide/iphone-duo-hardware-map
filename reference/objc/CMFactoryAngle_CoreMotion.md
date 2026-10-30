# `CMFactoryAngle`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _valid;
f _angleDegrees;
d _timestamp;
```

## Properties

```
@property (Tf,R,N,V_angleDegrees) angleDegrees;
@property (TB,R,N,GisValid,V_valid) valid;
@property (Td,R,N,V_timestamp) timestamp;
```

## Class methods

```
+[CMFactoryAngle supportsSecureCoding];
```

## Instance methods

```
-[CMFactoryAngle dealloc];
-[CMFactoryAngle timestamp];
-[CMFactoryAngle encodeWithCoder:];
-[CMFactoryAngle isValid];
-[CMFactoryAngle description];
-[CMFactoryAngle initWithCoder:];
-[CMFactoryAngle copyWithZone:];
-[CMFactoryAngle isEqual:];
-[CMFactoryAngle angleDegrees];
-[CMFactoryAngle initWithAngle:timestamp:];
```
