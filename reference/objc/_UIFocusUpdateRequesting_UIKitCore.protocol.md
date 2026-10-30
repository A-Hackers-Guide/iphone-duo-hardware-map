# `_UIFocusUpdateRequesting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"UIFocusSystem",R,W,N) focusSystem;
@property (TB,R,N,GisMovementRequest) movementRequest;
@property (TB,R,N,GshouldScrollIfNecessary) scrollIfNecessary;
@property (TB,R,N) shouldPlayFocusSound;
@property (TB,R,N) shouldPerformHapticFeedback;
@property (TB,R,N) requiresNextFocusedItem;
@property (TB,R,N) requiresEnvironmentValidation;
@property (TB,R,N) allowsFocusingCurrentItem;
@property (TB,R,N) allowsDeferral;
@property (TB,R,N) allowsOverridingPreferedFocusEnvironments;
@property (T@"_UIFocusInputDeviceInfo",R,N) inputDeviceInfo;
```

## Instance methods

```
-[_UIFocusUpdateRequesting inputDeviceInfo];
-[_UIFocusUpdateRequesting focusSystem];
-[_UIFocusUpdateRequesting allowsDeferral];
-[_UIFocusUpdateRequesting allowsFocusingCurrentItem];
-[_UIFocusUpdateRequesting allowsOverridingPreferedFocusEnvironments];
-[_UIFocusUpdateRequesting isMovementRequest];
-[_UIFocusUpdateRequesting requiresEnvironmentValidation];
-[_UIFocusUpdateRequesting requiresNextFocusedItem];
-[_UIFocusUpdateRequesting shouldPerformHapticFeedback];
-[_UIFocusUpdateRequesting shouldPlayFocusSound];
-[_UIFocusUpdateRequesting shouldScrollIfNecessary];
```
