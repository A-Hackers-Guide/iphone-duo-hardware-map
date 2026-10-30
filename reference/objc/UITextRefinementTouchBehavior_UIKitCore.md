# `UITextRefinementTouchBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextRefinementInteractionBehaviorDelegate`
- 6 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _isShiftKeyBeingHeld;
@"UITextRange" _originalTextRange;
q _activeSelectionMode;
@"_UIKeyboardTextSelectionController" _activeSelectionController;
@"UITextLoupeSession" _loupeSession;
@"<_UIInvalidatable>" _grabberHandleSuppressionAssertion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextRefinementTouchBehavior configureLoupeGestureRecognizer:forTextLoupeInteraction:];
-[UITextRefinementTouchBehavior _allowsPaintSelectionForLoupeInteraction:];
-[UITextRefinementTouchBehavior velocityInView:forLoupeGesture:];
-[UITextRefinementTouchBehavior gestureRecognizerClassForLoupeInteraction:];
-[UITextRefinementTouchBehavior adjustVariableDelaySettingsForLoupeInteraction:];
-[UITextRefinementTouchBehavior textLoupeInteraction:gestureChangedWithState:location:translation:velocity:modifierFlags:shouldCancel:];
-[UITextRefinementTouchBehavior translationInView:forLoupeGesture:];
-[UITextRefinementTouchBehavior startPointForLoupeGesture:];
-[UITextRefinementTouchBehavior usesTouchAlignment];
-[UITextRefinementTouchBehavior loupeGestureRecognizerShouldBegin:forTextLoupeInteraction:];
-[UITextRefinementTouchBehavior configureGestureExclusionRequirementsForTextLoupeInteraction:];
-[UITextRefinementTouchBehavior shouldAllowEnforcedTouchTypeForTouch:forGestureRecognizer:];
-[UITextRefinementTouchBehavior triggeredByLongPressGesture:];
```
