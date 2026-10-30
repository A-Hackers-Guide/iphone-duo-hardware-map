# `MPSCNNYOLOLoss`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSCNNKernel`
- 20 instance variables, 15 properties, 42 instance methods, 1 class methods

## Instance variables

```
@"MPSCNNLoss" _lossXY;
@"MPSCNNLoss" _lossWH;
@"MPSCNNLoss" _lossConfidence;
@"MPSCNNLoss" _lossClasses;
i _reductionType;
B _reduceAcrossBatch;
B _rescore;
f _scaleXY;
f _scaleWH;
f _scaleNoObject;
f _scaleObject;
f _scaleClass;
f _minIOUForObjectPresence;
f _maxIOUForObjectAbsence;
f _countOfPresentObjects;
@"NSObject<OS_dispatch_semaphore>" _encodingSemaphore;
@"NSData" _anchorBoxes;
Q _numberOfAnchorBoxes;
@"MPSMatrix" _reductionBuffer;
@"MPSImage" _firstLossTexture;
```

## Properties

```
@property (Tf,N,V_scaleXY) scaleXY;
@property (Tf,N,V_scaleWH) scaleWH;
@property (Tf,N,V_scaleNoObject) scaleNoObject;
@property (Tf,N,V_scaleObject) scaleObject;
@property (Tf,N,V_scaleClass) scaleClass;
@property (Tf,N,V_minIOUForObjectPresence) minIOUForObjectPresence;
@property (Tf,N,V_maxIOUForObjectAbsence) maxIOUForObjectAbsence;
@property (Ti,N,V_reductionType) reductionType;
@property (TQ,N,V_numberOfAnchorBoxes) numberOfAnchorBoxes;
@property (T@"NSData",&,N,V_anchorBoxes) anchorBoxes;
@property (TB,N,V_reduceAcrossBatch) reduceAcrossBatch;
@property (T@"MPSCNNLoss",R,&,N,V_lossXY) lossXY;
@property (T@"MPSCNNLoss",R,&,N,V_lossWH) lossWH;
@property (T@"MPSCNNLoss",R,&,N,V_lossConfidence) lossConfidence;
@property (T@"MPSCNNLoss",R,&,N,V_lossClasses) lossClasses;
```

## Class methods

```
+[MPSCNNYOLOLoss libraryInfo:];
```

## Instance methods

```
-[MPSCNNYOLOLoss initWithDevice:];
-[MPSCNNYOLOLoss debugDescription];
-[MPSCNNYOLOLoss maxBatchSize];
-[MPSCNNYOLOLoss dealloc];
-[MPSCNNYOLOLoss copyWithZone:device:];
-[MPSCNNYOLOLoss initWithCoder:device:];
-[MPSCNNYOLOLoss encodeWithCoder:];
-[MPSCNNYOLOLoss encodeBatchToCommandBuffer:sourceImages:labels:];
-[MPSCNNYOLOLoss initWithDevice:lossDescriptor:];
-[MPSCNNYOLOLoss scaleWH];
-[MPSCNNYOLOLoss scaleXY];
-[MPSCNNYOLOLoss setScaleObject:];
-[MPSCNNYOLOLoss anchorBoxes];
-[MPSCNNYOLOLoss numberOfAnchorBoxes];
-[MPSCNNYOLOLoss reductionType];
-[MPSCNNYOLOLoss scaleClass];
-[MPSCNNYOLOLoss setMaxIOUForObjectAbsence:];
-[MPSCNNYOLOLoss setMinIOUForObjectPresence:];
-[MPSCNNYOLOLoss setReduceAcrossBatch:];
-[MPSCNNYOLOLoss setScaleClass:];
-[MPSCNNYOLOLoss setScaleNoObject:];
-[MPSCNNYOLOLoss setScaleWH:];
-[MPSCNNYOLOLoss setScaleXY:];
-[MPSCNNYOLOLoss setAnchorBoxes:];
-[MPSCNNYOLOLoss countPresetobjectsSourceImages:labels:];
-[MPSCNNYOLOLoss encodeBatchToCommandBuffer:sourceImages:labels:destinationImages:];
-[MPSCNNYOLOLoss encodeToCommandBuffer:sourceImage:labels:];
-[MPSCNNYOLOLoss encodeToCommandBuffer:sourceImage:labels:destinationImage:];
-[MPSCNNYOLOLoss initializeSupportFiltersWithDevice:lossDescriptor:];
-[MPSCNNYOLOLoss lossClasses];
-[MPSCNNYOLOLoss lossConfidence];
-[MPSCNNYOLOLoss lossWH];
-[MPSCNNYOLOLoss lossXY];
-[MPSCNNYOLOLoss maxIOUForObjectAbsence];
-[MPSCNNYOLOLoss minIOUForObjectPresence];
-[MPSCNNYOLOLoss reduceAcrossBatch];
-[MPSCNNYOLOLoss resultStateForSourceImage:sourceStates:];
-[MPSCNNYOLOLoss scaleNoObject];
-[MPSCNNYOLOLoss scaleObject];
-[MPSCNNYOLOLoss setNumberOfAnchorBoxes:];
-[MPSCNNYOLOLoss setReductionType:];
-[MPSCNNYOLOLoss temporaryResultStateForCommandBuffer:sourceImage:sourceStates:];
```
