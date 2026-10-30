# `_UIKeyboardBasedTextSelectionInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKeyboardTextSelectionInteraction`
- 1 instance variables, 1 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UITextGestureTuning" _gestureTuning;
```

## Properties

```
@property (T@"UITextGestureTuning",R,N,V_gestureTuning) gestureTuning;
```

## Instance methods

```
-[_UIKeyboardBasedTextSelectionInteraction owner];
-[_UIKeyboardBasedTextSelectionInteraction gestureRecognizer:shouldReceiveTouch:];
-[_UIKeyboardBasedTextSelectionInteraction gestureTuning];
-[_UIKeyboardBasedTextSelectionInteraction dealloc];
-[_UIKeyboardBasedTextSelectionInteraction _processGestureForCustomHighlighter:];
-[_UIKeyboardBasedTextSelectionInteraction _createGestureTuningIfNecessary];
-[_UIKeyboardBasedTextSelectionInteraction endOneFingerSelectWithExecutionContext:];
-[_UIKeyboardBasedTextSelectionInteraction oneFingerForcePan:];
-[_UIKeyboardBasedTextSelectionInteraction oneFingerForcePress:];
-[_UIKeyboardBasedTextSelectionInteraction transitionFromBlockMagnifyToBlockSelectWithLocation:viaDrag:];
-[_UIKeyboardBasedTextSelectionInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIKeyboardBasedTextSelectionInteraction beginOneFingerSelectWithTranslation:executionContext:];
-[_UIKeyboardBasedTextSelectionInteraction updateOneFingerSelectWithTranslation:executionContext:];
-[_UIKeyboardBasedTextSelectionInteraction enclosingScrollViewIsScrolling];
-[_UIKeyboardBasedTextSelectionInteraction didMoveToView:];
```
