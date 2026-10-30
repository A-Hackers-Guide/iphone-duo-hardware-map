# `_UIEditMenuListViewCell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewCell`
- 13 instance variables, 13 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"_UIEditMenuListItem" _item;
d _maximumContentWidth;
@"_UISlotView" _securePasteButtonSlotView;
@"UIStackView" _contentStackView;
@"UILabel" _titleLabel;
@"UIImageView" _imageView;
@"UIView" _customView;
@"NSArray" _contentConstraints;
@"NSLayoutConstraint" _minimumWidthConstraint;
@"NSLayoutConstraint" _maximumWidthConstraint;
@"NSLayoutConstraint" _slotViewCenterXConstraint;
@"NSLayoutConstraint" _slotViewCenterYConstraint;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _arrowEdgeInsets;
```

## Properties

```
@property (T@"UIStackView",R,N,V_contentStackView) contentStackView;
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (T@"UIImageView",R,N,V_imageView) imageView;
@property (T@"UIView",R,N,V_customView) customView;
@property (T@"NSArray",R,N,V_contentConstraints) contentConstraints;
@property (T@"NSLayoutConstraint",R,N,V_minimumWidthConstraint) minimumWidthConstraint;
@property (T@"NSLayoutConstraint",R,N,V_maximumWidthConstraint) maximumWidthConstraint;
@property (T@"NSLayoutConstraint",R,N,V_slotViewCenterXConstraint) slotViewCenterXConstraint;
@property (T@"NSLayoutConstraint",R,N,V_slotViewCenterYConstraint) slotViewCenterYConstraint;
@property (T@"_UIEditMenuListItem",&,N,V_item) item;
@property (Td,N,V_maximumContentWidth) maximumContentWidth;
@property (T{UIEdgeInsets=dddd},N,V_arrowEdgeInsets) arrowEdgeInsets;
@property (T@"_UISlotView",R,N,V_securePasteButtonSlotView) securePasteButtonSlotView;
```

## Class methods

```
+[_UIEditMenuListViewCell layoutSizeForItem:traitCollection:containerSize:];
```

## Instance methods

```
-[_UIEditMenuListViewCell customView];
-[_UIEditMenuListViewCell didMoveToWindow];
-[_UIEditMenuListViewCell _updateFont];
-[_UIEditMenuListViewCell titleLabel];
-[_UIEditMenuListViewCell setItem:];
-[_UIEditMenuListViewCell _contentSizeCategoryDidChange];
-[_UIEditMenuListViewCell _createViewHierarchy];
-[_UIEditMenuListViewCell item];
-[_UIEditMenuListViewCell setBounds:];
-[_UIEditMenuListViewCell minimumWidthConstraint];
-[_UIEditMenuListViewCell setHighlighted:];
-[_UIEditMenuListViewCell prepareForReuse];
-[_UIEditMenuListViewCell initWithCoder:];
-[_UIEditMenuListViewCell imageView];
-[_UIEditMenuListViewCell initWithFrame:];
-[_UIEditMenuListViewCell maximumWidthConstraint];
-[_UIEditMenuListViewCell _updateConstraints];
-[_UIEditMenuListViewCell arrowEdgeInsets];
-[_UIEditMenuListViewCell _hideContents];
-[_UIEditMenuListViewCell _overlaySlotView:];
-[_UIEditMenuListViewCell _secureName];
-[_UIEditMenuListViewCell _setupSlotView];
-[_UIEditMenuListViewCell _updateLayoutMargins];
-[_UIEditMenuListViewCell _wantsPasteSlotView];
-[_UIEditMenuListViewCell contentConstraints];
-[_UIEditMenuListViewCell contentStackView];
-[_UIEditMenuListViewCell maximumContentWidth];
-[_UIEditMenuListViewCell securePasteButtonSlotView];
-[_UIEditMenuListViewCell setArrowEdgeInsets:];
-[_UIEditMenuListViewCell setMaximumContentWidth:];
-[_UIEditMenuListViewCell slotViewCenterXConstraint];
-[_UIEditMenuListViewCell slotViewCenterYConstraint];
```
