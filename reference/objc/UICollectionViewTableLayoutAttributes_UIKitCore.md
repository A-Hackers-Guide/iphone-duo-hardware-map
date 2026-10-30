# `UICollectionViewTableLayoutAttributes`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayoutAttributes`
- Protocols: `UICollectionViewTableSectionHeaderFooterAttributes`, `UICollectionViewTableAllRowAttributes`
- 26 instance variables, 26 properties, 54 instance methods, 2 class methods

## Instance variables

```
B _separatorInsetIsRelativeToCellEdges;
B _shouldIndentWhileEditing;
B _showsReorderControl;
B _layoutMarginsFollowReadableWidth;
B _insetsContentViewsToSafeArea;
B _drawsSeparatorAtTopOfSection;
B _drawsSeparatorAtBottomOfSection;
B _preferredAttributesCached;
B _isHeader;
B _floating;
i _sectionLocation;
q _separatorStyle;
@"UIColor" _separatorColor;
@"UIVisualEffect" _separatorEffect;
@"UIColor" _backgroundColor;
q _accessoryType;
q _editingStyle;
d _defaultLeadingCellMarginWidth;
d _defaultTrailingCellMarginWidth;
d _indexBarExtentFromEdge;
q _indentationLevel;
d _maxTitleWidth;
q _textAlignment;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _separatorInset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _backgroundInset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _margins;
```

## Properties

```
@property (TB,N,V_preferredAttributesCached) preferredAttributesCached;
@property (TB,N,V_isHeader) isHeader;
@property (Td,N,V_maxTitleWidth) maxTitleWidth;
@property (T{UIEdgeInsets=dddd},N,V_margins) margins;
@property (Tq,N,V_textAlignment) textAlignment;
@property (TB,N,V_floating) floating;
@property (T@"UIColor",C,N,V_backgroundColor) backgroundColor;
@property (Tq,N,V_separatorStyle) separatorStyle;
@property (T{UIEdgeInsets=dddd},N,V_separatorInset) separatorInset;
@property (TB,N,V_separatorInsetIsRelativeToCellEdges) separatorInsetIsRelativeToCellEdges;
@property (T@"UIColor",C,N,V_separatorColor) separatorColor;
@property (T@"UIVisualEffect",&,N,V_separatorEffect) separatorEffect;
@property (Ti,N,V_sectionLocation) sectionLocation;
@property (TB,N,V_layoutMarginsFollowReadableWidth) layoutMarginsFollowReadableWidth;
@property (TB,N,V_insetsContentViewsToSafeArea) insetsContentViewsToSafeArea;
@property (Td,N,V_defaultLeadingCellMarginWidth) defaultLeadingCellMarginWidth;
@property (Td,N,V_defaultTrailingCellMarginWidth) defaultTrailingCellMarginWidth;
@property (Td,N,V_indexBarExtentFromEdge) indexBarExtentFromEdge;
@property (T{UIEdgeInsets=dddd},N,V_backgroundInset) backgroundInset;
@property (Tq,N,V_indentationLevel) indentationLevel;
@property (TB,N,V_drawsSeparatorAtTopOfSection) drawsSeparatorAtTopOfSection;
@property (TB,N,V_drawsSeparatorAtBottomOfSection) drawsSeparatorAtBottomOfSection;
@property (Tq,N,V_accessoryType) accessoryType;
@property (Tq,N,V_editingStyle) editingStyle;
@property (TB,N,V_shouldIndentWhileEditing) shouldIndentWhileEditing;
@property (TB,N,V_showsReorderControl) showsReorderControl;
```

## Class methods

```
+[UICollectionViewTableLayoutAttributes applyValuesFromAttributes:toAttributes:valueOptions:];
+[UICollectionViewTableLayoutAttributes automaticValueOptionsForRepresentedElementCategory:];
```

## Instance methods

```
-[UICollectionViewTableLayoutAttributes separatorInset];
-[UICollectionViewTableLayoutAttributes setTextAlignment:];
-[UICollectionViewTableLayoutAttributes setFloating:];
-[UICollectionViewTableLayoutAttributes backgroundInset];
-[UICollectionViewTableLayoutAttributes setBackgroundInset:];
-[UICollectionViewTableLayoutAttributes textAlignment];
-[UICollectionViewTableLayoutAttributes setSeparatorStyle:];
-[UICollectionViewTableLayoutAttributes setSeparatorInset:];
-[UICollectionViewTableLayoutAttributes floating];
-[UICollectionViewTableLayoutAttributes setSeparatorColor:];
-[UICollectionViewTableLayoutAttributes setBackgroundColor:];
-[UICollectionViewTableLayoutAttributes separatorEffect];
-[UICollectionViewTableLayoutAttributes setSeparatorEffect:];
-[UICollectionViewTableLayoutAttributes margins];
-[UICollectionViewTableLayoutAttributes separatorColor];
-[UICollectionViewTableLayoutAttributes backgroundColor];
-[UICollectionViewTableLayoutAttributes copyWithZone:];
-[UICollectionViewTableLayoutAttributes isEqual:];
-[UICollectionViewTableLayoutAttributes separatorStyle];
-[UICollectionViewTableLayoutAttributes indentationLevel];
-[UICollectionViewTableLayoutAttributes sectionLocation];
-[UICollectionViewTableLayoutAttributes drawsSeparatorAtBottomOfSection];
-[UICollectionViewTableLayoutAttributes accessoryType];
-[UICollectionViewTableLayoutAttributes defaultLeadingCellMarginWidth];
-[UICollectionViewTableLayoutAttributes defaultTrailingCellMarginWidth];
-[UICollectionViewTableLayoutAttributes drawsSeparatorAtTopOfSection];
-[UICollectionViewTableLayoutAttributes editingStyle];
-[UICollectionViewTableLayoutAttributes indexBarExtentFromEdge];
-[UICollectionViewTableLayoutAttributes insetsContentViewsToSafeArea];
-[UICollectionViewTableLayoutAttributes isHeader];
-[UICollectionViewTableLayoutAttributes layoutMarginsFollowReadableWidth];
-[UICollectionViewTableLayoutAttributes maxTitleWidth];
-[UICollectionViewTableLayoutAttributes preferredAttributesCached];
-[UICollectionViewTableLayoutAttributes separatorInsetIsRelativeToCellEdges];
-[UICollectionViewTableLayoutAttributes setAccessoryType:];
-[UICollectionViewTableLayoutAttributes setDefaultLeadingCellMarginWidth:];
-[UICollectionViewTableLayoutAttributes setDefaultTrailingCellMarginWidth:];
-[UICollectionViewTableLayoutAttributes setDrawsSeparatorAtBottomOfSection:];
-[UICollectionViewTableLayoutAttributes setDrawsSeparatorAtTopOfSection:];
-[UICollectionViewTableLayoutAttributes setEditingStyle:];
-[UICollectionViewTableLayoutAttributes setIndentationLevel:];
-[UICollectionViewTableLayoutAttributes setIndexBarExtentFromEdge:];
-[UICollectionViewTableLayoutAttributes setInsetsContentViewsToSafeArea:];
-[UICollectionViewTableLayoutAttributes setIsHeader:];
-[UICollectionViewTableLayoutAttributes setLayoutMarginsFollowReadableWidth:];
-[UICollectionViewTableLayoutAttributes setMargins:];
-[UICollectionViewTableLayoutAttributes setMaxTitleWidth:];
-[UICollectionViewTableLayoutAttributes setPreferredAttributesCached:];
-[UICollectionViewTableLayoutAttributes setSectionLocation:];
-[UICollectionViewTableLayoutAttributes setSeparatorInsetIsRelativeToCellEdges:];
-[UICollectionViewTableLayoutAttributes setShouldIndentWhileEditing:];
-[UICollectionViewTableLayoutAttributes setShowsReorderControl:];
-[UICollectionViewTableLayoutAttributes shouldIndentWhileEditing];
-[UICollectionViewTableLayoutAttributes showsReorderControl];
```
