# `PLAccountingDebugService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 1 instance variables, 1 properties, 36 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _testNames;
```

## Properties

```
@property (T@"NSArray",&,N,V_testNames) testNames;
```

## Class methods

```
+[PLAccountingDebugService load];
+[PLAccountingDebugService printError:];
```

## Instance methods

```
-[PLAccountingDebugService init];
-[PLAccountingDebugService testCorrection2];
-[PLAccountingDebugService testCorrection4];
-[PLAccountingDebugService testPerformance];
-[PLAccountingDebugService testCorrection1];
-[PLAccountingDebugService testCorrection3];
-[PLAccountingDebugService blockingClearQueues];
-[PLAccountingDebugService blockingLogGasGaugeWithTotalPower:withStartDate:withEndDate:];
-[PLAccountingDebugService setTestNames:];
-[PLAccountingDebugService testAddRemoveDistributionEventForward];
-[PLAccountingDebugService testChunk];
-[PLAccountingDebugService testCorrectionInMemory];
-[PLAccountingDebugService testCurrentDistributionEventForward];
-[PLAccountingDebugService testDistribution1];
-[PLAccountingDebugService testDistribution2];
-[PLAccountingDebugService testDistribution3];
-[PLAccountingDebugService testDistribution4];
-[PLAccountingDebugService testDistribution5];
-[PLAccountingDebugService testNames];
-[PLAccountingDebugService testPowerEventIntervalOverlap];
-[PLAccountingDebugService testQualification1];
-[PLAccountingDebugService testQualification2];
-[PLAccountingDebugService testQualification3];
-[PLAccountingDebugService testReloadAfter1];
-[PLAccountingDebugService testReloadAfter2];
-[PLAccountingDebugService testReloadBefore1];
-[PLAccountingDebugService testReloadBefore2];
-[PLAccountingDebugService testShortDistributionEventDuration];
-[PLAccountingDebugService testShortQualificationEventDuration];
-[PLAccountingDebugService verifyAggregateQualificationEnergyWithQualificationID:withRootNodeID:withNodeName:withQualificationEnergy:withDate:];
-[PLAccountingDebugService verifyAggregateRootNodeEnergyWithNodeName:withRootNodeID:withEnergy:withDate:];
-[PLAccountingDebugService verifyLastDistributionEventWithDistributionID:withNodeName:withWeight:];
-[PLAccountingDebugService verifyLastPowerEventWithRootNodeID:withPower:];
-[PLAccountingDebugService verifyLastQualificationEventWithQualificationID:withNodeName:];
-[PLAccountingDebugService verifyTotalCorrectionEnergyWithNodeName:withTotalCorrectionEnergy:withRootNodeID:];
-[PLAccountingDebugService verifyTotalEnergyWithNodeName:withTotalEnergy:withRootNodeID:withEpsilon:];
```
