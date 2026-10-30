# `SBChronoHomeScreenUsageObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHHomeScreenUsageMonitorObserver`
- 6 instance variables, 6 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"NSMutableOrderedSet" _registeredIconManagers;
@"NSMapTable" _appearanceChangeRegistrations;
@"NSMapTable" _appearanceChangeObservedViewControllers;
@"NSMapTable" _pendingInterfaceOrientations;
@"CHSWidgetHost" _widgetHost;
Q _widgetDataGeneration;
```

## Properties

```
@property (T@"CHSWidgetHost",R,N,V_widgetHost) widgetHost;
@property (TQ,N,V_widgetDataGeneration) widgetDataGeneration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBChronoHomeScreenUsageObserver init];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserTappedWidgetIcon:withURL:];
-[SBChronoHomeScreenUsageObserver dealloc];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserDislikedWidgetIconStackSuggestion:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserDislikedSiriSuggestionOnWidgetIconStackSuggestion:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteUserAddedWidgetIconStackSuggestion:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteWidgetIconStackChangedActiveWidget:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteCurrentPageIndexChanged:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteWidgetIconAdded:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregator:didNoteWidgetIconRemoved:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregatorAddWidgetSheetWillPresent:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregatorDidNoteEditingModeEnded:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregatorDidNoteEditingModeEntered:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregatorDidNoteIconStylePickerDidDismiss:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregatorDidNoteInterfaceOrientationChanged:];
-[SBChronoHomeScreenUsageObserver homeScreenUsageAggregatorDidNoteListLayoutProviderChanged:];
-[SBChronoHomeScreenUsageObserver addIconManager:];
-[SBChronoHomeScreenUsageObserver _combinedMetricsSpecificationForPrimaryIconManager:];
-[SBChronoHomeScreenUsageObserver _containerDescriptorForWidgetIcon:iconManager:atLocation:page:];
-[SBChronoHomeScreenUsageObserver _descriptionForArray:name:];
-[SBChronoHomeScreenUsageObserver _effectiveInterfaceOrientationForIconManager:];
-[SBChronoHomeScreenUsageObserver _rebuildAndTransmitConfiguredWidgetData];
-[SBChronoHomeScreenUsageObserver _setRegisteredIconManagersForTesting:];
-[SBChronoHomeScreenUsageObserver _startObservingAppearanceChangesForIconManager:];
-[SBChronoHomeScreenUsageObserver _stopObservingAppearanceChangesForIconManager:];
-[SBChronoHomeScreenUsageObserver _supportedFamiliesForIconManager:];
-[SBChronoHomeScreenUsageObserver _systemDefaultMetricsSpecificationForIconManager:families:];
-[SBChronoHomeScreenUsageObserver noteIconManager:willTransitionToInterfaceOrientation:];
-[SBChronoHomeScreenUsageObserver noteIconManagerDidFinishInterfaceOrientationTransition:];
-[SBChronoHomeScreenUsageObserver removeIconManager:];
-[SBChronoHomeScreenUsageObserver rootViewControllerDidChange:];
-[SBChronoHomeScreenUsageObserver setWidgetDataGeneration:];
-[SBChronoHomeScreenUsageObserver widgetDataGeneration];
-[SBChronoHomeScreenUsageObserver widgetHost];
```
