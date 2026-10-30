# `UITapGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `UITapRecognizerDelegate`
- 5 instance variables, 16 properties, 62 instance methods, 2 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _locationInView;
@"UITapRecognizer" _imp;
I _delaysRecognitionForGreaterTapCounts;
B _isSingleKeyPressGesture;
q _buttonType;
```

## Properties

```
@property (Tq,N,S_setButtonType:,V_buttonType) _buttonType;
@property (T{CGPoint=dd},R,N) centroid;
@property (T{CGPoint=dd},R,N) location;
@property (T@"NSArray",R,N) touches;
@property (Td,N) maximumTapDuration;
@property (TB,N) continuousTapRecognition;
@property (TQ,R,N) currentNumberOfTaps;
@property (TB,N,V_isSingleKeyPressGesture) isSingleKeyPressGesture;
@property (TQ,N) numberOfTapsRequired;
@property (TQ,N) numberOfTouchesRequired;
@property (Tq,N) buttonMaskRequired;
@property (T@"UIView",R,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITapGestureRecognizer supportsSecureCoding];
+[UITapGestureRecognizer _supportsTouchContinuation];
```

## Instance methods

```
-[UITapGestureRecognizer numberOfTapsRequired];
-[UITapGestureRecognizer allowableMovement];
-[UITapGestureRecognizer canPreventGestureRecognizer:];
-[UITapGestureRecognizer _shouldReceivePress:];
-[UITapGestureRecognizer centroid];
-[UITapGestureRecognizer touchesEnded:withEvent:];
-[UITapGestureRecognizer _resetGestureRecognizer];
-[UITapGestureRecognizer buttonMaskRequired];
-[UITapGestureRecognizer touchesCancelled:withEvent:];
-[UITapGestureRecognizer setMaximumIntervalBetweenSuccessiveTaps:];
-[UITapGestureRecognizer setAllowableMovement:];
-[UITapGestureRecognizer setContinuousTapRecognition:];
-[UITapGestureRecognizer setAllowedPressTypes:];
-[UITapGestureRecognizer setButtonMaskRequired:];
-[UITapGestureRecognizer pressesCancelled:withEvent:];
-[UITapGestureRecognizer location];
-[UITapGestureRecognizer pressesEnded:withEvent:];
-[UITapGestureRecognizer resetTapCountForTapRecognizer:];
-[UITapGestureRecognizer touches];
-[UITapGestureRecognizer _isGestureType:];
-[UITapGestureRecognizer dealloc];
-[UITapGestureRecognizer numberOfTouches];
-[UITapGestureRecognizer maximumIntervalBetweenSuccessiveTaps];
-[UITapGestureRecognizer maximumTapDuration];
-[UITapGestureRecognizer touchesBegan:withEvent:];
-[UITapGestureRecognizer touchesMoved:withEvent:];
-[UITapGestureRecognizer initWithTarget:action:];
-[UITapGestureRecognizer locationInView:];
-[UITapGestureRecognizer setNumberOfTapsRequired:];
-[UITapGestureRecognizer pressesBegan:withEvent:];
-[UITapGestureRecognizer pressesChanged:withEvent:];
-[UITapGestureRecognizer setNumberOfTouchesRequired:];
-[UITapGestureRecognizer _shouldFailInResponseToPresses:withEvent:];
-[UITapGestureRecognizer _digitizerLocation];
-[UITapGestureRecognizer tapIsPossibleForTapRecognizer:];
-[UITapGestureRecognizer _touchSloppinessFactor];
-[UITapGestureRecognizer encodeWithCoder:];
-[UITapGestureRecognizer shouldRequireFailureOfGestureRecognizer:];
-[UITapGestureRecognizer tapRecognizerFailedToRecognizeTap:];
-[UITapGestureRecognizer initWithCoder:];
-[UITapGestureRecognizer numberOfTouchesRequired];
-[UITapGestureRecognizer currentNumberOfTaps];
-[UITapGestureRecognizer _appendSubclassDescription:];
-[UITapGestureRecognizer continuousTapRecognition];
-[UITapGestureRecognizer locationOfTouch:inView:];
-[UITapGestureRecognizer setMaximumTapDuration:];
-[UITapGestureRecognizer _updateGestureTraits];
-[UITapGestureRecognizer tapRecognizerRecognizedTap:];
-[UITapGestureRecognizer _setButtonType:];
-[UITapGestureRecognizer _allowableSeparation];
-[UITapGestureRecognizer _allowableTouchTimeSeparation];
-[UITapGestureRecognizer _buttonType];
-[UITapGestureRecognizer _canHandleTouches];
-[UITapGestureRecognizer _delaysRecognitionForGreaterTapCounts];
-[UITapGestureRecognizer _finalStateForRecognitionWithNumberOfTaps:];
-[UITapGestureRecognizer _setAllowableSeparation:];
-[UITapGestureRecognizer _setAllowableTouchTimeSeparation:];
-[UITapGestureRecognizer _setDelaysRecognitionForGreaterTapCounts:];
-[UITapGestureRecognizer isSingleKeyPressGesture];
-[UITapGestureRecognizer maximumSingleTapDuration];
-[UITapGestureRecognizer setIsSingleKeyPressGesture:];
-[UITapGestureRecognizer setMaximumSingleTapDuration:];
```
