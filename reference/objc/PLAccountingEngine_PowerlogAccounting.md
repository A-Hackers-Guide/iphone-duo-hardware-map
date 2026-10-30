# `PLAccountingEngine`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLAccountingDistributionManagerDelegate`, `PLAccountingCorrectionManagerDelegate`, `PLAccountingQualificationManagerDelegate`
- 7 instance variables, 11 properties, 54 instance methods, 19 class methods

## Instance variables

```
B _pluggedIn;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"PLActivity" _chunkActivity;
@"PLEntryNotificationOperatorComposition" _batteryListener;
@"PLAccountingDistributionManager" _distributionManager;
@"PLAccountingCorrectionManager" _correctionManager;
@"PLAccountingQualificationManager" _qualificationManager;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (T@"PLActivity",&,V_chunkActivity) chunkActivity;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryListener) batteryListener;
@property (TB,V_pluggedIn) pluggedIn;
@property (T@"PLAccountingDistributionManager",&,N,V_distributionManager) distributionManager;
@property (T@"PLAccountingCorrectionManager",&,N,V_correctionManager) correctionManager;
@property (T@"PLAccountingQualificationManager",&,N,V_qualificationManager) qualificationManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLAccountingEngine sharedInstance];
+[PLAccountingEngine workQueue];
+[PLAccountingEngine debugInstance];
+[PLAccountingEngine accountingDebugEnabled];
+[PLAccountingEngine allBBRootNodeIDs];
+[PLAccountingEngine allDistributionIDs];
+[PLAccountingEngine allQualificationIDs];
+[PLAccountingEngine allSoCRootNodeIDs];
+[PLAccountingEngine clearWithEntryKey:];
+[PLAccountingEngine deviceBBRootNodeIDs];
+[PLAccountingEngine deviceRootNodeIDs];
+[PLAccountingEngine deviceSoCRootNodeIDs];
+[PLAccountingEngine distributionIDForDistributionName:];
+[PLAccountingEngine gasGaugeEntryKey];
+[PLAccountingEngine maxPowerEventChunkInterval];
+[PLAccountingEngine minDistributionEnergy];
+[PLAccountingEngine minEnergy];
+[PLAccountingEngine normalizeWeights:];
+[PLAccountingEngine qualificationIDForQualificationName:];
```

## Instance methods

```
-[PLAccountingEngine setWorkQueue:];
-[PLAccountingEngine setPluggedIn:];
-[PLAccountingEngine didQualifyEnergyEvent:withRootNodeID:withQualificationID:];
-[PLAccountingEngine createQualificationEventPointWithQualificationID:withChildNodeNames:withStartDate:];
-[PLAccountingEngine addQualificationEventIntervalWithLastQualificationEventForward:withQualificationEventForward:];
-[PLAccountingEngine createPowerEventIntervalWithRootNodeID:withPower:withStartDate:withEndDate:];
-[PLAccountingEngine createPowerEventForwardWithRootNodeID:withPower:withStartDate:];
-[PLAccountingEngine didDistributeEnergyEstimate:];
-[PLAccountingEngine createQualificationEventForwardWithQualificationID:withAddingChildNodeName:withStartDate:];
-[PLAccountingEngine setDistributionManager:];
-[PLAccountingEngine createQualificationEventForwardWithQualificationID:withChildNodeNames:withStartDate:];
-[PLAccountingEngine init];
-[PLAccountingEngine setCorrectionManager:];
-[PLAccountingEngine chunkWithLastChunkDate:withNow:];
-[PLAccountingEngine batteryListener];
-[PLAccountingEngine workQueue];
-[PLAccountingEngine qualificationManager];
-[PLAccountingEngine createDistributionEventForwardWithDistributionID:withRemovingChildNodeName:withStartDate:];
-[PLAccountingEngine reset];
-[PLAccountingEngine createPowerEventBackwardWithRootNodeID:withPower:withEndDate:];
-[PLAccountingEngine setBatteryListener:];
-[PLAccountingEngine setChunkActivity:];
-[PLAccountingEngine setQualificationManager:];
-[PLAccountingEngine reload];
-[PLAccountingEngine addDistributionEventIntervalWithLastDistributionEventForward:withDistributionEventForward:];
-[PLAccountingEngine currentDistributionEventForwardWithDistributionID:];
-[PLAccountingEngine distributionManager];
-[PLAccountingEngine createDistributionEventPointWithDistributionID:withChildNodeNameToWeight:withStartDate:];
-[PLAccountingEngine addDistributionEventIntervalWithLastDistributionEventBackward:withDistributionEventBackward:];
-[PLAccountingEngine pluggedIn];
-[PLAccountingEngine createQualificationEventForwardWithQualificationID:withRemovingChildNodeName:withStartDate:];
-[PLAccountingEngine createDistributionEventBackwardWithDistributionID:withChildNodeNameToWeight:withEndDate:];
-[PLAccountingEngine reloadLastDistributionEventsWithLastDeviceBootDate:];
-[PLAccountingEngine addPowerMeasurementEventIntervalWithPower:withStartDate:withEndDate:];
-[PLAccountingEngine didCreateChildEnergyEstimate:withParentEnergyEstimate:];
-[PLAccountingEngine addDistributionEventInterval:];
-[PLAccountingEngine createDistributionEventIntervalWithDistributionID:withChildNodeNameToWeight:withStartDate:withEndDate:];
-[PLAccountingEngine didCorrectEnergyEstimate:];
-[PLAccountingEngine addEnergyMeasurementWithRootNodeID:withEnergy:withRange:];
-[PLAccountingEngine addQualificationEventPoint:];
-[PLAccountingEngine createQualificationEventBackwardWithQualificationID:withChildNodeNames:withEndDate:];
-[PLAccountingEngine addQualificationEventIntervalWithLastQualificationEventBackward:withQualificationEventBackward:];
-[PLAccountingEngine chunkActivity];
-[PLAccountingEngine reloadLastPowerEventsWithLastDeviceBootDate:];
-[PLAccountingEngine correctionManager];
-[PLAccountingEngine createQualificationEventIntervalWithQualificationID:withChildNodeNames:withStartDate:withEndDate:];
-[PLAccountingEngine addQualificationEventInterval:];
-[PLAccountingEngine addDistributionEventPoint:];
-[PLAccountingEngine reloadLastQualificationEventsWithLastDeviceBootDate:];
-[PLAccountingEngine createDistributionEventForwardWithDistributionID:withAddingChildNodeName:withStartDate:];
-[PLAccountingEngine createAggregateRootNodeEnergyEntryWithEnergyEstimate:];
-[PLAccountingEngine createEventWithEvent:withActionBlock:];
-[PLAccountingEngine createDistributionEventForwardWithDistributionID:withChildNodeNameToWeight:withStartDate:];
-[PLAccountingEngine getLastQualifiedEnergyEventDate];
```
