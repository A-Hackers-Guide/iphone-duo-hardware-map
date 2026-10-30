# `CMDisplayGravity`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"CMAttitude" _attitude;
d _timestamp;
{?="x"d"y"d"z"d} _gravity;
```

## Properties

```
@property (T{?=ddd},R,N,V_gravity) gravity;
@property (T@"CMAttitude",R,N,V_attitude) attitude;
@property (Td,R,N,V_timestamp) timestamp;
```

## Class methods

```
+[CMDisplayGravity supportsSecureCoding];
```

## Instance methods

```
-[CMDisplayGravity dealloc];
-[CMDisplayGravity timestamp];
-[CMDisplayGravity gravity];
-[CMDisplayGravity encodeWithCoder:];
-[CMDisplayGravity description];
-[CMDisplayGravity initWithCoder:];
-[CMDisplayGravity copyWithZone:];
-[CMDisplayGravity isEqual:];
-[CMDisplayGravity attitude];
-[CMDisplayGravity initWithDisplayGravity:timestamp:];
```
