# `UITextRefinementAcceleratedTouchBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextRefinementInteractionBehaviorDelegate`
- 3 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UITextRange" _originalTextRange;
@"_UIKeyboardTextSelectionController" _activeSelectionController;
@"UITextLoupeSession" _loupeSession;
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
-[UITextRefinementAcceleratedTouchBehavior configureLoupeGestureRecognizer:forTextLoupeInteraction:];
-[UITextRefinementAcceleratedTouchBehavior velocityInView:forLoupeGesture:];
-[UITextRefinementAcceleratedTouchBehavior gestureRecognizerClassForLoupeInteraction:];
-[UITextRefinementAcceleratedTouchBehavior adjustVariableDelaySettingsForLoupeInteraction:];
-[UITextRefinementAcceleratedTouchBehavior textLoupeInteraction:gestureChangedWithState:location:translation:velocity:modifierFlags:shouldCancel:];
-[UITextRefinementAcceleratedTouchBehavior translationInView:forLoupeGesture:];
-[UITextRefinementAcceleratedTouchBehavior startPointForLoupeGesture:];
-[UITextRefinementAcceleratedTouchBehavior usesTouchAlignment];
-[UITextRefinementAcceleratedTouchBehavior loupeGestureRecognizerShouldBegin:forTextLoupeInteraction:];
-[UITextRefinementAcceleratedTouchBehavior configureGestureExclusionRequirementsForTextLoupeInteraction:];
-[UITextRefinementAcceleratedTouchBehavior shouldAllowEnforcedTouchTypeForTouch:forGestureRecognizer:];
-[UITextRefinementAcceleratedTouchBehavior triggeredByLongPressGesture:];
```
