# `_UIButtonBarItemLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIButtonBarLayout`
- 13 instance variables, 3 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"UIBarButtonItem" _item;
@"UIView" _itemView;
@"_UITAMICAdaptorView" _itemViewWrapper;
@"NSLayoutConstraint" _requestedSize;
@"NSLayoutConstraint" _maximumAlignmentSize;
@"NSLayoutConstraint" _groupSameSize;
@"NSLayoutConstraint" _popoverGuideLeading;
@"NSLayoutConstraint" _popoverGuideTrailing;
@"NSLayoutConstraint" _popoverGuideTop;
@"NSLayoutConstraint" _popoverGuideHeight;
B _useGroupSizing;
B _suppressSpacing;
@? _itemViewGenerator;
```

## Properties

```
@property (TB,N,V_useGroupSizing) useGroupSizing;
@property (TB,N,V_suppressSpacing) suppressSpacing;
@property (T@?,C,N,V_itemViewGenerator) itemViewGenerator;
```

## Instance methods

```
-[_UIButtonBarItemLayout _configure];
-[_UIButtonBarItemLayout barButtonItem];
-[_UIButtonBarItemLayout description];
-[_UIButtonBarItemLayout _updateItemView];
-[_UIButtonBarItemLayout suppressSpacing];
-[_UIButtonBarItemLayout _addConstraintsToActivate:toDeactivate:];
-[_UIButtonBarItemLayout _addLayoutGuides:];
-[_UIButtonBarItemLayout _addLayoutViews:];
-[_UIButtonBarItemLayout _shouldBeDirty];
-[_UIButtonBarItemLayout _updateCustomView];
-[_UIButtonBarItemLayout _updateItemViewSizing];
-[_UIButtonBarItemLayout dirtyLayoutForPlainAppearanceChange:doneAppearanceChanged:];
-[_UIButtonBarItemLayout initWithLayoutMetrics:];
-[_UIButtonBarItemLayout initWithLayoutMetrics:barButtonItem:];
-[_UIButtonBarItemLayout itemViewGenerator];
-[_UIButtonBarItemLayout minimumLayoutWidthGivenMinimumSpaceWidth:];
-[_UIButtonBarItemLayout setItemViewGenerator:];
-[_UIButtonBarItemLayout setSuppressSpacing:];
-[_UIButtonBarItemLayout setUseGroupSizing:];
-[_UIButtonBarItemLayout shouldHorizontallyCenterView:];
-[_UIButtonBarItemLayout useGroupSizing];
```
