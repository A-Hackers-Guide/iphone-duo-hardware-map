# `UIFocusMovementAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"_UIFocusMovementInfo",R,N) focusMovementInfo;
@property (T@"_UIFocusInputDeviceInfo",R,N) inputDeviceInfo;
@property (TB,R,N) shouldPerformHapticFeedback;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) focusedFrame;
```

## Instance methods

```
-[UIFocusMovementAction UIActionType];
-[UIFocusMovementAction abortForUsageViolation:];
-[UIFocusMovementAction inputDeviceInfo];
-[UIFocusMovementAction focusMovementInfo];
-[UIFocusMovementAction focusedFrame];
-[UIFocusMovementAction initWithFocusMovementInfo:];
-[UIFocusMovementAction initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:];
-[UIFocusMovementAction initWithFocusMovementInfo:inputDeviceInfo:shouldPerformHapticFeedback:focusedFrameInSceneCoordinateSpace:];
-[UIFocusMovementAction shouldPerformHapticFeedback];
```
