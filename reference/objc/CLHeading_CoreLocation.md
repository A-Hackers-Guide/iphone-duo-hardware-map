# `CLHeading`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (Tq,R,N) headingMode;
@property (Td,R,N) magneticHeading;
@property (Td,R,N) trueHeading;
@property (Td,R,N) headingAccuracy;
@property (Td,R,N) x;
@property (Td,R,N) y;
@property (Td,R,N) z;
@property (T@"NSDate",R,C,N) timestamp;
```

## Class methods

```
+[CLHeading supportsSecureCoding];
```

## Instance methods

```
-[CLHeading y];
-[CLHeading dealloc];
-[CLHeading timestamp];
-[CLHeading shortDescription];
-[CLHeading x];
-[CLHeading encodeWithCoder:];
-[CLHeading description];
-[CLHeading initWithCoder:];
-[CLHeading copyWithZone:];
-[CLHeading z];
-[CLHeading headingAccuracy];
-[CLHeading magneticHeading];
-[CLHeading initWithClientHeading:];
-[CLHeading trueHeading];
-[CLHeading headingMode];
```
