# `CLBIO_DeltaPosition`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
d _X;
d _Y;
d _Z;
```

## Properties

```
@property (Td,R,N,V_X) X;
@property (Td,R,N,V_Y) Y;
@property (Td,R,N,V_Z) Z;
```

## Class methods

```
+[CLBIO_DeltaPosition supportsSecureCoding];
```

## Instance methods

```
-[CLBIO_DeltaPosition encodeWithCoder:];
-[CLBIO_DeltaPosition isValid];
-[CLBIO_DeltaPosition initWithCoder:];
-[CLBIO_DeltaPosition copyWithZone:];
-[CLBIO_DeltaPosition isEqual:];
-[CLBIO_DeltaPosition X];
-[CLBIO_DeltaPosition Z];
-[CLBIO_DeltaPosition Y];
-[CLBIO_DeltaPosition initWithX:Y:Z:];
```
