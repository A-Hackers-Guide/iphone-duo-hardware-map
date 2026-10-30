# `_UICarPlaySessionAccessRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _timer;
@? _completion;
@? _timeoutHandler;
```

## Properties

```
@property (T@?,C,N,V_completion) completion;
@property (T@?,C,N,V_timeoutHandler) timeoutHandler;
```

## Instance methods

```
-[_UICarPlaySessionAccessRequest setCompletion:];
-[_UICarPlaySessionAccessRequest setTimeoutHandler:];
-[_UICarPlaySessionAccessRequest completion];
-[_UICarPlaySessionAccessRequest timeoutHandler];
-[_UICarPlaySessionAccessRequest dealloc];
-[_UICarPlaySessionAccessRequest _cancelTimer];
-[_UICarPlaySessionAccessRequest initWithTimeout:completion:];
```
