# `SBIdleTimerTimeoutPrecedenceSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
d _normalTimeout;
d _highTimeout;
d _criticalTimeout;
```

## Properties

```
@property (Td,R,N,V_normalTimeout) normalTimeout;
@property (Td,R,N,V_highTimeout) highTimeout;
@property (Td,R,N,V_criticalTimeout) criticalTimeout;
@property (TQ,R,N) highestPrecedence;
@property (Td,R,N) leastTimeout;
@property (Td,R,N) greatestTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerTimeoutPrecedenceSettings succinctDescriptionBuilder];
-[SBIdleTimerTimeoutPrecedenceSettings descriptionWithMultilinePrefix:];
-[SBIdleTimerTimeoutPrecedenceSettings succinctDescription];
-[SBIdleTimerTimeoutPrecedenceSettings description];
-[SBIdleTimerTimeoutPrecedenceSettings descriptionBuilderWithMultilinePrefix:];
-[SBIdleTimerTimeoutPrecedenceSettings greatestTimeout];
-[SBIdleTimerTimeoutPrecedenceSettings criticalTimeout];
-[SBIdleTimerTimeoutPrecedenceSettings _intervalForPrecedence:];
-[SBIdleTimerTimeoutPrecedenceSettings _setTimeout:ifGreatestForPrecedence:];
-[SBIdleTimerTimeoutPrecedenceSettings _setTimeout:ifLeastForPrecedence:];
-[SBIdleTimerTimeoutPrecedenceSettings _setTimeout:withPrecedence:];
-[SBIdleTimerTimeoutPrecedenceSettings highTimeout];
-[SBIdleTimerTimeoutPrecedenceSettings highestPrecedence];
-[SBIdleTimerTimeoutPrecedenceSettings leastTimeout];
-[SBIdleTimerTimeoutPrecedenceSettings normalTimeout];
```
