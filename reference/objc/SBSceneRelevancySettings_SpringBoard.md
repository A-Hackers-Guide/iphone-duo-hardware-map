# `SBSceneRelevancySettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 11 instance variables, 11 properties, 29 instance methods, 5 class methods

## Instance variables

```
B _preventFreezingUnoccludedScenes;
B _prefersProcessTaskSuspensionWhileSceneForegroundAndOccluded;
B _freezeFullyOccludedWindows;
B _freezeAllWindowsBelowMaximizedWindow;
q _highPriorityNonFocalRangeFirstZOrder;
q _mediumPriorityNonFocalRangeFirstZOrder;
q _lowPriorityNonFocalRangeFirstZOrder;
Q _maximumWindowsInForegroundJetsamBand;
q _numberOfTopMostWindowsToNeverFreeze;
q _maximumNumberOfVisuallyOpaqueScenesOnStage;
q _numberOfFadingScenesOnStage;
```

## Properties

```
@property (Tq,N,V_highPriorityNonFocalRangeFirstZOrder) highPriorityNonFocalRangeFirstZOrder;
@property (Tq,N,V_mediumPriorityNonFocalRangeFirstZOrder) mediumPriorityNonFocalRangeFirstZOrder;
@property (Tq,N,V_lowPriorityNonFocalRangeFirstZOrder) lowPriorityNonFocalRangeFirstZOrder;
@property (TQ,N,V_maximumWindowsInForegroundJetsamBand) maximumWindowsInForegroundJetsamBand;
@property (Tq,N,V_numberOfTopMostWindowsToNeverFreeze) numberOfTopMostWindowsToNeverFreeze;
@property (Tq,N,V_maximumNumberOfVisuallyOpaqueScenesOnStage) maximumNumberOfVisuallyOpaqueScenesOnStage;
@property (Tq,N,V_numberOfFadingScenesOnStage) numberOfFadingScenesOnStage;
@property (TB,N,V_preventFreezingUnoccludedScenes) preventFreezingUnoccludedScenes;
@property (TB,N,V_prefersProcessTaskSuspensionWhileSceneForegroundAndOccluded) prefersProcessTaskSuspensionWhileSceneForegroundAndOccluded;
@property (TB,N,V_freezeFullyOccludedWindows) freezeFullyOccludedWindows;
@property (TB,N,V_freezeAllWindowsBelowMaximizedWindow) freezeAllWindowsBelowMaximizedWindow;
```

## Class methods

```
+[SBSceneRelevancySettings settingsControllerModule];
+[SBSceneRelevancySettings settingsFor3GBPhysicalMemory];
+[SBSceneRelevancySettings settingsFor4GBPhysicalMemory];
+[SBSceneRelevancySettings settingsFor6GBPhysicalMemory];
+[SBSceneRelevancySettings settingsFor8GBPhysicalMemory];
```

## Instance methods

```
-[SBSceneRelevancySettings setNumberOfTopMostWindowsToNeverFreeze:];
-[SBSceneRelevancySettings freezeFullyOccludedWindows];
-[SBSceneRelevancySettings _commonSetDefaultValues];
-[SBSceneRelevancySettings preventFreezingUnoccludedScenes];
-[SBSceneRelevancySettings freezeAllWindowsBelowMaximizedWindow];
-[SBSceneRelevancySettings setMaximumNumberOfVisuallyOpaqueScenesOnStage:];
-[SBSceneRelevancySettings highPriorityNonFocalRangeFirstZOrder];
-[SBSceneRelevancySettings prefersProcessTaskSuspensionWhileSceneForegroundAndOccluded];
-[SBSceneRelevancySettings _configureDefaultValuesFor6GBPhysicalMemory];
-[SBSceneRelevancySettings _configureDefaultValuesFor4GBPhysicalMemory];
-[SBSceneRelevancySettings setDefaultValues];
-[SBSceneRelevancySettings numberOfTopMostWindowsToNeverFreeze];
-[SBSceneRelevancySettings maximumWindowsInForegroundJetsamBand];
-[SBSceneRelevancySettings _configureForPhysicalMemoryConstraints];
-[SBSceneRelevancySettings setMaximumWindowsInForegroundJetsamBand:];
-[SBSceneRelevancySettings numberOfFadingScenesOnStage];
-[SBSceneRelevancySettings setFreezeAllWindowsBelowMaximizedWindow:];
-[SBSceneRelevancySettings mediumPriorityNonFocalRangeFirstZOrder];
-[SBSceneRelevancySettings setFreezeFullyOccludedWindows:];
-[SBSceneRelevancySettings setNumberOfFadingScenesOnStage:];
-[SBSceneRelevancySettings _configureDefaultValuesFor8GBPhysicalMemory];
-[SBSceneRelevancySettings setHighPriorityNonFocalRangeFirstZOrder:];
-[SBSceneRelevancySettings lowPriorityNonFocalRangeFirstZOrder];
-[SBSceneRelevancySettings setMediumPriorityNonFocalRangeFirstZOrder:];
-[SBSceneRelevancySettings _configureDefaultValuesFor3GBPhysicalMemory];
-[SBSceneRelevancySettings setPrefersProcessTaskSuspensionWhileSceneForegroundAndOccluded:];
-[SBSceneRelevancySettings setLowPriorityNonFocalRangeFirstZOrder:];
-[SBSceneRelevancySettings setPreventFreezingUnoccludedScenes:];
-[SBSceneRelevancySettings maximumNumberOfVisuallyOpaqueScenesOnStage];
```
