# `CTCAServiceIntervals`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _atStart;
@"NSDate" _startsAt;
@"NSDate" _endsAt;
@"NSArray" _changesAt;
```

## Properties

```
@property (T@"NSDate",&,N,V_startsAt) startsAt;
@property (T@"NSDate",&,N,V_endsAt) endsAt;
@property (TB,N,V_atStart) atStart;
@property (T@"NSArray",&,N,V_changesAt) changesAt;
```

## Class methods

```
+[CTCAServiceIntervals supportsSecureCoding];
```

## Instance methods

```
-[CTCAServiceIntervals encodeWithCoder:];
-[CTCAServiceIntervals description];
-[CTCAServiceIntervals initWithCoder:];
-[CTCAServiceIntervals copyWithZone:];
-[CTCAServiceIntervals atStart];
-[CTCAServiceIntervals changesAt];
-[CTCAServiceIntervals endsAt];
-[CTCAServiceIntervals setAtStart:];
-[CTCAServiceIntervals setChangesAt:];
-[CTCAServiceIntervals setEndsAt:];
-[CTCAServiceIntervals setStartsAt:];
-[CTCAServiceIntervals startsAt];
```
