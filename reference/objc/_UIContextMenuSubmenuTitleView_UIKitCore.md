# `_UIContextMenuSubmenuTitleView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionReusableView`
- 7 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _highlighted;
B _allowsFocus;
@"_UIContextMenuCellContentView" _contentView;
@"UIVisualEffectView" _obscuringMaterialView;
@"UIView" _bgView;
@"UIView" _highlightedBgView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _backgroundShapeInsets;
```

## Properties

```
@property (T@"UIView",&,N,V_bgView) bgView;
@property (T@"UIVisualEffectView",&,N,V_obscuringMaterialView) obscuringMaterialView;
@property (T@"UIView",&,N,V_highlightedBgView) highlightedBgView;
@property (T{UIEdgeInsets=dddd},N,V_backgroundShapeInsets) backgroundShapeInsets;
@property (T@"_UIContextMenuCellContentView",R,N,V_contentView) contentView;
@property (TB,N,V_highlighted) highlighted;
@property (TB,N,V_allowsFocus) allowsFocus;
```

## Instance methods

```
-[_UIContextMenuSubmenuTitleView allowsFocus];
-[_UIContextMenuSubmenuTitleView setDirectionalLayoutMargins:];
-[_UIContextMenuSubmenuTitleView _platformMetrics];
-[_UIContextMenuSubmenuTitleView didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIContextMenuSubmenuTitleView highlighted];
-[_UIContextMenuSubmenuTitleView canBecomeFocused];
-[_UIContextMenuSubmenuTitleView setAllowsFocus:];
-[_UIContextMenuSubmenuTitleView setHighlighted:];
-[_UIContextMenuSubmenuTitleView focusItemDeferralMode];
-[_UIContextMenuSubmenuTitleView contentView];
-[_UIContextMenuSubmenuTitleView _wantsKeyCommandsWhenDeferred];
-[_UIContextMenuSubmenuTitleView initWithFrame:];
-[_UIContextMenuSubmenuTitleView setBackgroundMaterialGroupName:];
-[_UIContextMenuSubmenuTitleView addObscuringMaterialViewWithGroupName:];
-[_UIContextMenuSubmenuTitleView backgroundShapeInsets];
-[_UIContextMenuSubmenuTitleView bgView];
-[_UIContextMenuSubmenuTitleView highlightedBgView];
-[_UIContextMenuSubmenuTitleView obscuringMaterialView];
-[_UIContextMenuSubmenuTitleView setBackgroundShapeInsets:];
-[_UIContextMenuSubmenuTitleView setBgView:];
-[_UIContextMenuSubmenuTitleView setHighlightedBgView:];
-[_UIContextMenuSubmenuTitleView setObscuringMaterialView:];
```
