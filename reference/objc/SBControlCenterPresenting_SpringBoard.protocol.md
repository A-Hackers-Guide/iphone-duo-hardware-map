# `SBControlCenterPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisPresented) presented;
@property (TB,R,N,GisPresentedOrDismissing) presentedOrDismissing;
@property (TB,R,N,GisVisible) visible;
```

## Instance methods

```
-[SBControlCenterPresenting dismissAnimated:];
-[SBControlCenterPresenting isPresented];
-[SBControlCenterPresenting presentAnimated:completion:];
-[SBControlCenterPresenting handleMenuButtonTap];
-[SBControlCenterPresenting dismissAnimated:completion:];
-[SBControlCenterPresenting isVisible];
-[SBControlCenterPresenting isPresentedOrDismissing];
-[SBControlCenterPresenting canBePresented];
-[SBControlCenterPresenting presentAnimated:];
-[SBControlCenterPresenting handleIndirectStatusBarAction];
```
