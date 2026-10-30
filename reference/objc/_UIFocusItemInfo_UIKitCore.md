# `_UIFocusItemInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
{?="hasResolvedFocusedRegion"b1"useFallbackAncestorScroller"b1} _flags;
@"NSArray" _ancestorEnvironmentScrollableContainers;
q _inheritedFocusMovementStyle;
@"_UIFocusRegion" _focusedRegion;
@"<UIFocusItem>" _item;
```

## Properties

```
@property (Tq,R,N,V_inheritedFocusMovementStyle) inheritedFocusMovementStyle;
@property (T@"_UIFocusRegion",R,N,V_focusedRegion) focusedRegion;
@property (T@"<UIFocusItem>",R,W,N,V_item) item;
@property (T@"NSArray",R,C,N,V_ancestorEnvironmentScrollableContainers) ancestorEnvironmentScrollableContainers;
@property (TB,R,N) useFallbackAncestorScroller;
```

## Class methods

```
+[_UIFocusItemInfo infoWithItem:];
+[_UIFocusItemInfo infoWithItem:useFallbackAncestorScroller:];
```

## Instance methods

```
-[_UIFocusItemInfo shortDescription];
-[_UIFocusItemInfo item];
-[_UIFocusItemInfo description];
-[_UIFocusItemInfo copyWithZone:];
-[_UIFocusItemInfo _createFocusedRegion];
-[_UIFocusItemInfo _initWithItem:useFallbackAncestorScroller:];
-[_UIFocusItemInfo ancestorEnvironmentScrollableContainers];
-[_UIFocusItemInfo focusedRectInCoordinateSpace:];
-[_UIFocusItemInfo focusedRegion];
-[_UIFocusItemInfo inheritedFocusMovementStyle];
-[_UIFocusItemInfo invalidateFocusedRegion];
-[_UIFocusItemInfo useFallbackAncestorScroller];
```
