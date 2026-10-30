# `CMALSPhone`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" fTimestamp;
@"NSNumber" fIllumination;
```

## Properties

```
@property (T@"NSNumber",R,N) timestamp;
@property (T@"NSNumber",R,N) illumination;
```

## Class methods

```
+[CMALSPhone supportsSecureCoding];
```

## Instance methods

```
-[CMALSPhone dealloc];
-[CMALSPhone timestamp];
-[CMALSPhone encodeWithCoder:];
-[CMALSPhone description];
-[CMALSPhone initWithCoder:];
-[CMALSPhone copyWithZone:];
-[CMALSPhone initWithTimestamp:illumination:];
-[CMALSPhone illumination];
```
