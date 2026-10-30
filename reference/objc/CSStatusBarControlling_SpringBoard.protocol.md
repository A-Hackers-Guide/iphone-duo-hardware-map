# `CSStatusBarControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSNumber",R,N) statusBarAlpha;
@property (Tq,R,N) statusBarStyle;
@property (T@"_UILegibilitySettings",R,N) statusBarLegibilitySettings;
```

## Instance methods

```
-[CSStatusBarControlling statusBarAlpha];
-[CSStatusBarControlling statusBarStyle];
-[CSStatusBarControlling clearStatusBarParameters];
-[CSStatusBarControlling createFakeStatusBarWithReason:withFrame:];
-[CSStatusBarControlling destroyFakeStatusBar:];
-[CSStatusBarControlling effectiveStatusBarStyleRequestForAlpha:style:legibilitySettings:];
-[CSStatusBarControlling setStatusBarAlpha:style:legibilitySettings:];
-[CSStatusBarControlling setStatusBarHidden:forReason:];
-[CSStatusBarControlling setStatusBarPart:hidden:animationDuration:];
-[CSStatusBarControlling statusBarLegibilitySettings];
```
