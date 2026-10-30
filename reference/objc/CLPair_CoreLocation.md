# `CLPair`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
i _first;
i _second;
```

## Properties

```
@property (Ti,R,N,V_first) first;
@property (Ti,R,N,V_second) second;
```

## Class methods

```
+[CLPair supportsSecureCoding];
```

## Instance methods

```
-[CLPair initWithFirst:second:];
-[CLPair second];
-[CLPair first];
-[CLPair encodeWithCoder:];
-[CLPair initWithCoder:];
-[CLPair copyWithZone:];
```
