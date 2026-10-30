# `SBFluidSwitcherItemContainerHeaderView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`
- 26 instance variables, 9 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _itemsToIconImageViews;
@"NSMutableArray" _iconImageViewReusePool;
@"NSMutableDictionary" _itemsToTitleLabels;
@"NSMutableArray" _titleLabelReusePool;
@"NSMutableDictionary" _itemsToSubtitleLabelViews;
@"NSMutableArray" _subtitleLabelReusePool;
@"NSMutableDictionary" _itemsToMultiWindowIndicatorViews;
@"NSMutableArray" _multiWindowIndicatorViewReusePool;
q _subtitleVisualStylingInterfaceStyle;
@"MTVisualStyling" _subtitleVisualStyling;
d _spacingBetweenLeadingEdgeAndIcon;
d _spacingBetweenTrailingEdgeAndLabels;
d _iconSideLength;
d _spacingBetweenSnapshotAndIcon;
d _spacingBetweenSnapshotAndLabelBaseline;
d _spacingBetweenTitleAndSubtitleBaseline;
d _spacingBetweenIconAndLabel;
d _spacingBetweenLabelAndMultipleWindowsIndicator;
d _multipleWindowsIndicatorSideLength;
d _spacingBetweenLabelAndSecondIcon;
d _spacingBetweenBoundsCenterAndSecondIcon;
@"UITapGestureRecognizer" _tapGestureRecognizer;
B _trailingIconOpacityMatchesTextOpacity;
@"<SBFluidSwitcherItemContainerHeaderViewDelegate>" _delegate;
d _textAlpha;
@"NSArray" _titleItems;
```

## Properties

```
@property (T@"<SBFluidSwitcherItemContainerHeaderViewDelegate>",R,W,N,V_delegate) delegate;
@property (Td,R,N) preferredHeaderHeight;
@property (Td,N,V_textAlpha) textAlpha;
@property (TB,N,V_trailingIconOpacityMatchesTextOpacity) trailingIconOpacityMatchesTextOpacity;
@property (T@"NSArray",C,N,V_titleItems) titleItems;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFluidSwitcherItemContainerHeaderView distanceFromBoundingLeadingEdgeToIconTrailingEdge];
```

## Instance methods

```
-[SBFluidSwitcherItemContainerHeaderView _applyPrototypeSettings];
-[SBFluidSwitcherItemContainerHeaderView setTitleItems:];
-[SBFluidSwitcherItemContainerHeaderView _titleLabelFont];
-[SBFluidSwitcherItemContainerHeaderView setTitleItems:animated:];
-[SBFluidSwitcherItemContainerHeaderView titleItems];
-[SBFluidSwitcherItemContainerHeaderView _makeMultipleWindowsIndicatorView];
-[SBFluidSwitcherItemContainerHeaderView dealloc];
-[SBFluidSwitcherItemContainerHeaderView _updateVisualStylingWithTitleItems:];
-[SBFluidSwitcherItemContainerHeaderView preferredHeaderHeight];
-[SBFluidSwitcherItemContainerHeaderView layoutSubviews];
-[SBFluidSwitcherItemContainerHeaderView settings:changedValueForKey:];
-[SBFluidSwitcherItemContainerHeaderView _multiWindowIndicatorAccessibilityIdentifierForDisplayItem:];
-[SBFluidSwitcherItemContainerHeaderView _updateTitleAlpha];
-[SBFluidSwitcherItemContainerHeaderView trailingIconOpacityMatchesTextOpacity];
-[SBFluidSwitcherItemContainerHeaderView _handleTapGestureRecognizer:];
-[SBFluidSwitcherItemContainerHeaderView _contentSizeCategoryDidChangeNotification:];
-[SBFluidSwitcherItemContainerHeaderView delegate];
-[SBFluidSwitcherItemContainerHeaderView setTextAlpha:];
-[SBFluidSwitcherItemContainerHeaderView _subtitleLabelFont];
-[SBFluidSwitcherItemContainerHeaderView setTrailingIconOpacityMatchesTextOpacity:];
-[SBFluidSwitcherItemContainerHeaderView _labelLayoutMetricsForItem:];
-[SBFluidSwitcherItemContainerHeaderView initWithFrame:delegate:];
-[SBFluidSwitcherItemContainerHeaderView textAlpha];
```
