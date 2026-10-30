# `_UISystemAppearanceManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 10 instance variables, 15 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _homeIndicatorAutoHidden;
Q _screenEdgesDeferringSystemGestures;
q _userInterfaceStyle;
q _whitePointAdaptivityStyle;
@"NSArray" _multitaskingDragExclusionRects;
Q _supportedInterfaceOrientations;
q _preferredInterfaceOrientation;
@"UIWindowScene" _windowScene;
@"UIWindow" _previousWindowDrivingSystemAppearance;
@"<BSInvalidatable>" _stateCaptureToken;
```

## Properties

```
@property (T@"UIWindowScene",&,N,V_windowScene) windowScene;
@property (T@"UIWindow",W,N,V_previousWindowDrivingSystemAppearance) previousWindowDrivingSystemAppearance;
@property (T@"<BSInvalidatable>",&,N,V_stateCaptureToken) stateCaptureToken;
@property (TB,R,N,V_homeIndicatorAutoHidden) homeIndicatorAutoHidden;
@property (TQ,R,N,V_screenEdgesDeferringSystemGestures) screenEdgesDeferringSystemGestures;
@property (Tq,R,N,V_userInterfaceStyle) userInterfaceStyle;
@property (Tq,R,N,V_whitePointAdaptivityStyle) whitePointAdaptivityStyle;
@property (T@"NSArray",R,N,V_multitaskingDragExclusionRects) multitaskingDragExclusionRects;
@property (TQ,R,N,V_supportedInterfaceOrientations) supportedInterfaceOrientations;
@property (Tq,R,N,V_preferredInterfaceOrientation) preferredInterfaceOrientation;
@property (T@"UIScene",W,N,G_scene,S_setScene:) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISystemAppearanceManager updateWhitePointAdaptivityStyle];
-[_UISystemAppearanceManager setWindowScene:];
-[_UISystemAppearanceManager preferredInterfaceOrientation];
-[_UISystemAppearanceManager _scene];
-[_UISystemAppearanceManager updateMultitaskingDragExclusionRects];
-[_UISystemAppearanceManager supportedInterfaceOrientations];
-[_UISystemAppearanceManager homeIndicatorAutoHidden];
-[_UISystemAppearanceManager multitaskingDragExclusionRects];
-[_UISystemAppearanceManager dealloc];
-[_UISystemAppearanceManager updateScreenEdgesDeferringSystemGestures];
-[_UISystemAppearanceManager _handleWindowVisibilityNotification:];
-[_UISystemAppearanceManager updateHomeIndicatorAutoHidden];
-[_UISystemAppearanceManager initWithScene:];
-[_UISystemAppearanceManager updateUserInterfaceStyle];
-[_UISystemAppearanceManager userInterfaceStyle];
-[_UISystemAppearanceManager setStateCaptureToken:];
-[_UISystemAppearanceManager previousWindowDrivingSystemAppearance];
-[_UISystemAppearanceManager _logOrientationPreferencesChangeWithOldSupportedOrientations:newSupportedOrientations:oldPreferredOrientation:newPreferredOrientation:animationSettings:fenced:];
-[_UISystemAppearanceManager window:didUpdateSupportedOrientations:preferredOrientation:prefersAnimation:];
-[_UISystemAppearanceManager screenEdgesDeferringSystemGestures];
-[_UISystemAppearanceManager _windowDrivingSystemAppearanceDidChange:];
-[_UISystemAppearanceManager setPreviousWindowDrivingSystemAppearance:];
-[_UISystemAppearanceManager _setScene:];
-[_UISystemAppearanceManager _findWindowDrivingSystemAppearance];
-[_UISystemAppearanceManager windowScene];
-[_UISystemAppearanceManager whitePointAdaptivityStyle];
-[_UISystemAppearanceManager stateCaptureToken];
```
