# `_UIDynamicButtonNotifyingGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIAbstractDynamicButtonGestureRecognizer`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<_UIGestureRecognizerDynamicButtonObserving>" _dynamicButtonObserver;
Q _activeDynamicButtons;
@"_UIPhysicalButtonConfigurationSet" _physicalButtonConfigurations;
```

## Instance methods

```
-[_UIDynamicButtonNotifyingGestureRecognizer shouldReceiveEvent:];
-[_UIDynamicButtonNotifyingGestureRecognizer _shouldReceiveDynamicButton:];
-[_UIDynamicButtonNotifyingGestureRecognizer _dynamicButtonsCancelled:withEvent:];
-[_UIDynamicButtonNotifyingGestureRecognizer reset];
-[_UIDynamicButtonNotifyingGestureRecognizer _dynamicButtonsEnded:withEvent:];
-[_UIDynamicButtonNotifyingGestureRecognizer _dynamicButtonsBegan:withEvent:];
-[_UIDynamicButtonNotifyingGestureRecognizer _dynamicButtonsChanged:withEvent:];
```
