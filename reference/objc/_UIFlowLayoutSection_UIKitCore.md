# `_UIFlowLayoutSection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 30 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
B _isValid;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _validRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rectToKeepValid;
@"NSMutableSet" _invalidatedIndexPaths;
B _fixedItemSize;
B _lastRowIncomplete;
@"NSMutableArray" _items;
@"NSMutableArray" _rows;
d _lineSpacing;
d _interItemSpacing;
d _headerDimension;
d _footerDimension;
@"_UIFlowLayoutInfo" _layoutInfo;
d _otherMargin;
d _beginMargin;
d _endMargin;
d _actualGap;
d _lastRowBeginMargin;
d _lastRowEndMargin;
d _lastRowActualGap;
q _itemsCount;
q _itemsByRowCount;
q _indexOfIncompleteRow;
{?="commonRowHorizontalAlignment"i"lastRowHorizontalAlignment"i"rowVerticalAlignment"i} _rowAlignmentOptions;
{CGSize="width"d"height"d} _itemSize;
{_NSRange="location"Q"length"Q} _validItemRange;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _sectionMargins;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _headerFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _footerFrame;
```

## Instance methods

```
-[_UIFlowLayoutSection init];
```
