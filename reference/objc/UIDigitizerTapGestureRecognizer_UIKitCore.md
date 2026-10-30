# `UIDigitizerTapGestureRecognizer`

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
@property (Td,N) maximumPressDuration;
@property (T{CGPoint=dd},R,N) digitizerLocation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDigitizerTapGestureRecognizer touchesEnded:withEvent:];
-[UIDigitizerTapGestureRecognizer setAllowedTouchTypes:];
-[UIDigitizerTapGestureRecognizer touchesCancelled:withEvent:];
-[UIDigitizerTapGestureRecognizer setAllowedPressTypes:];
-[UIDigitizerTapGestureRecognizer maximumPressDuration];
-[UIDigitizerTapGestureRecognizer pressesCancelled:withEvent:];
-[UIDigitizerTapGestureRecognizer pressesEnded:withEvent:];
-[UIDigitizerTapGestureRecognizer reset];
-[UIDigitizerTapGestureRecognizer touchesBegan:withEvent:];
-[UIDigitizerTapGestureRecognizer touchesMoved:withEvent:];
-[UIDigitizerTapGestureRecognizer initWithTarget:action:];
-[UIDigitizerTapGestureRecognizer pressesBegan:withEvent:];
-[UIDigitizerTapGestureRecognizer pressesChanged:withEvent:];
-[UIDigitizerTapGestureRecognizer setMaximumPressDuration:];
-[UIDigitizerTapGestureRecognizer digitizerLocation];
-[UIDigitizerTapGestureRecognizer pressesEndedSuccessfully:];
-[UIDigitizerTapGestureRecognizer pressesHeldForMinimum:];
-[UIDigitizerTapGestureRecognizer pressesHeldOverMaximum:];
-[UIDigitizerTapGestureRecognizer pressesNotHeldLongEnough:];
-[UIDigitizerTapGestureRecognizer touchesBeganSuccessfully:];
```
