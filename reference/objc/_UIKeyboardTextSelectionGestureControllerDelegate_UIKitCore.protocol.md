# `_UIKeyboardTextSelectionGestureControllerDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"UIKeyboardTaskQueue",R,N) taskQueue;
@property (T@"_UIKeyboardTextSelectionController",R,N) textSelectionController;
@property (Td,?,R,N) timestampOfLastTouchesEnded;
```

## Instance methods

```
-[_UIKeyboardTextSelectionGestureControllerDelegate taskQueue];
-[_UIKeyboardTextSelectionGestureControllerDelegate textSelectionController];
-[_UIKeyboardTextSelectionGestureControllerDelegate transitionInProgress];
-[_UIKeyboardTextSelectionGestureControllerDelegate setTwoFingerTapTimestamp:];
-[_UIKeyboardTextSelectionGestureControllerDelegate shouldAllowSelectionGestures:atPoint:toBegin:];
-[_UIKeyboardTextSelectionGestureControllerDelegate timestampOfLastTouchesEnded];
-[_UIKeyboardTextSelectionGestureControllerDelegate hasMarkedText];
-[_UIKeyboardTextSelectionGestureControllerDelegate didEndGesture];
-[_UIKeyboardTextSelectionGestureControllerDelegate willBeginGesture];
-[_UIKeyboardTextSelectionGestureControllerDelegate shouldAllowTwoFingerSelectionGestureOnView:];
```
