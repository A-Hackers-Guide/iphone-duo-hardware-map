# `_UIKeyboardLayoutAlignmentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 1 properties, 16 instance methods, 3 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} lastKnownKeyboardRect;
@"NSLayoutConstraint" bottomConstraint;
@"NSLayoutConstraint" widthConstraint;
@"NSLayoutConstraint" heightConstraint;
@"NSLayoutConstraint" disambiguatingLeftConstraint;
B _automaticKeyboardFrameTrackingDisabled;
```

## Properties

```
@property (TB,N,V_automaticKeyboardFrameTrackingDisabled) automaticKeyboardFrameTrackingDisabled;
```

## Class methods

```
+[_UIKeyboardLayoutAlignmentView _endFrameForNotification:inView:];
+[_UIKeyboardLayoutAlignmentView _shouldIgnoreFrameChangeNotification:inView:];
+[_UIKeyboardLayoutAlignmentView _frameInBoundsForKeyboardFrame:inView:];
```

## Instance methods

```
-[_UIKeyboardLayoutAlignmentView _shouldOverrideAnimationForFrameChangeNotification:];
-[_UIKeyboardLayoutAlignmentView didMoveToWindow];
-[_UIKeyboardLayoutAlignmentView setAutomaticKeyboardFrameTrackingDisabled:];
-[_UIKeyboardLayoutAlignmentView _keyboardChanged:];
-[_UIKeyboardLayoutAlignmentView _updateConstraintsForKeyboardNotification:];
-[_UIKeyboardLayoutAlignmentView dealloc];
-[_UIKeyboardLayoutAlignmentView willMoveToWindow:];
-[_UIKeyboardLayoutAlignmentView automaticKeyboardFrameTrackingDisabled];
-[_UIKeyboardLayoutAlignmentView _startObservingKeyboardNotificationsForScreen:];
-[_UIKeyboardLayoutAlignmentView _frameInBoundsForKeyboardFrame:];
-[_UIKeyboardLayoutAlignmentView _createConstraints];
-[_UIKeyboardLayoutAlignmentView initWithFrame:];
-[_UIKeyboardLayoutAlignmentView _stopObservingKeyboardNotifications];
-[_UIKeyboardLayoutAlignmentView _matchInitialKeyboardFrame];
-[_UIKeyboardLayoutAlignmentView _updateConstraintsToMatchKeyboardFrame:];
-[_UIKeyboardLayoutAlignmentView _removeConstraints];
```
