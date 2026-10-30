# `CAMBarsAccessibilityHUDManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIView<CAMBarsAccessibilityHUDManagerGestureProvider><CAMAccessibilityHUDItemProvider>" _view;
@"<CAMBarsAccessibilityHUDManagerDelegate>" _delegate;
@"UILongPressGestureRecognizer" __accessibilityLongPressGestureRecognizer;
```

## Properties

```
@property (T@"<CAMBarsAccessibilityHUDManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView<CAMBarsAccessibilityHUDManagerGestureProvider><CAMAccessibilityHUDItemProvider>",W,N,V_view) view;
@property (T@"UILongPressGestureRecognizer",&,N,S_setAccessibilityLongPressGestureRecognizer:,V__accessibilityLongPressGestureRecognizer) _accessibilityLongPressGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMBarsAccessibilityHUDManager setView:];
-[CAMBarsAccessibilityHUDManager view];
-[CAMBarsAccessibilityHUDManager setDelegate:];
-[CAMBarsAccessibilityHUDManager gestureRecognizerShouldBegin:];
-[CAMBarsAccessibilityHUDManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[CAMBarsAccessibilityHUDManager delegate];
-[CAMBarsAccessibilityHUDManager _accessibilityLongPressGestureRecognizer];
-[CAMBarsAccessibilityHUDManager _handleAccessibilityLongPressGesture:];
-[CAMBarsAccessibilityHUDManager _setAccessibilityLongPressGestureRecognizer:];
-[CAMBarsAccessibilityHUDManager initWithView:delegate:cancelsTouchesInView:];
-[CAMBarsAccessibilityHUDManager locationOfAccessibilityGestureInView:];
```
