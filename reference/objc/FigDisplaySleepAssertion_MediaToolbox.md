# `FigDisplaySleepAssertion`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _timer;
@"NSString" _reason;
@"<BSInvalidatable>" _idleTimerAssertion;
q _lastIdleTimerResetTime;
```

## Instance methods

```
-[FigDisplaySleepAssertion dealloc];
-[FigDisplaySleepAssertion initWithReason:queue:expirationHandler:];
-[FigDisplaySleepAssertion resetIdleTimerOnBehalfOfSceneWithPID:];
```
