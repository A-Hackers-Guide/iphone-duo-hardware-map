# `_UIFocusItemUIKitMetadata`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
{?="hasResolvedFocusTouchSensitivityStyle"b1"hasResolvedFocusMovementFlippedHorizontally"b1"hasResolvedSafeItemSize"b1} _flags;
B _focusMovementFlippedHorizontally;
q _focusTouchSensitivityStyle;
q _inheritedFocusMovementStyle;
@"<UIFocusItem>" _item;
```

## Properties

```
@property (T@"<UIFocusItem>",R,N,V_item) item;
@property (Tq,R,N,V_focusTouchSensitivityStyle) focusTouchSensitivityStyle;
@property (TB,R,N,GisFocusMovementFlippedHorizontally,V_focusMovementFlippedHorizontally) focusMovementFlippedHorizontally;
@property (Tq,R,N,V_inheritedFocusMovementStyle) inheritedFocusMovementStyle;
```

## Instance methods

```
-[_UIFocusItemUIKitMetadata item];
-[_UIFocusItemUIKitMetadata initWithItem:];
-[_UIFocusItemUIKitMetadata focusTouchSensitivityStyle];
-[_UIFocusItemUIKitMetadata inheritedFocusMovementStyle];
-[_UIFocusItemUIKitMetadata isFocusMovementFlippedHorizontally];
-[_UIFocusItemUIKitMetadata itemSizeInCoordinateSpace:];
```
