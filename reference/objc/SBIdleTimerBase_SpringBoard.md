# `SBIdleTimerBase`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerActivation`, `SBIdleTimer`
- 1 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"NSHashTable",R,N,V_observers) observers;
@property (TB,N,GisActivated) activated;
@property (TB,R,N,GisDisabled) disabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerBase isActivated];
-[SBIdleTimerBase setActivated:];
-[SBIdleTimerBase succinctDescriptionBuilder];
-[SBIdleTimerBase _logExpirationTimeout:];
-[SBIdleTimerBase reset];
-[SBIdleTimerBase descriptionWithMultilinePrefix:];
-[SBIdleTimerBase isDisabled];
-[SBIdleTimerBase succinctDescription];
-[SBIdleTimerBase hash];
-[SBIdleTimerBase _enumerateObserversRespondingToSelector:usingBlock:];
-[SBIdleTimerBase description];
-[SBIdleTimerBase stateCaptureDescriptionWithMultilinePrefix:];
-[SBIdleTimerBase observers];
-[SBIdleTimerBase isEqualToTimer:];
-[SBIdleTimerBase copyWithZone:];
-[SBIdleTimerBase descriptionBuilderWithMultilinePrefix:];
-[SBIdleTimerBase conformsToSBIdleTimerActivation];
-[SBIdleTimerBase _makeObserversPerformSelector:];
-[SBIdleTimerBase addIdleTimerObserver:];
-[SBIdleTimerBase removeAllIdleTimerObservers];
-[SBIdleTimerBase removeIdleTimerObserver:];
```
