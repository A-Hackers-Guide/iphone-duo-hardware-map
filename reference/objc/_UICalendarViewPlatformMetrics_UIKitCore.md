# `_UICalendarViewPlatformMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualStyleProviding`
- 33 instance variables, 33 properties, 67 instance methods, 1 class methods

## Instance variables

```
@? _maximumContentWidthForLayoutMargins;
d _minimumContentWidth;
d _minimumLayoutWidth;
d _collectionViewHeightOffset;
@? _headerViewLayoutMarginsForProposedLayoutMargins;
@? _headerViewIntrinsicLayoutMarginsForProposedLayoutMargins;
@? _headerViewInsetsForLayoutMargins;
@"UIButtonConfiguration" _headerViewDefaultButtonConfiguration;
@"UIColor" _monthYearLabelColor;
@"UIColor" _expandedMonthYearLabelColor;
@"UIColor" _monthYearChevronColor;
@"UIColor" _expandedMonthYearChevronColor;
@? _monthYearLabelFontProvider;
@? _monthYearChevronSymbolConfiguration;
@? _nextPreviousMonthButtonConfiguration;
@? _monthYearButtonConfiguration;
d _headerViewInterMonthButtonSpacing;
d _monthYearChevronSpacing;
@? _monthYearContainerViewProvider;
@"UIColor" _weekdayLabelTextColor;
d _weekdayViewMinimumHeight;
d _weekdayViewVerticalSpacing;
@"NSDictionary" _weekdayLabelOverrideAttributes;
d _dateViewCellBackgroundSize;
d _dateViewCellSpacing;
@"UIVisualEffect" _defaultCellBackgroundEffect;
@"UIVisualEffect" _highlightedCellBackgroundEffect;
@? _dateCellForegroundColorProvider;
@? _dateCellBackgroundColorProvider;
@? _dateCellFontProvider;
{UIOffset="horizontal"d"vertical"d} _monthYearContainerOffset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _monthYearContainerEdgeInsets;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _highlightedContentTransform;
```

## Properties

```
@property (T@?,C,N,V_maximumContentWidthForLayoutMargins) maximumContentWidthForLayoutMargins;
@property (Td,N,V_minimumContentWidth) minimumContentWidth;
@property (Td,N,V_minimumLayoutWidth) minimumLayoutWidth;
@property (Td,N,V_collectionViewHeightOffset) collectionViewHeightOffset;
@property (T@?,C,N,V_headerViewLayoutMarginsForProposedLayoutMargins) headerViewLayoutMarginsForProposedLayoutMargins;
@property (T@?,C,N,V_headerViewIntrinsicLayoutMarginsForProposedLayoutMargins) headerViewIntrinsicLayoutMarginsForProposedLayoutMargins;
@property (T@?,C,N,V_headerViewInsetsForLayoutMargins) headerViewInsetsForLayoutMargins;
@property (T@"UIButtonConfiguration",C,N,V_headerViewDefaultButtonConfiguration) headerViewDefaultButtonConfiguration;
@property (T@"UIColor",C,N,V_monthYearLabelColor) monthYearLabelColor;
@property (T@"UIColor",C,N,V_expandedMonthYearLabelColor) expandedMonthYearLabelColor;
@property (T@"UIColor",C,N,V_monthYearChevronColor) monthYearChevronColor;
@property (T@"UIColor",C,N,V_expandedMonthYearChevronColor) expandedMonthYearChevronColor;
@property (T@?,C,N,V_monthYearLabelFontProvider) monthYearLabelFontProvider;
@property (T@?,C,N,V_monthYearChevronSymbolConfiguration) monthYearChevronSymbolConfiguration;
@property (T@?,C,N,V_nextPreviousMonthButtonConfiguration) nextPreviousMonthButtonConfiguration;
@property (T@?,C,N,V_monthYearButtonConfiguration) monthYearButtonConfiguration;
@property (Td,N,V_headerViewInterMonthButtonSpacing) headerViewInterMonthButtonSpacing;
@property (Td,N,V_monthYearChevronSpacing) monthYearChevronSpacing;
@property (T{UIEdgeInsets=dddd},N,V_monthYearContainerEdgeInsets) monthYearContainerEdgeInsets;
@property (T@?,C,N,V_monthYearContainerViewProvider) monthYearContainerViewProvider;
@property (T@"UIColor",C,N,V_weekdayLabelTextColor) weekdayLabelTextColor;
@property (Td,N,V_weekdayViewMinimumHeight) weekdayViewMinimumHeight;
@property (Td,N,V_weekdayViewVerticalSpacing) weekdayViewVerticalSpacing;
@property (T@"NSDictionary",C,N,V_weekdayLabelOverrideAttributes) weekdayLabelOverrideAttributes;
@property (Td,N,V_dateViewCellBackgroundSize) dateViewCellBackgroundSize;
@property (Td,N,V_dateViewCellSpacing) dateViewCellSpacing;
@property (T@"UIVisualEffect",C,N,V_defaultCellBackgroundEffect) defaultCellBackgroundEffect;
@property (T@"UIVisualEffect",C,N,V_highlightedCellBackgroundEffect) highlightedCellBackgroundEffect;
@property (T{CATransform3D=dddddddddddddddd},N,V_highlightedContentTransform) highlightedContentTransform;
@property (T@?,C,N,V_dateCellForegroundColorProvider) dateCellForegroundColorProvider;
@property (T@?,C,N,V_dateCellBackgroundColorProvider) dateCellBackgroundColorProvider;
@property (T@?,C,N,V_dateCellFontProvider) dateCellFontProvider;
@property (T{UIOffset=dd},N,V_monthYearContainerOffset) monthYearContainerOffset;
```

## Class methods

```
+[_UICalendarViewPlatformMetrics _headerViewDefaultButtonConfiguration];
```

## Instance methods

```
-[_UICalendarViewPlatformMetrics init];
-[_UICalendarViewPlatformMetrics minimumLayoutWidth];
-[_UICalendarViewPlatformMetrics dateCellBackgroundColorProvider];
-[_UICalendarViewPlatformMetrics highlightedCellBackgroundEffect];
-[_UICalendarViewPlatformMetrics setDefaultCellBackgroundEffect:];
-[_UICalendarViewPlatformMetrics setExpandedMonthYearLabelColor:];
-[_UICalendarViewPlatformMetrics setHighlightedContentTransform:];
-[_UICalendarViewPlatformMetrics dateCellForegroundColorProvider];
-[_UICalendarViewPlatformMetrics collectionViewHeightOffset];
-[_UICalendarViewPlatformMetrics dateCellFontProvider];
-[_UICalendarViewPlatformMetrics dateViewCellBackgroundSize];
-[_UICalendarViewPlatformMetrics dateViewCellSpacing];
-[_UICalendarViewPlatformMetrics defaultCellBackgroundEffect];
-[_UICalendarViewPlatformMetrics expandedMonthYearChevronColor];
-[_UICalendarViewPlatformMetrics expandedMonthYearLabelColor];
-[_UICalendarViewPlatformMetrics headerViewDefaultButtonConfiguration];
-[_UICalendarViewPlatformMetrics headerViewInsetsForLayoutMargins];
-[_UICalendarViewPlatformMetrics headerViewInterMonthButtonSpacing];
-[_UICalendarViewPlatformMetrics headerViewIntrinsicLayoutMarginsForProposedLayoutMargins];
-[_UICalendarViewPlatformMetrics headerViewLayoutMarginsForProposedLayoutMargins];
-[_UICalendarViewPlatformMetrics highlightedContentTransform];
-[_UICalendarViewPlatformMetrics maximumContentWidthForLayoutMargins];
-[_UICalendarViewPlatformMetrics minimumContentWidth];
-[_UICalendarViewPlatformMetrics monthYearButtonConfiguration];
-[_UICalendarViewPlatformMetrics monthYearChevronColor];
-[_UICalendarViewPlatformMetrics monthYearChevronSpacing];
-[_UICalendarViewPlatformMetrics monthYearChevronSymbolConfiguration];
-[_UICalendarViewPlatformMetrics monthYearContainerEdgeInsets];
-[_UICalendarViewPlatformMetrics monthYearContainerOffset];
-[_UICalendarViewPlatformMetrics monthYearContainerViewProvider];
-[_UICalendarViewPlatformMetrics monthYearLabelColor];
-[_UICalendarViewPlatformMetrics monthYearLabelFontProvider];
-[_UICalendarViewPlatformMetrics nextPreviousMonthButtonConfiguration];
-[_UICalendarViewPlatformMetrics setCollectionViewHeightOffset:];
-[_UICalendarViewPlatformMetrics setDateCellBackgroundColorProvider:];
-[_UICalendarViewPlatformMetrics setDateCellFontProvider:];
-[_UICalendarViewPlatformMetrics setDateCellForegroundColorProvider:];
-[_UICalendarViewPlatformMetrics setDateViewCellBackgroundSize:];
-[_UICalendarViewPlatformMetrics setDateViewCellSpacing:];
-[_UICalendarViewPlatformMetrics setExpandedMonthYearChevronColor:];
-[_UICalendarViewPlatformMetrics setHeaderViewDefaultButtonConfiguration:];
-[_UICalendarViewPlatformMetrics setHeaderViewInsetsForLayoutMargins:];
-[_UICalendarViewPlatformMetrics setHeaderViewInterMonthButtonSpacing:];
-[_UICalendarViewPlatformMetrics setHeaderViewIntrinsicLayoutMarginsForProposedLayoutMargins:];
-[_UICalendarViewPlatformMetrics setHeaderViewLayoutMarginsForProposedLayoutMargins:];
-[_UICalendarViewPlatformMetrics setHighlightedCellBackgroundEffect:];
-[_UICalendarViewPlatformMetrics setMaximumContentWidthForLayoutMargins:];
-[_UICalendarViewPlatformMetrics setMinimumContentWidth:];
-[_UICalendarViewPlatformMetrics setMinimumLayoutWidth:];
-[_UICalendarViewPlatformMetrics setMonthYearButtonConfiguration:];
-[_UICalendarViewPlatformMetrics setMonthYearChevronColor:];
-[_UICalendarViewPlatformMetrics setMonthYearChevronSpacing:];
-[_UICalendarViewPlatformMetrics setMonthYearChevronSymbolConfiguration:];
-[_UICalendarViewPlatformMetrics setMonthYearContainerEdgeInsets:];
-[_UICalendarViewPlatformMetrics setMonthYearContainerOffset:];
-[_UICalendarViewPlatformMetrics setMonthYearContainerViewProvider:];
-[_UICalendarViewPlatformMetrics setMonthYearLabelColor:];
-[_UICalendarViewPlatformMetrics setMonthYearLabelFontProvider:];
-[_UICalendarViewPlatformMetrics setNextPreviousMonthButtonConfiguration:];
-[_UICalendarViewPlatformMetrics setWeekdayLabelOverrideAttributes:];
-[_UICalendarViewPlatformMetrics setWeekdayLabelTextColor:];
-[_UICalendarViewPlatformMetrics setWeekdayViewMinimumHeight:];
-[_UICalendarViewPlatformMetrics setWeekdayViewVerticalSpacing:];
-[_UICalendarViewPlatformMetrics weekdayLabelOverrideAttributes];
-[_UICalendarViewPlatformMetrics weekdayLabelTextColor];
-[_UICalendarViewPlatformMetrics weekdayViewMinimumHeight];
-[_UICalendarViewPlatformMetrics weekdayViewVerticalSpacing];
```
