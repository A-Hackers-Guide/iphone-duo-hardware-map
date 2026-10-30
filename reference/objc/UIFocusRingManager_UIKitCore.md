# `UIFocusRingManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIGeometryChangeObserver`
- 1 instance variables, 1 properties, 16 instance methods, 11 class methods

## Instance variables

```
@"NSMutableDictionary" _focusRingStateForClient;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_focusRingStateForClient) focusRingStateForClient;
```

## Class methods

```
+[UIFocusRingManager manager];
+[UIFocusRingManager _currentFocusItemForClient:];
+[UIFocusRingManager _removeActiveFocusLayers];
+[UIFocusRingManager _updateActiveFocusLayers];
+[UIFocusRingManager moveRingToFocusItem:];
+[UIFocusRingManager moveRingToFocusItem:forClient:];
+[UIFocusRingManager removeRingFromFocusItem:];
+[UIFocusRingManager removeRingFromFocusItem:forClient:];
+[UIFocusRingManager shapeLayerClassForItem:client:];
+[UIFocusRingManager updateRingForFocusItem:];
+[UIFocusRingManager updateRingForFocusItem:forClient:];
```

## Instance methods

```
-[UIFocusRingManager addSelectedFocusRingForItem:forClient:];
-[UIFocusRingManager _focusRingPathForItem:inView:];
-[UIFocusRingManager _updateFocusLayerFrames];
-[UIFocusRingManager setFocusRingStateForClient:];
-[UIFocusRingManager addSelectedParentFocusRingForItem:forClient:];
-[UIFocusRingManager _geometryChanged:forAncestor:];
-[UIFocusRingManager activeFocusLayersForClient:];
-[UIFocusRingManager focusRingStateForClient];
-[UIFocusRingManager _addFocusLayer:toView:forItem:];
-[UIFocusRingManager _removeActiveFocusLayersForClient:];
-[UIFocusRingManager addParentFocusRingForItem:forClient:];
-[UIFocusRingManager description];
-[UIFocusRingManager _viewToAddFocusLayerForItem:forClient:];
-[UIFocusRingManager activeFocusLayersToItemsForClient:];
-[UIFocusRingManager addFocusRingForItem:forClient:];
-[UIFocusRingManager _focusItemWantsFocusRing:forClient:];
```
