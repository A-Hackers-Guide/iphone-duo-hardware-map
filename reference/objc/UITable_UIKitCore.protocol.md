# `UITable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIEditable`, `UITableConstantsTableProviding`
- 0 instance variables, 31 properties, 36 instance methods, 0 class methods

## Properties

```
@property (T@"UIScrollView",R,N,G_scrollView) scrollView;
@property (Tq,R,N,G_numberOfSections) numberOfSections;
@property (TB,R,N) allowsMultipleSelection;
@property (TB,R,N) allowsMultipleSelectionDuringEditing;
@property (Td,R,N) rowHeight;
@property (Td,R,N) sectionHeaderHeight;
@property (Td,R,N) sectionFooterHeight;
@property (Td,R,N) estimatedRowHeight;
@property (Td,R,N) estimatedSectionHeaderHeight;
@property (Td,R,N) estimatedSectionFooterHeight;
@property (T{UIEdgeInsets=dddd},R,N) separatorInset;
@property (TB,R,N,G_separatorInsetIsRelativeToCellEdges) separatorInsetIsRelativeToCellEdges;
@property (TB,R,N) usesVariableMargins;
@property (TB,R,N) overlapsSectionHeaderViews;
@property (Td,R,N,G_backgroundInset) backgroundInset;
@property (T{UIEdgeInsets=dddd},R,N,G_cellSafeAreaInsets) cellSafeAreaInsets;
@property (TB,R,N) cellLayoutMarginsFollowReadableWidth;
@property (TB,N,S_setHeadersHugContent:) _sectionHeadersHugContent;
@property (Td,R,N,G_topPadding) topPadding;
@property (Td,R,N,G_bottomPadding) bottomPadding;
@property (TB,R,N,G_isShowingIndex) showingIndex;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,G_indexFrame) indexFrame;
@property (Td,R,N,G_indexBarExtentFromEdge) indexBarExtentFromEdge;
@property (T{UIEdgeInsets=dddd},R,N,G_sectionContentInset) sectionContentInset;
@property (T{UIEdgeInsets=dddd},R,N,G_rawSectionContentInset) rawSectionContentInset;
@property (Td,R,N,G_sectionCornerRadius) sectionCornerRadius;
@property (TB,R,N,G_sectionContentInsetFollowsLayoutMargins) sectionContentInsetFollowsLayoutMargins;
@property (TB,R,N,G_supplementarySectionHeadersHugContent) supplementarySectionHeadersHugContent;
@property (TB,R,N,G_supplementariesFollowSectionContentInsets) supplementariesFollowSectionContentInsets;
@property (T@"UIColor",R,N,G_accessoryBaseColor) accessoryBaseColor;
@property (T@"UIColor",R,N,G_multiselectCheckmarkColor) multiselectCheckmarkColor;
```

## Instance methods

```
-[UITable _scrollView];
-[UITable estimatedSectionFooterHeight];
-[UITable separatorInset];
-[UITable estimatedRowHeight];
-[UITable sectionFooterHeight];
-[UITable sectionHeaderHeight];
-[UITable rowHeight];
-[UITable estimatedSectionHeaderHeight];
-[UITable _numberOfSections];
-[UITable _isShowingIndex];
-[UITable _accessoryBaseColor];
-[UITable _backgroundInset];
-[UITable _bottomPadding];
-[UITable _cellSafeAreaInsets];
-[UITable _headerFooterDidInvalidateIntrinsicContentSize:];
-[UITable _indexBarExtentFromEdge];
-[UITable _indexFrame];
-[UITable _multiselectCheckmarkColor];
-[UITable _numberOfRowsInSection:];
-[UITable _rawSectionContentInset];
-[UITable _sectionContentInset];
-[UITable _sectionContentInsetFollowsLayoutMargins];
-[UITable _sectionCornerRadius];
-[UITable _sectionHeadersHugContent];
-[UITable _separatorInsetIsRelativeToCellEdges];
-[UITable _setHeadersHugContent:];
-[UITable _shouldHaveFooterViewForSection:];
-[UITable _shouldHaveHeaderViewForSection:];
-[UITable _supplementariesFollowSectionContentInsets];
-[UITable _supplementarySectionHeadersHugContent];
-[UITable _topPadding];
-[UITable allowsMultipleSelection];
-[UITable allowsMultipleSelectionDuringEditing];
-[UITable cellLayoutMarginsFollowReadableWidth];
-[UITable overlapsSectionHeaderViews];
-[UITable usesVariableMargins];
```
