# `PLIOReportMetricsAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 12 instance variables, 12 properties, 51 instance methods, 1 class methods

## Instance variables

```
@"PLEntryNotificationOperatorComposition" _batteryLevelChangedNotifications;
@"PLEntryNotificationOperatorComposition" _screenstateChangedNotifications;
@"PLEntryNotificationOperatorComposition" _displayOffNotification;
@"PLEntryNotificationOperatorComposition" _displayOnNotification;
@"PLNSNotificationOperatorComposition" _enhancedScreenStateChangeListener;
@"PLStateTrackingComposition" _stateTracker;
@"PLMonotonicTimer" _displayOffTimer;
@"NSMutableDictionary" _sampleChannelsSignificantBattery;
@"NSMutableDictionary" _sampleChannelsScreenState;
@"NSMutableDictionary" _sampleChannelsSnapshot;
@"NSMutableDictionary" _sampleChannelsCustom;
@"NSDate" _lastEntryDate;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryLevelChangedNotifications) batteryLevelChangedNotifications;
@property (T@"PLEntryNotificationOperatorComposition",&,V_screenstateChangedNotifications) screenstateChangedNotifications;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayOffNotification) displayOffNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayOnNotification) displayOnNotification;
@property (T@"PLNSNotificationOperatorComposition",&,V_enhancedScreenStateChangeListener) enhancedScreenStateChangeListener;
@property (T@"PLStateTrackingComposition",&,V_stateTracker) stateTracker;
@property (T@"PLMonotonicTimer",&,V_displayOffTimer) displayOffTimer;
@property (T@"NSMutableDictionary",&,N,V_sampleChannelsSignificantBattery) sampleChannelsSignificantBattery;
@property (T@"NSMutableDictionary",&,N,V_sampleChannelsScreenState) sampleChannelsScreenState;
@property (T@"NSMutableDictionary",&,N,V_sampleChannelsSnapshot) sampleChannelsSnapshot;
@property (T@"NSMutableDictionary",&,N,V_sampleChannelsCustom) sampleChannelsCustom;
@property (T@"NSDate",&,V_lastEntryDate) lastEntryDate;
```

## Class methods

```
+[PLIOReportMetricsAgent load];
```

## Instance methods

```
-[PLIOReportMetricsAgent enhancedScreenStateChangeListener];
-[PLIOReportMetricsAgent stopDisplayOffPeriodicTimer];
-[PLIOReportMetricsAgent startDisplayOffPeriodicTimer];
-[PLIOReportMetricsAgent sampleDeltaForChannelSets];
-[PLIOReportMetricsAgent setSampleChannelsScreenState:];
-[PLIOReportMetricsAgent displayOnNotification];
-[PLIOReportMetricsAgent setSampleChannelsSnapshot:];
-[PLIOReportMetricsAgent init];
-[PLIOReportMetricsAgent sampleChannelsCustom];
-[PLIOReportMetricsAgent logIOReportSnapshots:];
-[PLIOReportMetricsAgent stateTracker];
-[PLIOReportMetricsAgent sampleDeltaForChannelGroup:];
-[PLIOReportMetricsAgent skipCurrentIteration:forChannel:];
-[PLIOReportMetricsAgent initOperatorDependancies];
-[PLIOReportMetricsAgent batteryLevelChangedNotifications];
-[PLIOReportMetricsAgent buildCustomSet:];
-[PLIOReportMetricsAgent setDisplayOffTimer:];
-[PLIOReportMetricsAgent setDisplayOnNotification:];
-[PLIOReportMetricsAgent sampleChannelsSignificantBattery];
-[PLIOReportMetricsAgent logIOReportIntervals:forChannelGroup:];
-[PLIOReportMetricsAgent buildScreenStateSet:];
-[PLIOReportMetricsAgent setSampleChannelsCustom:];
-[PLIOReportMetricsAgent logDisplayOffAPWake];
-[PLIOReportMetricsAgent lastEntryDate];
-[PLIOReportMetricsAgent sampleChannelsScreenState];
-[PLIOReportMetricsAgent logScreenStateChange];
-[PLIOReportMetricsAgent displayOffTimer];
-[PLIOReportMetricsAgent logIOReportEntry:forCategory:withEntryDate:withAPWakeTime:isInterval:];
-[PLIOReportMetricsAgent buildSnapshotSet:];
-[PLIOReportMetricsAgent initGroupChecks];
-[PLIOReportMetricsAgent subscribeToChannelSets];
-[PLIOReportMetricsAgent setStateTracker:];
-[PLIOReportMetricsAgent displayOffNotification];
-[PLIOReportMetricsAgent logDisplayOffAPWakeStats];
-[PLIOReportMetricsAgent screenstateChangedNotifications];
-[PLIOReportMetricsAgent setSampleChannelsSignificantBattery:];
-[PLIOReportMetricsAgent isDynamicTable:];
-[PLIOReportMetricsAgent allowlistedChannel:];
-[PLIOReportMetricsAgent setEnhancedScreenStateChangeListener:];
-[PLIOReportMetricsAgent sampleChannelsSnapshot];
-[PLIOReportMetricsAgent logInit];
-[PLIOReportMetricsAgent log];
-[PLIOReportMetricsAgent setScreenstateChangedNotifications:];
-[PLIOReportMetricsAgent setBatteryLevelChangedNotifications:];
-[PLIOReportMetricsAgent sampleSnapshotForChannelGroup:];
-[PLIOReportMetricsAgent channelDictionaryWithChannelSet:];
-[PLIOReportMetricsAgent buildBaseSet:];
-[PLIOReportMetricsAgent setDisplayOffNotification:];
-[PLIOReportMetricsAgent setLastEntryDate:];
-[PLIOReportMetricsAgent logSBC];
-[PLIOReportMetricsAgent createCategoryString:forSubgroup:];
```
