# `_UIPhysicalButtonInteractionDynamicButtonDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPhysicalButtonInteractionDriving`, `_UIGestureRecognizerDynamicButtonObserving`
- 2 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<_UIPhysicalButtonInteractionDriverReceiving>" _receiver;
@"_UIDynamicButtonNotifyingGestureRecognizer" _dynamicButtonGesture;
```

## Properties

```
@property (Tq,R,N) _driverType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPhysicalButtonInteractionDynamicButtonDriver init];
-[_UIPhysicalButtonInteractionDynamicButtonDriver _driverType];
-[_UIPhysicalButtonInteractionDynamicButtonDriver _dynamicButtonGestureRecognizer:dynamicButtonsDidUpdate:allDynamicButtons:];
-[_UIPhysicalButtonInteractionDynamicButtonDriver _installToViewIfNeeded:];
-[_UIPhysicalButtonInteractionDynamicButtonDriver _physicalButtonConfigurationsDidChange];
-[_UIPhysicalButtonInteractionDynamicButtonDriver _uninstallFromViewIfNeeded:];
-[_UIPhysicalButtonInteractionDynamicButtonDriver initWithReceiver:];
```
