# `ETTask`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 24 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} network;
B _dumpData;
@"ETModelDef" _model;
@"ETOptimizerDef" _optimizer;
@"ETImageDescriptorExtractor" _extractor;
```

## Properties

```
@property (T@"ETModelDef",&,N,V_model) model;
@property (T@"ETOptimizerDef",&,N,V_optimizer) optimizer;
@property (T@"ETImageDescriptorExtractor",&,N,V_extractor) extractor;
@property (TB,N,V_dumpData) dumpData;
```

## Instance methods

```
-[ETTask model];
-[ETTask setModel:];
-[ETTask init];
-[ETTask extractor];
-[ETTask setExtractor:];
-[ETTask dumpData];
-[ETTask evaluate:];
-[ETTask fit:numberOfBatches:outputNames:batchCallback:];
-[ETTask fit:numberOfBatches:withProgress:];
-[ETTask fit:numberOfEpochs:outputNames:batchCallback:];
-[ETTask fit:numberOfEpochs:withProgress:];
-[ETTask initWithModelDef:optimizerDef:extractor:];
-[ETTask initWithModelDef:optimizerDef:extractor:needWeightsInitialization:];
-[ETTask initWithModelDef:optimizerDef:lossConfig:];
-[ETTask initWithModelDef:optimizerDef:lossConfig:extractor:];
-[ETTask moveToGPU:error:];
-[ETTask optimizer];
-[ETTask reinitializeVariables];
-[ETTask runBatches:numberOfBatches:outputNames:batchCallback:];
-[ETTask runInference:outputNames:batchCallback:];
-[ETTask saveNetwork:];
-[ETTask saveNetwork:revertToInferenceMode:];
-[ETTask setDumpData:];
-[ETTask setOptimizer:];
```
