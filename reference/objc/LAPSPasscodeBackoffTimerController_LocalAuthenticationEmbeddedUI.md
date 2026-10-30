# `LAPSPasscodeBackoffTimerController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _timer;
q _timeout;
@? _updateHandler;
@? _completionHandler;
```

## Instance methods

```
-[LAPSPasscodeBackoffTimerController start];
-[LAPSPasscodeBackoffTimerController _startTimerWithTimeout:];
-[LAPSPasscodeBackoffTimerController initWithTimeout:updateHandler:completionHandler:];
```
