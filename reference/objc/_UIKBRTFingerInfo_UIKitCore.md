# `_UIKBRTFingerInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _unknownSeen;
d _radius;
d _lastSeenTimestamp;
Q _identity;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (T{CGPoint=dd},N,V_location) location;
@property (Td,N,V_radius) radius;
@property (Td,N,V_lastSeenTimestamp) lastSeenTimestamp;
@property (TQ,N,V_identity) identity;
@property (TB,N,V_unknownSeen) unknownSeen;
@property (Td,R,N) feedbackAlpha;
```

## Instance methods

```
-[_UIKBRTFingerInfo location];
-[_UIKBRTFingerInfo setIdentity:];
-[_UIKBRTFingerInfo setRadius:];
-[_UIKBRTFingerInfo radius];
-[_UIKBRTFingerInfo setLocation:];
-[_UIKBRTFingerInfo identity];
-[_UIKBRTFingerInfo description];
-[_UIKBRTFingerInfo copyWithZone:];
-[_UIKBRTFingerInfo isEqual:];
-[_UIKBRTFingerInfo setUnknownSeen:];
-[_UIKBRTFingerInfo feedbackAlpha];
-[_UIKBRTFingerInfo lastSeenTimestamp];
-[_UIKBRTFingerInfo setLastSeenTimestamp:];
-[_UIKBRTFingerInfo unknownSeen];
```
