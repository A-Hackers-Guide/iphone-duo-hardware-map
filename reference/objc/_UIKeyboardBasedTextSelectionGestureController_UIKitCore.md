# `_UIKeyboardBasedTextSelectionGestureController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKeyboardTextSelectionGestureController`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _delayForceMagnify;
B _didLongForcePress;
```

## Properties

```
@property (TB,N,V_delayForceMagnify) delayForceMagnify;
@property (TB,N,V_didLongForcePress) didLongForcePress;
```

## Class methods

```
+[_UIKeyboardBasedTextSelectionGestureController sharedInstance];
```

## Instance methods

```
-[_UIKeyboardBasedTextSelectionGestureController oneFingerForcePressShouldFailWithoutForce];
-[_UIKeyboardBasedTextSelectionGestureController textInteractionClass];
-[_UIKeyboardBasedTextSelectionGestureController oneFingerForcePressShouldCancelTouchesInView];
-[_UIKeyboardBasedTextSelectionGestureController setDidLongForcePress:];
-[_UIKeyboardBasedTextSelectionGestureController didLongForcePress];
-[_UIKeyboardBasedTextSelectionGestureController setDelayForceMagnify:];
-[_UIKeyboardBasedTextSelectionGestureController _cleanupDeadGesturesIfNecessary];
-[_UIKeyboardBasedTextSelectionGestureController oneFingerForcePressMinimumDuration];
-[_UIKeyboardBasedTextSelectionGestureController allowOneFingerDeepPress];
-[_UIKeyboardBasedTextSelectionGestureController delayForceMagnify];
```
