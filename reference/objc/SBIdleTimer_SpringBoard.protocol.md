# `SBIdleTimer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`, `BSDescriptionProviding`
- 0 instance variables, 1 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisDisabled) disabled;
```

## Instance methods

```
-[SBIdleTimer reset];
-[SBIdleTimer isDisabled];
-[SBIdleTimer stateCaptureDescriptionWithMultilinePrefix:];
-[SBIdleTimer addIdleTimerObserver:];
-[SBIdleTimer removeAllIdleTimerObservers];
-[SBIdleTimer removeIdleTimerObserver:];
```
