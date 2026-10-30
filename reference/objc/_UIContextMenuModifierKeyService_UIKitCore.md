# `_UIContextMenuModifierKeyService`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIKeyboardEventModifierListenerDelegate`
- 2 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
modifierKeyListener;
observations;
```

## Properties

```
@property (Tq,N,R) currentModifierFlags;
```

## Class methods

```
+[_UIContextMenuModifierKeyService sharedService];
```

## Instance methods

```
-[_UIContextMenuModifierKeyService removeObserver:];
-[_UIContextMenuModifierKeyService init];
-[_UIContextMenuModifierKeyService dealloc];
-[_UIContextMenuModifierKeyService modifierListener:didUpdateModifierFlag:];
-[_UIContextMenuModifierKeyService addObserver:];
-[_UIContextMenuModifierKeyService currentModifierFlags];
-[_UIContextMenuModifierKeyService modifierListenerDidPressNonModifierKey:];
-[_UIContextMenuModifierKeyService handleKeyboardEvent:];
-[_UIContextMenuModifierKeyService applicationWillResignActiveWithNotification:];
```
