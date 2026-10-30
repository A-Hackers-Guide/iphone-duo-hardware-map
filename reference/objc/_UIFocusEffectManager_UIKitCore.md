# `_UIFocusEffectManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGeometryChangeObserver`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"_UIFocusHaloView" _haloView;
@"<UIFocusItem>" _focusedItem;
```

## Properties

```
@property (T@"_UIFocusHaloView",R,N,V_haloView) haloView;
@property (T@"<UIFocusItem>",W,N,V_focusedItem) focusedItem;
```

## Instance methods

```
-[_UIFocusEffectManager _geometryChanged:forAncestor:];
-[_UIFocusEffectManager haloView];
-[_UIFocusEffectManager setFocusedItem:];
-[_UIFocusEffectManager _observeFocusedItemGeometryForItem:];
-[_UIFocusEffectManager focusedItem];
-[_UIFocusEffectManager moveFocusToItem:];
```
