# `UITextMultiTapRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `UITapRecognizerDelegate`
- 8 instance variables, 15 properties, 33 instance methods, 0 class methods

## Instance variables

```
@ _target;
: _tapAction;
@"UITapRecognizer" _tapRecognizer;
Q _tapCount;
Q _touchDownCount;
B _sendTapAction;
B _recognizesOnSubsequentTouchDowns;
q _requiredButtonMask;
```

## Properties

```
@property (TQ,R) tapCount;
@property (TQ) numberOfTouchesRequired;
@property (TQ) minimumNumberOfTapsRequired;
@property (Td) maximumTouchDownDuration;
@property (Td) maximumIntervalBetweenTaps;
@property (Td) allowableMovement;
@property (TB,V_recognizesOnSubsequentTouchDowns) recognizesOnSubsequentTouchDowns;
@property (Tq,V_requiredButtonMask) requiredButtonMask;
@property (T@"NSArray",R) touchesForTap;
@property (T{CGPoint=dd},R) location;
@property (T@"UIView",R,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextMultiTapRecognizer allowableMovement];
-[UITextMultiTapRecognizer canPreventGestureRecognizer:];
-[UITextMultiTapRecognizer touchesEnded:withEvent:];
-[UITextMultiTapRecognizer _shouldReceiveTouch:withEvent:];
-[UITextMultiTapRecognizer touchesForTap];
-[UITextMultiTapRecognizer touchesCancelled:withEvent:];
-[UITextMultiTapRecognizer maximumTouchDownDuration];
-[UITextMultiTapRecognizer _allowsEventWithRequiredButtonMask:];
-[UITextMultiTapRecognizer setAllowableMovement:];
-[UITextMultiTapRecognizer location];
-[UITextMultiTapRecognizer resetTapCountForTapRecognizer:];
-[UITextMultiTapRecognizer onStateUpdate:];
-[UITextMultiTapRecognizer reset];
-[UITextMultiTapRecognizer setMinimumNumberOfTapsRequired:];
-[UITextMultiTapRecognizer touchesBegan:withEvent:];
-[UITextMultiTapRecognizer touchesMoved:withEvent:];
-[UITextMultiTapRecognizer locationInView:];
-[UITextMultiTapRecognizer recognizesOnSubsequentTouchDowns];
-[UITextMultiTapRecognizer setNumberOfTouchesRequired:];
-[UITextMultiTapRecognizer tapIsPossibleForTapRecognizer:];
-[UITextMultiTapRecognizer _touchSloppinessFactor];
-[UITextMultiTapRecognizer setRecognizesOnSubsequentTouchDowns:];
-[UITextMultiTapRecognizer initWithTarget:tapAction:];
-[UITextMultiTapRecognizer minimumNumberOfTapsRequired];
-[UITextMultiTapRecognizer tapRecognizerFailedToRecognizeTap:];
-[UITextMultiTapRecognizer maximumIntervalBetweenTaps];
-[UITextMultiTapRecognizer numberOfTouchesRequired];
-[UITextMultiTapRecognizer setMaximumIntervalBetweenTaps:];
-[UITextMultiTapRecognizer setMaximumTouchDownDuration:];
-[UITextMultiTapRecognizer requiredButtonMask];
-[UITextMultiTapRecognizer tapCount];
-[UITextMultiTapRecognizer setRequiredButtonMask:];
-[UITextMultiTapRecognizer tapRecognizerRecognizedTap:];
```
