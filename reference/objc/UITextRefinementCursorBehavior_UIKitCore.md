# `UITextRefinementCursorBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextRefinementInteractionBehaviorDelegate`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_UIKeyboardTextSelectionController" _activeSelectionController;
@ _grabberHandleSuppressionAssertion;
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
-[UITextRefinementCursorBehavior configureLoupeGestureRecognizer:forTextLoupeInteraction:];
-[UITextRefinementCursorBehavior velocityInView:forLoupeGesture:];
-[UITextRefinementCursorBehavior gestureRecognizerClassForLoupeInteraction:];
-[UITextRefinementCursorBehavior adjustVariableDelaySettingsForLoupeInteraction:];
-[UITextRefinementCursorBehavior textLoupeInteraction:gestureChangedWithState:location:translation:velocity:modifierFlags:shouldCancel:];
-[UITextRefinementCursorBehavior translationInView:forLoupeGesture:];
-[UITextRefinementCursorBehavior startPointForLoupeGesture:];
-[UITextRefinementCursorBehavior usesTouchAlignment];
-[UITextRefinementCursorBehavior loupeGestureRecognizerShouldBegin:forTextLoupeInteraction:];
-[UITextRefinementCursorBehavior configureGestureExclusionRequirementsForTextLoupeInteraction:];
-[UITextRefinementCursorBehavior shouldAllowEnforcedTouchTypeForTouch:forGestureRecognizer:];
-[UITextRefinementCursorBehavior triggeredByLongPressGesture:];
```
