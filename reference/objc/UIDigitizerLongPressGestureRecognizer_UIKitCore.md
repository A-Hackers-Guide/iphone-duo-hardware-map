# `UIDigitizerLongPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIDigitizerGestureRecognizerImpDelegate`
- 1 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"_UIDigitizerGestureRecognizerImp" _imp;
```

## Properties

```
@property (Td,N) minimumPressDuration;
@property (T{CGPoint=dd},R,N) digitizerLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDigitizerLongPressGestureRecognizer touchesEnded:withEvent:];
-[UIDigitizerLongPressGestureRecognizer setAllowedTouchTypes:];
-[UIDigitizerLongPressGestureRecognizer touchesCancelled:withEvent:];
-[UIDigitizerLongPressGestureRecognizer setAllowedPressTypes:];
-[UIDigitizerLongPressGestureRecognizer pressesCancelled:withEvent:];
-[UIDigitizerLongPressGestureRecognizer pressesEnded:withEvent:];
-[UIDigitizerLongPressGestureRecognizer reset];
-[UIDigitizerLongPressGestureRecognizer touchesBegan:withEvent:];
-[UIDigitizerLongPressGestureRecognizer touchesMoved:withEvent:];
-[UIDigitizerLongPressGestureRecognizer initWithTarget:action:];
-[UIDigitizerLongPressGestureRecognizer pressesBegan:withEvent:];
-[UIDigitizerLongPressGestureRecognizer pressesChanged:withEvent:];
-[UIDigitizerLongPressGestureRecognizer minimumPressDuration];
-[UIDigitizerLongPressGestureRecognizer setMinimumPressDuration:];
-[UIDigitizerLongPressGestureRecognizer digitizerLocation];
-[UIDigitizerLongPressGestureRecognizer pressesEndedSuccessfully:];
-[UIDigitizerLongPressGestureRecognizer pressesHeldForMinimum:];
-[UIDigitizerLongPressGestureRecognizer pressesHeldOverMaximum:];
-[UIDigitizerLongPressGestureRecognizer pressesNotHeldLongEnough:];
-[UIDigitizerLongPressGestureRecognizer touchesBeganSuccessfully:];
```
