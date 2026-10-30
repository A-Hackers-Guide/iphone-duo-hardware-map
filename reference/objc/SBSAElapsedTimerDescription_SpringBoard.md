# `SBSAElapsedTimerDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSATimerDescription`
- Protocols: `SBSAElapsedTimerDescribing`
- 1 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _elapsed;
```

## Properties

```
@property (TB,R,N,GisElapsed,V_elapsed) elapsed;
@property (T@"NSUUID",R,C,N) timerDescriptionIdentifier;
@property (Td,R,N) timeInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSAElapsedTimerDescription _hashBuilder];
-[SBSAElapsedTimerDescription copyWithZone:];
-[SBSAElapsedTimerDescription _equalsBuilder:];
-[SBSAElapsedTimerDescription _mutableDescriptionMissingEndAngleBracket];
-[SBSAElapsedTimerDescription initElapsedTimerDescriptionWithDescription:];
-[SBSAElapsedTimerDescription isElapsed];
```
