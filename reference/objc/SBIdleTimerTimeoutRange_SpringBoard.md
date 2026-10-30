# `SBIdleTimerTimeoutRange`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _lowerTimeout;
d _upperTimeout;
```

## Properties

```
@property (Td,R,N,V_lowerTimeout) lowerTimeout;
@property (Td,R,N,V_upperTimeout) upperTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerTimeoutRange succinctDescriptionBuilder];
-[SBIdleTimerTimeoutRange descriptionWithMultilinePrefix:];
-[SBIdleTimerTimeoutRange succinctDescription];
-[SBIdleTimerTimeoutRange description];
-[SBIdleTimerTimeoutRange descriptionBuilderWithMultilinePrefix:];
-[SBIdleTimerTimeoutRange intersects:];
-[SBIdleTimerTimeoutRange clippedRangeWithFavoredRange:];
-[SBIdleTimerTimeoutRange initWithLowerTimeout:upperTimeout:];
-[SBIdleTimerTimeoutRange lowerTimeout];
-[SBIdleTimerTimeoutRange upperTimeout];
```
