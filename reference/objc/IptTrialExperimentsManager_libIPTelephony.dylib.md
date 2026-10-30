# `IptTrialExperimentsManager`

- Image: [`/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`](../userland/System__Library__PrivateFrameworks__IPTelephony.framework__Support__libIPTelephony.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"TRIClient" trialClient;
^{dispatch_queue_s=} _cellularProdExpQueue;
```

## Properties

```
@property (T^{dispatch_queue_s=},V_cellularProdExpQueue) cellularProdExpQueue;
```

## Class methods

```
+[IptTrialExperimentsManager getSharedInstance];
```

## Instance methods

```
-[IptTrialExperimentsManager init];
-[IptTrialExperimentsManager updateTreatment];
-[IptTrialExperimentsManager cellularProdExpQueue];
-[IptTrialExperimentsManager notifyRegisteredClientsForExperimentEnd];
-[IptTrialExperimentsManager notifyRegisteredClientsForExperimentStart:];
-[IptTrialExperimentsManager readParametersFromPlist:];
-[IptTrialExperimentsManager setCellularProdExpQueue:];
-[IptTrialExperimentsManager subscribeToTrial];
```
