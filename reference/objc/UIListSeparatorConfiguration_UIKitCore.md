# `UIListSeparatorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 10 properties, 36 instance methods, 6 class methods

## Instance variables

```
B _ignoreTopSeparatorInsetsFromCell;
B _ignoreBottomSeparatorInsetsFromCell;
q _topSeparatorVisibility;
q _bottomSeparatorVisibility;
@"UIColor" _color;
@"UIColor" _multipleSelectionColor;
@"UIVisualEffect" _visualEffect;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _topSeparatorInsets;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _bottomSeparatorInsets;
```

## Properties

```
@property (TB,N,G_ignoreBottomSeparatorInsetsFromCell,S_setIgnoreBottomSeparatorInsetsFromCell:,V_ignoreBottomSeparatorInsetsFromCell) _ignoreBottomSeparatorInsetsFromCell;
@property (TB,N,G_ignoreTopSeparatorInsetsFromCell,S_setIgnoreTopSeparatorInsetsFromCell:,V_ignoreTopSeparatorInsetsFromCell) _ignoreTopSeparatorInsetsFromCell;
@property (T@"UIVisualEffect",C,N,G_visualEffect,S_setVisualEffect:) _visualEffect;
@property (Tq,N,V_topSeparatorVisibility) topSeparatorVisibility;
@property (Tq,N,V_bottomSeparatorVisibility) bottomSeparatorVisibility;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_topSeparatorInsets) topSeparatorInsets;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_bottomSeparatorInsets) bottomSeparatorInsets;
@property (T@"UIColor",&,N,V_color) color;
@property (T@"UIColor",&,N,V_multipleSelectionColor) multipleSelectionColor;
@property (T@"UIVisualEffect",C,N,V_visualEffect) visualEffect;
```

## Class methods

```
+[UIListSeparatorConfiguration supportsSecureCoding];
+[UIListSeparatorConfiguration _dynamicMultiselectSeparatorColor_UICollectionLayoutListAppearanceGrouped];
+[UIListSeparatorConfiguration _dynamicMultiselectSeparatorColor_UICollectionLayoutListAppearanceInsetGrouped];
+[UIListSeparatorConfiguration _dynamicMultiselectSeparatorColor_UICollectionLayoutListAppearancePlain];
+[UIListSeparatorConfiguration _dynamicMultiselectSeparatorColor_UICollectionLayoutListAppearanceSidebar];
+[UIListSeparatorConfiguration _dynamicMultiselectSeparatorColor_UICollectionLayoutListAppearanceSidebarPlain];
```

## Instance methods

```
-[UIListSeparatorConfiguration _color];
-[UIListSeparatorConfiguration _insets];
-[UIListSeparatorConfiguration _setColor:];
-[UIListSeparatorConfiguration _replaceAutomaticValuesWithValuesFromConfiguration:];
-[UIListSeparatorConfiguration setColor:];
-[UIListSeparatorConfiguration _ignoreBottomSeparatorInsetsFromCell];
-[UIListSeparatorConfiguration setMultipleSelectionColor:];
-[UIListSeparatorConfiguration _setInsets:];
-[UIListSeparatorConfiguration setTopSeparatorInsets:];
-[UIListSeparatorConfiguration topSeparatorInsets];
-[UIListSeparatorConfiguration _setMultipleSelectionColor:];
-[UIListSeparatorConfiguration visualEffect];
-[UIListSeparatorConfiguration initWithListAppearance:];
-[UIListSeparatorConfiguration __copyWithSubclass:inZone:];
-[UIListSeparatorConfiguration setTopSeparatorVisibility:];
-[UIListSeparatorConfiguration topSeparatorVisibility];
-[UIListSeparatorConfiguration _setVisualEffect:];
-[UIListSeparatorConfiguration _multiselectSeparatorColorForListAppearance:];
-[UIListSeparatorConfiguration color];
-[UIListSeparatorConfiguration _ignoreTopSeparatorInsetsFromCell];
-[UIListSeparatorConfiguration bottomSeparatorVisibility];
-[UIListSeparatorConfiguration multipleSelectionColor];
-[UIListSeparatorConfiguration _setIgnoreBottomSeparatorInsetsFromCell:];
-[UIListSeparatorConfiguration encodeWithCoder:];
-[UIListSeparatorConfiguration hash];
-[UIListSeparatorConfiguration _setIgnoreTopSeparatorInsetsFromCell:];
-[UIListSeparatorConfiguration description];
-[UIListSeparatorConfiguration initWithCoder:];
-[UIListSeparatorConfiguration bottomSeparatorInsets];
-[UIListSeparatorConfiguration copyWithZone:];
-[UIListSeparatorConfiguration isEqual:];
-[UIListSeparatorConfiguration setBottomSeparatorInsets:];
-[UIListSeparatorConfiguration _multipleSelectionColor];
-[UIListSeparatorConfiguration setBottomSeparatorVisibility:];
-[UIListSeparatorConfiguration setVisualEffect:];
-[UIListSeparatorConfiguration _visualEffect];
```
