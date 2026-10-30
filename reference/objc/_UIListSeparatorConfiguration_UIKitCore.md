# `_UIListSeparatorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIListSeparatorConfiguration`
- 4 instance variables, 7 properties, 18 instance methods, 2 class methods

## Instance variables

```
B _adjustColorForMultipleSelection;
q _hidingBehavior;
q _insetAdjustmentBehavior;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _insetsForBoundarySeparators;
```

## Properties

```
@property (T{NSDirectionalEdgeInsets=dddd},N,G_insets,S_setInsets:) _insets;
@property (T{NSDirectionalEdgeInsets=dddd},N,G_insetsForBoundarySeparators,S_setInsetsForBoundarySeparators:,V_insetsForBoundarySeparators) _insetsForBoundarySeparators;
@property (T@"UIColor",&,N,G_color,S_setColor:) _color;
@property (T@"UIColor",&,N,G_multipleSelectionColor,S_setMultipleSelectionColor:) _multipleSelectionColor;
@property (TB,N,G_shouldAdjustColorForMultipleSelection,S_setAdjustColorForMultipleSelection:,V_adjustColorForMultipleSelection) _adjustColorForMultipleSelection;
@property (Tq,N,G_hidingBehavior,S_setHidingBehavior:,V_hidingBehavior) _hidingBehavior;
@property (Tq,N,G_insetAdjustmentBehaviour,S_setInsetAdjustmentBehavior:,V_insetAdjustmentBehavior) _insetAdjustmentBehavior;
```

## Class methods

```
+[_UIListSeparatorConfiguration supportsSecureCoding];
+[_UIListSeparatorConfiguration _configurationForAppearanceStyle:inLayoutEnvironment:];
```

## Instance methods

```
-[_UIListSeparatorConfiguration _color];
-[_UIListSeparatorConfiguration _insets];
-[_UIListSeparatorConfiguration _setColor:];
-[_UIListSeparatorConfiguration _setInsets:];
-[_UIListSeparatorConfiguration _setInsetAdjustmentBehavior:];
-[_UIListSeparatorConfiguration _setMultipleSelectionColor:];
-[_UIListSeparatorConfiguration _shouldAdjustColorForMultipleSelection];
-[_UIListSeparatorConfiguration _hidingBehavior];
-[_UIListSeparatorConfiguration encodeWithCoder:];
-[_UIListSeparatorConfiguration _insetAdjustmentBehaviour];
-[_UIListSeparatorConfiguration _setHidingBehavior:];
-[_UIListSeparatorConfiguration _setInsetsForBoundarySeparators:];
-[_UIListSeparatorConfiguration initWithCoder:];
-[_UIListSeparatorConfiguration copyWithZone:];
-[_UIListSeparatorConfiguration _insetsForBoundarySeparators];
-[_UIListSeparatorConfiguration isEqual:];
-[_UIListSeparatorConfiguration _multipleSelectionColor];
-[_UIListSeparatorConfiguration _setAdjustColorForMultipleSelection:];
```
