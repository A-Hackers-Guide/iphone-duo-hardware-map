# `SBSATimerDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSATimerDescribing`
- 2 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _timerDescriptionIdentifier;
d _timeInterval;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_timerDescriptionIdentifier) timerDescriptionIdentifier;
@property (Td,R,N,V_timeInterval) timeInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSATimerDescription timeInterval];
-[SBSATimerDescription initWithTimeInterval:];
-[SBSATimerDescription hash];
-[SBSATimerDescription description];
-[SBSATimerDescription _hashBuilder];
-[SBSATimerDescription copyWithZone:];
-[SBSATimerDescription isEqual:];
-[SBSATimerDescription _equalsBuilder:];
-[SBSATimerDescription _initWithIdentifier:timeInterval:];
-[SBSATimerDescription _mutableDescriptionMissingClosingAngleBracket];
-[SBSATimerDescription timerDescriptionIdentifier];
```
