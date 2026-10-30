# `SBButterflyRegionsModelModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 15 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBAppsRegionModel" _nextAppsRegionModel;
@"SBDeckRegionModel" _nextDeckRegionModel;
@"NSString" _appExposeBundleID;
Q _appLayoutsGenerationCount;
@"NSArray" _nextSpacesBeforeAppsRegion;
@"NSArray" _nextSpacesAfterAppsRegion;
@"NSArray" _appLayoutsAtTimeOfComputingDeck;
@"SBAppsRegionModel" _appsRegionAtTimeOfComputingDeck;
B _wasSplitSupportedAtTimeOfComputingDeck;
@"NSSet" _transientlyPairedDisplayItems;
Q _clearTransientlyRememberedPairingGeneration;
@"NSString" _clearTransientlyRememberedPairingTimerReason;
@"NSDate" _clearTransientlyRememberedPairingTimerStartedAt;
d _clearTransientlyRememberedPairingTimerPausedRemaining;
B _inContinuousFold;
```

## Instance methods

```
-[SBButterflyRegionsModelModifier stateModel];
-[SBButterflyRegionsModelModifier transientlyPairedDisplayItems];
-[SBButterflyRegionsModelModifier willUpdate];
-[SBButterflyRegionsModelModifier init];
-[SBButterflyRegionsModelModifier timerFired:];
-[SBButterflyRegionsModelModifier willBegin];
-[SBButterflyRegionsModelModifier _clearTransientlyRememberedPairing];
-[SBButterflyRegionsModelModifier _recomputeForAppLayouts:];
-[SBButterflyRegionsModelModifier _recomputeForTransition:];
-[SBButterflyRegionsModelModifier _startClearTransientlyRememberedPairingTimerWithDelay:];
-[SBButterflyRegionsModelModifier continuousFoldDidBegin:];
-[SBButterflyRegionsModelModifier continuousFoldDidEnd:];
-[SBButterflyRegionsModelModifier itemInserted:];
-[SBButterflyRegionsModelModifier itemRemoved:];
-[SBButterflyRegionsModelModifier switcherInterfaceOrientationChanged:];
-[SBButterflyRegionsModelModifier transitionWillPrepare:];
```
