# `SBProactiveHomeScreenUsageObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHHomeScreenUsageMonitorObserver`
- 3 instance variables, 7 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"ATXHomeScreenPrediction" _currentPrediction;
@"<SBProactiveHomeScreenUsageObserverDelegate>" _delegate;
@"SBHIconManager" _iconManager;
```

## Properties

```
@property (T@"SBHIconManager",R,W,N,V_iconManager) iconManager;
@property (T@"ATXHomeScreenPrediction",&,N,V_currentPrediction) currentPrediction;
@property (T@"<SBProactiveHomeScreenUsageObserverDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBProactiveHomeScreenUsageObserver iconManager];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregatorDidStartDiscoveringWidgets:];
-[SBProactiveHomeScreenUsageObserver setCurrentPrediction:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteDataSourceDidAppear:forWidgetIcon:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteDataSourceDidDisappear:forWidgetIcon:];
-[SBProactiveHomeScreenUsageObserver logTodayViewDidAppear];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserTappedWidgetIcon:withURL:];
-[SBProactiveHomeScreenUsageObserver widgetIdentifiablesDictionaryForIconListModel:];
-[SBProactiveHomeScreenUsageObserver pushCurrentHomeScreenConfiguration];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregatorDidNoteHomeScreenLayoutChanged:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserDislikedWidgetIconStackSuggestion:];
-[SBProactiveHomeScreenUsageObserver pushCurrentTodayConfiguration];
-[SBProactiveHomeScreenUsageObserver pushCurrentDockConfiguration];
-[SBProactiveHomeScreenUsageObserver setDelegate:];
-[SBProactiveHomeScreenUsageObserver currentPrediction];
-[SBProactiveHomeScreenUsageObserver proactiveStackForWidgetIcon:atIndex:inList:gridCellInfo:];
-[SBProactiveHomeScreenUsageObserver rootFolder];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:widgetDiscoverabilityDidRejectSuggestion:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserDislikedSiriSuggestionOnWidgetIconStackSuggestion:];
-[SBProactiveHomeScreenUsageObserver pushCurrentHomeScreenPagesConfiguration];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserAddedWidgetIconStackSuggestion:];
-[SBProactiveHomeScreenUsageObserver delegate];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:widgetDiscoverabilityDidAcceptSuggestion:];
-[SBProactiveHomeScreenUsageObserver deviceLockStateDidChange:];
-[SBProactiveHomeScreenUsageObserver initWithIconManager:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteWidgetIconStackChangedActiveWidget:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteCurrentPageIndexChanged:];
-[SBProactiveHomeScreenUsageObserver logHomeScreenPageDidAppearWithPageIndex:];
-[SBProactiveHomeScreenUsageObserver proactiveWidgetForIconDataSource:ofIcon:];
-[SBProactiveHomeScreenUsageObserver iconModel];
-[SBProactiveHomeScreenUsageObserver proactiveWidgetForWidget:ofIcon:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregatorWidgetDiscoverabilityDidEnterEditingMode:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteRootControllerWillAppearWithPageIndex:];
-[SBProactiveHomeScreenUsageObserver homeScreenUsageAggregator:didNoteTodayViewAtLocation:scrolledWithIconVisibility:];
```
