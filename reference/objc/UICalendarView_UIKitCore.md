# `UICalendarView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDelegate`, `_UICalendarHeaderViewDelegate`, `_UICalendarMonthYearSelectorDelegate`, `_UIVisualStyleStylable`
- 21 instance variables, 18 properties, 101 instance methods, 1 class methods

## Instance variables

```
{?="needsCollectionViewSelectionUpdate"b1"needsCollectionViewScrollPositionUpdate"b1"needsUpdateSizing"b1"needsUpdateForChangedLayoutMargins"b1"isIgnoringScrollCallbacks"b1"implementsDecorationDelegate"b1"implementsDidChangeVisibleDateDelegate"b1"hasDecorations"b1} _flags;
@"NSDateFormatter" _cellFormatter;
@"UICollectionViewDiffableDataSource" _dataSource;
@"_UICalendarViewDataSourceController" _dataSourceController;
q _stateUpdatesInFlight;
@"_UICalendarMonthYearSelector" _monthYearSelector;
{CGSize="width"d"height"d} _lastKnownSize;
{CGPoint="x"d"y"d} _frozenContentOffset;
d _lastWeekdayLabelWidth;
d _collectionViewAspectRatio;
d _collectionViewDecorationsTotalHeight;
@"_UIDatePickerLinkedLabel" _daySizingLabel;
@"_UICalendarDataModel" _dataModel;
q _viewState;
@"<UICalendarViewDelegate>" _delegate;
@"UICalendarSelection" _selectionBehavior;
@"UIView" _contentView;
@"_UICalendarHeaderView" _headerView;
@"_UICalendarWeekdayView" _weekdayView;
@"UICollectionView" _collectionView;
@"_UICalendarViewDecorationSystem" _decorationSystem;
```

## Properties

```
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"_UICalendarHeaderView",&,N,V_headerView) headerView;
@property (T@"_UICalendarWeekdayView",&,N,V_weekdayView) weekdayView;
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"_UICalendarViewDecorationSystem",&,N,V_decorationSystem) decorationSystem;
@property (T@"<UICalendarViewDelegate>",W,N,V_delegate) delegate;
@property (T@"UICalendarSelection",&,N,V_selectionBehavior) selectionBehavior;
@property (T@"NSLocale",&,N) locale;
@property (T@"NSCalendar",C,N) calendar;
@property (T@"NSTimeZone",&,N) timeZone;
@property (T@"NSString",C,N) fontDesign;
@property (T@"NSDateInterval",C,N) availableDateRange;
@property (T@"NSDateComponents",C,N) visibleDateComponents;
@property (TB,N) wantsDateDecorations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICalendarView visualStyleRegistryIdentity];
```

## Instance methods

```
-[UICalendarView selection];
-[UICalendarView setSelection:];
-[UICalendarView setTimeZone:];
-[UICalendarView setCalendar:];
-[UICalendarView setContentView:];
-[UICalendarView headerView];
-[UICalendarView setAllowsMultipleSelection:];
-[UICalendarView _intrinsicSizeWithinSize:];
-[UICalendarView collectionView:didSelectItemAtIndexPath:];
-[UICalendarView setLocale:];
-[UICalendarView collectionView];
-[UICalendarView layoutSubviews];
-[UICalendarView layoutMarginsDidChange];
-[UICalendarView collectionView:shouldDeselectItemAtIndexPath:];
-[UICalendarView collectionView:shouldSelectItemAtIndexPath:];
-[UICalendarView collectionView:shouldHighlightItemAtIndexPath:];
-[UICalendarView calendar];
-[UICalendarView setBounds:];
-[UICalendarView timeZone];
-[UICalendarView setCollectionView:];
-[UICalendarView sizeThatFits:];
-[UICalendarView setDelegate:];
-[UICalendarView locale];
-[UICalendarView scrollViewDidEndScrollingAnimation:];
-[UICalendarView contentView];
-[UICalendarView delegate];
-[UICalendarView setFrame:];
-[UICalendarView initWithCoder:];
-[UICalendarView scrollViewDidEndDecelerating:];
-[UICalendarView collectionView:didDeselectItemAtIndexPath:];
-[UICalendarView initWithFrame:];
-[UICalendarView scrollViewDidScroll:];
-[UICalendarView setHeaderView:];
-[UICalendarView _updateCollectionViewSelection:];
-[UICalendarView setWeekdayView:];
-[UICalendarView __dayAndWeekdayLabelWidth];
-[UICalendarView _axesForDerivingIntrinsicContentSizeFromLayoutSize];
-[UICalendarView _canSelectItemAtIndexPath:forSelection:];
-[UICalendarView _cleanupDataIfNecessary];
-[UICalendarView _configuedCellForCollectionView:indexPath:day:];
-[UICalendarView _configureMonthYearSelector];
-[UICalendarView _contentSizeCategoryForContentWidth:];
-[UICalendarView _dataModel];
-[UICalendarView _delegateDecorationForDay:];
-[UICalendarView _deselectDates:animated:];
-[UICalendarView _destroyMonthYearSelector];
-[UICalendarView _freezeContentOffset];
-[UICalendarView _hasCellDecorations];
-[UICalendarView _performIfNotIgnoringScrollCallbacks:];
-[UICalendarView _performIgnoringScrollCallbacks:];
-[UICalendarView _preferredCollectionViewHeightForWidth:];
-[UICalendarView _reconfigureVisibleItems];
-[UICalendarView _reloadCollectionViewLayout];
-[UICalendarView _reloadDataSourceController];
-[UICalendarView _reloadDateFormatters];
-[UICalendarView _reloadEverythingIncludingLayout:];
-[UICalendarView _reloadPossibleDayValues];
-[UICalendarView _reloadVisibleMonthIfNeeded];
-[UICalendarView _restoreContentOffsetWithPageOffset:];
-[UICalendarView _selectDates:animated:];
-[UICalendarView _selectionRoundedEdgeForDay:];
-[UICalendarView _setNeedsCollectionViewScrollPositionUpdate];
-[UICalendarView _setNeedsCollectionViewSelectionUpdate];
-[UICalendarView _setNeedsUpdateForChangedLayoutMargins];
-[UICalendarView _setNeedsUpdateSizing];
-[UICalendarView _setVisibleMonth:];
-[UICalendarView _setVisibleMonth:animated:];
-[UICalendarView _setVisibleMonth:animated:updateDataSource:updateCollectionView:notifyDelegate:];
-[UICalendarView _setupInitialValues];
-[UICalendarView _setupViewHierarchy];
-[UICalendarView _shouldDifferentiateWithoutColorUpdated:];
-[UICalendarView _shouldUpdateDateViewForVisibleMonth:];
-[UICalendarView _updateCollectionViewContentInsets];
-[UICalendarView _updateCollectionViewScrollPosition:];
-[UICalendarView _updateContentSizeLimitations];
-[UICalendarView _updateDateViewForVisibleMonth:animated:];
-[UICalendarView _updateForChangedLayoutMargins];
-[UICalendarView _updateSizing];
-[UICalendarView _updateViewState:animated:];
-[UICalendarView _updateVisibleMonth:animated:];
-[UICalendarView _updateVisibleMonthIfNecessary];
-[UICalendarView allowsMultipleSelection];
-[UICalendarView availableDateRange];
-[UICalendarView decorationSystem];
-[UICalendarView fontDesign];
-[UICalendarView headerViewDidSelect:];
-[UICalendarView headerViewDidStepBackward:];
-[UICalendarView headerViewDidStepForward:];
-[UICalendarView monthYearSelector:didSelectMonth:];
-[UICalendarView reloadDecorationsForDateComponents:animated:];
-[UICalendarView selectionBehavior];
-[UICalendarView setAvailableDateRange:];
-[UICalendarView setDecorationSystem:];
-[UICalendarView setFontDesign:];
-[UICalendarView setSelectionBehavior:];
-[UICalendarView setVisibleDateComponents:];
-[UICalendarView setVisibleDateComponents:animated:];
-[UICalendarView setWantsDateDecorations:];
-[UICalendarView visibleDateComponents];
-[UICalendarView wantsDateDecorations];
-[UICalendarView weekdayView];
```
