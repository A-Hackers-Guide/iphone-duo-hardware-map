# `SBMutableKeyboardFocusPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBKeyboardFocusPolicy`
- 0 instance variables, 5 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"SBKeyboardFocusTarget",&,D,N) keyboardFocusTarget;
@property (Tq,D,N) advicePolicy;
@property (TB,D,N) shouldSuppressRemoteDeferring;
@property (TB,D,N) suppressCameraButtonDeferringToApplications;
@property (T@"SBWindowScene",W,D,N) windowSceneAncestor;
```

## Instance methods

```
-[SBMutableKeyboardFocusPolicy init];
-[SBMutableKeyboardFocusPolicy copyWithZone:];
-[SBMutableKeyboardFocusPolicy setAdvicePolicy:];
-[SBMutableKeyboardFocusPolicy setKeyboardFocusTarget:];
-[SBMutableKeyboardFocusPolicy setShouldSuppressRemoteDeferring:];
-[SBMutableKeyboardFocusPolicy setSuppressCameraButtonDeferringToApplications:];
-[SBMutableKeyboardFocusPolicy setWindowSceneAncestor:];
```
