# `NIHeading`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _timestamp;
d _trueHeading;
d _magneticHeading;
d _headingAccuracy;
```

## Properties

```
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (Td,N,V_trueHeading) trueHeading;
@property (Td,N,V_magneticHeading) magneticHeading;
@property (Td,N,V_headingAccuracy) headingAccuracy;
```

## Class methods

```
+[NIHeading supportsSecureCoding];
```

## Instance methods

```
-[NIHeading setTimestamp:];
-[NIHeading descriptionInternal];
-[NIHeading timestamp];
-[NIHeading encodeWithCoder:];
-[NIHeading hash];
-[NIHeading description];
-[NIHeading initWithCoder:];
-[NIHeading copyWithZone:];
-[NIHeading isEqual:];
-[NIHeading headingAccuracy];
-[NIHeading magneticHeading];
-[NIHeading setHeadingAccuracy:];
-[NIHeading trueHeading];
-[NIHeading setTrueHeading:];
-[NIHeading setMagneticHeading:];
-[NIHeading initWithTimestamp:trueHeading:magneticHeading:headingAccuracy:];
```
