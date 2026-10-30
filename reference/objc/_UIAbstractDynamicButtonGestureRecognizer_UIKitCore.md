# `_UIAbstractDynamicButtonGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIDynamicButtonEventRespondable`
- 1 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _allowedPhysicalButtons;
```

## Properties

```
@property (TQ,N,S_setAllowedPhysicalButtons:,V_allowedPhysicalButtons) _allowedPhysicalButtons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIAbstractDynamicButtonGestureRecognizer canPreventGestureRecognizer:];
-[_UIAbstractDynamicButtonGestureRecognizer setCancelsTouchesInView:];
-[_UIAbstractDynamicButtonGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIAbstractDynamicButtonGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIAbstractDynamicButtonGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIAbstractDynamicButtonGestureRecognizer _shouldReceiveDynamicButton:];
-[_UIAbstractDynamicButtonGestureRecognizer _dynamicButtonsCancelled:withEvent:];
-[_UIAbstractDynamicButtonGestureRecognizer setDelaysTouchesEnded:];
-[_UIAbstractDynamicButtonGestureRecognizer initWithTarget:action:];
-[_UIAbstractDynamicButtonGestureRecognizer _shouldReceiveEvent:];
-[_UIAbstractDynamicButtonGestureRecognizer _dynamicButtonsEnded:withEvent:];
-[_UIAbstractDynamicButtonGestureRecognizer _dynamicButtonsBegan:withEvent:];
-[_UIAbstractDynamicButtonGestureRecognizer setDelaysTouchesBegan:];
-[_UIAbstractDynamicButtonGestureRecognizer _dynamicButtonsChanged:withEvent:];
-[_UIAbstractDynamicButtonGestureRecognizer _allowedPhysicalButtons];
-[_UIAbstractDynamicButtonGestureRecognizer _setAllowedPhysicalButtons:];
```
