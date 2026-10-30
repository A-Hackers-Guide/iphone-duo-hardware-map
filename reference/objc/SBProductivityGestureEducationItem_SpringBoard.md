# `SBProductivityGestureEducationItem`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _displayDate;
@"NSMutableDictionary" _activationHistoryMap;
q _type;
q _lastActivatedEducationType;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (Tq,R,N,V_lastActivatedEducationType) lastActivatedEducationType;
```

## Class methods

```
+[SBProductivityGestureEducationItem supportsSecureCoding];
```

## Instance methods

```
-[SBProductivityGestureEducationItem initWithType:];
-[SBProductivityGestureEducationItem type];
-[SBProductivityGestureEducationItem encodeWithCoder:];
-[SBProductivityGestureEducationItem initWithCoder:];
-[SBProductivityGestureEducationItem copyWithZone:];
-[SBProductivityGestureEducationItem _policyInterval];
-[SBProductivityGestureEducationItem _policyCount];
-[SBProductivityGestureEducationItem contentDidAppear];
-[SBProductivityGestureEducationItem isValidWithActivationForType:];
-[SBProductivityGestureEducationItem lastActivatedEducationType];
-[SBProductivityGestureEducationItem resetActivations];
```
