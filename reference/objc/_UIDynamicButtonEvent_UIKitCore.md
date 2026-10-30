# `_UIDynamicButtonEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- Protocols: `_UIEventComponentContaining`, `BSDebugDescriptionProviding`, `BSDescriptionStreamable`
- 3 instance variables, 5 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _dynamicButtonsByWindow;
@"NSMapTable" _deliveryTableByDynamicButton;
@"_UIDynamicButton" _dynamicButtonForDispatch;
```

## Properties

```
@property (T@"NSSet",R,C,N) _allDynamicButtons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDynamicButtonEvent _allWindows];
-[_UIDynamicButtonEvent _cleanupAfterDispatch];
-[_UIDynamicButtonEvent _setHIDEvent:];
-[_UIDynamicButtonEvent _removeComponents:];
-[_UIDynamicButtonEvent _removeGestureRecognizer:fromComponents:];
-[_UIDynamicButtonEvent _gestureRecognizersForWindow:];
-[_UIDynamicButtonEvent subtype];
-[_UIDynamicButtonEvent _cloneEvent];
-[_UIDynamicButtonEvent debugDescription];
-[_UIDynamicButtonEvent _sendEventToGestureRecognizer:];
-[_UIDynamicButtonEvent succinctDescriptionBuilder];
-[_UIDynamicButtonEvent _windowDidBecomeHidden:];
-[_UIDynamicButtonEvent init];
-[_UIDynamicButtonEvent appendDescriptionToFormatter:];
-[_UIDynamicButtonEvent dealloc];
-[_UIDynamicButtonEvent _cancelComponents:];
-[_UIDynamicButtonEvent descriptionWithMultilinePrefix:];
-[_UIDynamicButtonEvent _init];
-[_UIDynamicButtonEvent succinctDescription];
-[_UIDynamicButtonEvent _allDynamicButtons];
-[_UIDynamicButtonEvent _windowDidDetachContext:];
-[_UIDynamicButtonEvent debugDescriptionWithMultilinePrefix:];
-[_UIDynamicButtonEvent type];
-[_UIDynamicButtonEvent _componentsForGestureRecognizer:];
-[_UIDynamicButtonEvent description];
-[_UIDynamicButtonEvent _dispatchWindows];
-[_UIDynamicButtonEvent _gestureRecognizerNoLongerNeedsSendEvent:];
-[_UIDynamicButtonEvent _componentsForWindow:];
-[_UIDynamicButtonEvent descriptionBuilderWithMultilinePrefix:];
```
