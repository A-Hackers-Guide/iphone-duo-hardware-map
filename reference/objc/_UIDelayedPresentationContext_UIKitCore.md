# `_UIDelayedPresentationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _enableUserInteraction;
q _reqcnt;
@"NSInvocation" _presentInvocation;
@? _cancellationHandler;
d _timeout;
@"NSObject<OS_dispatch_source>" _timerSource;
@"UIWindowScene" _windowSceneIgnoringEvents;
```

## Properties

```
@property (T@?,C,N,V_cancellationHandler) cancellationHandler;
@property (T@"NSInvocation",&,N,V_presentInvocation) presentInvocation;
@property (T@"UIWindowScene",W,V_windowSceneIgnoringEvents) windowSceneIgnoringEvents;
```

## Instance methods

```
-[_UIDelayedPresentationContext requestCount];
-[_UIDelayedPresentationContext presentInvocation];
-[_UIDelayedPresentationContext initWithTimeout:cancellationHandler:];
-[_UIDelayedPresentationContext incrementRequestCount];
-[_UIDelayedPresentationContext delayingController];
-[_UIDelayedPresentationContext invocationTarget];
-[_UIDelayedPresentationContext dealloc];
-[_UIDelayedPresentationContext cancellationHandler];
-[_UIDelayedPresentationContext windowSceneIgnoringEvents];
-[_UIDelayedPresentationContext setWindowSceneIgnoringEvents:];
-[_UIDelayedPresentationContext decrementRequestCount];
-[_UIDelayedPresentationContext setCancellationHandler:];
-[_UIDelayedPresentationContext setPresentInvocation:];
```
