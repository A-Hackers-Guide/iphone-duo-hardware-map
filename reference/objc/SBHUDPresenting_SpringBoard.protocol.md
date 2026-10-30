# `SBHUDPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) identifier;
@property (T@"UIViewController<SBHUDViewControlling>",R,N) HUDViewController;
@property (TB,R,N,GisDismissalScheduled) dismissalScheduled;
@property (TB,R,N) isPresented;
@property (TB,R,N) isPresenting;
@property (TB,R,N) isDismissing;
@property (TB,R,N) isDismissed;
@property (TB,R,N) isVisible;
```

## Instance methods

```
-[SBHUDPresenting dismissAnimated:];
-[SBHUDPresenting isPresented];
-[SBHUDPresenting dismiss];
-[SBHUDPresenting identifier];
-[SBHUDPresenting isVisible];
-[SBHUDPresenting isDismissing];
-[SBHUDPresenting isPresenting];
-[SBHUDPresenting isDismissed];
-[SBHUDPresenting HUDViewController];
-[SBHUDPresenting invalidateDismissalTimer];
-[SBHUDPresenting isDismissalScheduled];
-[SBHUDPresenting presentWithDismissalInterval:];
-[SBHUDPresenting presentWithDismissalInterval:animated:];
-[SBHUDPresenting rescheduleDismissalTimer];
-[SBHUDPresenting scheduleDismissalTimer];
```
