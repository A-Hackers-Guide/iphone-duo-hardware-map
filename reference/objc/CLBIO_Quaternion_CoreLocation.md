# `CLBIO_Quaternion`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
d _X;
d _Y;
d _Z;
d _W;
```

## Properties

```
@property (Td,R,N,V_X) X;
@property (Td,R,N,V_Y) Y;
@property (Td,R,N,V_Z) Z;
@property (Td,R,N,V_W) W;
```

## Class methods

```
+[CLBIO_Quaternion supportsSecureCoding];
```

## Instance methods

```
-[CLBIO_Quaternion encodeWithCoder:];
-[CLBIO_Quaternion initWithCoder:];
-[CLBIO_Quaternion copyWithZone:];
-[CLBIO_Quaternion isEqual:];
-[CLBIO_Quaternion initWithX:Y:Z:W:];
-[CLBIO_Quaternion X];
-[CLBIO_Quaternion Z];
-[CLBIO_Quaternion W];
-[CLBIO_Quaternion Y];
```
