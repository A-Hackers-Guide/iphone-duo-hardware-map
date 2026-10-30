# `_UIContextMenuPinnedFooterView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 7 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"_UIContextMenuCellContentView" itemView;
@"UIView" separator;
@"NSLayoutConstraint" separatorTopConstraint;
@"NSLayoutConstraint" separatorBottomConstraint;
{UIEdgeInsets=dddd} backgroundShapeInsets;
@"UIMenuElement<UIMenuLeaf>" menuElement;
B pinnedToTop;
```

## Properties

```
@property (T@"_UIContextMenuCellContentView",N,R,VitemView) itemView;
@property (T@"UIView",N,R,Vseparator) separator;
@property (T@"NSLayoutConstraint",N,&,VseparatorTopConstraint) separatorTopConstraint;
@property (T@"NSLayoutConstraint",N,&,VseparatorBottomConstraint) separatorBottomConstraint;
@property (T{UIEdgeInsets=dddd},N,VbackgroundShapeInsets) backgroundShapeInsets;
@property (T@"UIMenuElement<UIMenuLeaf>",N,&,VmenuElement) menuElement;
@property (TB,N,VpinnedToTop) pinnedToTop;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (TB,N) highlighted;
@property (T@"_UIContextMenuPlatformMetrics",N,R) platformMetrics;
```

## Instance methods

```
-[_UIContextMenuPinnedFooterView separator];
-[_UIContextMenuPinnedFooterView directionalLayoutMargins];
-[_UIContextMenuPinnedFooterView setDirectionalLayoutMargins:];
-[_UIContextMenuPinnedFooterView isHighlighted];
-[_UIContextMenuPinnedFooterView updateContent];
-[_UIContextMenuPinnedFooterView setHighlighted:];
-[_UIContextMenuPinnedFooterView initWithCoder:];
-[_UIContextMenuPinnedFooterView initWithFrame:];
-[_UIContextMenuPinnedFooterView menuElement];
-[_UIContextMenuPinnedFooterView platformMetrics];
-[_UIContextMenuPinnedFooterView setMenuElement:];
-[_UIContextMenuPinnedFooterView setPinnedToTop:];
-[_UIContextMenuPinnedFooterView backgroundShapeInsets];
-[_UIContextMenuPinnedFooterView itemView];
-[_UIContextMenuPinnedFooterView pinnedToTop];
-[_UIContextMenuPinnedFooterView separatorBottomConstraint];
-[_UIContextMenuPinnedFooterView separatorTopConstraint];
-[_UIContextMenuPinnedFooterView setBackgroundShapeInsets:];
-[_UIContextMenuPinnedFooterView setSeparatorBottomConstraint:];
-[_UIContextMenuPinnedFooterView setSeparatorTopConstraint:];
-[_UIContextMenuPinnedFooterView updateBackgroundView];
```
