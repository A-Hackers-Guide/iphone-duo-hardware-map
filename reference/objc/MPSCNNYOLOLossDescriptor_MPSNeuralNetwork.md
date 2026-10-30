# `MPSCNNYOLOLossDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 16 instance variables, 16 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"MPSCNNLossDescriptor" _XYLossDescriptor;
@"MPSCNNLossDescriptor" _WHLossDescriptor;
@"MPSCNNLossDescriptor" _confidenceLossDescriptor;
@"MPSCNNLossDescriptor" _classesLossDescriptor;
i _reductionType;
B _rescore;
f _scaleXY;
f _scaleWH;
f _scaleNoObject;
f _scaleObject;
f _scaleClass;
f _minIOUForObjectPresence;
f _maxIOUForObjectAbsence;
@"NSData" _anchorBoxes;
Q _numberOfAnchorBoxes;
B _reduceAcrossBatch;
```

## Properties

```
@property (T@"MPSCNNLossDescriptor",&,N,V_XYLossDescriptor) XYLossDescriptor;
@property (T@"MPSCNNLossDescriptor",&,N,V_WHLossDescriptor) WHLossDescriptor;
@property (T@"MPSCNNLossDescriptor",&,N,V_confidenceLossDescriptor) confidenceLossDescriptor;
@property (T@"MPSCNNLossDescriptor",&,N,V_classesLossDescriptor) classesLossDescriptor;
@property (Ti,N,V_reductionType) reductionType;
@property (TB,N,V_reduceAcrossBatch) reduceAcrossBatch;
@property (TB,N,V_rescore) rescore;
@property (Tf,N,V_scaleXY) scaleXY;
@property (Tf,N,V_scaleWH) scaleWH;
@property (Tf,N,V_scaleNoObject) scaleNoObject;
@property (Tf,N,V_scaleObject) scaleObject;
@property (Tf,N,V_scaleClass) scaleClass;
@property (Tf,N,V_minIOUForObjectPresence) minIOUForObjectPresence;
@property (Tf,N,V_maxIOUForObjectAbsence) maxIOUForObjectAbsence;
@property (TQ,N,V_numberOfAnchorBoxes) numberOfAnchorBoxes;
@property (T@"NSData",&,N,V_anchorBoxes) anchorBoxes;
```

## Class methods

```
+[MPSCNNYOLOLossDescriptor cnnLossDescriptorWithXYLossType:WHLossType:confidenceLossType:classesLossType:reductionType:anchorBoxes:numberOfAnchorBoxes:];
```

## Instance methods

```
-[MPSCNNYOLOLossDescriptor debugDescription];
-[MPSCNNYOLOLossDescriptor dealloc];
-[MPSCNNYOLOLossDescriptor copyWithZone:];
-[MPSCNNYOLOLossDescriptor scaleWH];
-[MPSCNNYOLOLossDescriptor scaleXY];
-[MPSCNNYOLOLossDescriptor setScaleObject:];
-[MPSCNNYOLOLossDescriptor WHLossDescriptor];
-[MPSCNNYOLOLossDescriptor XYLossDescriptor];
-[MPSCNNYOLOLossDescriptor anchorBoxes];
-[MPSCNNYOLOLossDescriptor classesLossDescriptor];
-[MPSCNNYOLOLossDescriptor confidenceLossDescriptor];
-[MPSCNNYOLOLossDescriptor numberOfAnchorBoxes];
-[MPSCNNYOLOLossDescriptor reductionType];
-[MPSCNNYOLOLossDescriptor scaleClass];
-[MPSCNNYOLOLossDescriptor setMaxIOUForObjectAbsence:];
-[MPSCNNYOLOLossDescriptor setMinIOUForObjectPresence:];
-[MPSCNNYOLOLossDescriptor setReduceAcrossBatch:];
-[MPSCNNYOLOLossDescriptor setRescore:];
-[MPSCNNYOLOLossDescriptor setScaleClass:];
-[MPSCNNYOLOLossDescriptor setScaleNoObject:];
-[MPSCNNYOLOLossDescriptor setScaleWH:];
-[MPSCNNYOLOLossDescriptor setScaleXY:];
-[MPSCNNYOLOLossDescriptor rescore];
-[MPSCNNYOLOLossDescriptor setAnchorBoxes:];
-[MPSCNNYOLOLossDescriptor initWithXYLossType:WHLossType:confidenceLossType:classesLossType:reductionType:anchorBoxes:numberOfAnchorBoxes:];
-[MPSCNNYOLOLossDescriptor maxIOUForObjectAbsence];
-[MPSCNNYOLOLossDescriptor minIOUForObjectPresence];
-[MPSCNNYOLOLossDescriptor reduceAcrossBatch];
-[MPSCNNYOLOLossDescriptor scaleNoObject];
-[MPSCNNYOLOLossDescriptor scaleObject];
-[MPSCNNYOLOLossDescriptor setClassesLossDescriptor:];
-[MPSCNNYOLOLossDescriptor setConfidenceLossDescriptor:];
-[MPSCNNYOLOLossDescriptor setNumberOfAnchorBoxes:];
-[MPSCNNYOLOLossDescriptor setReductionType:];
-[MPSCNNYOLOLossDescriptor setWHLossDescriptor:];
-[MPSCNNYOLOLossDescriptor setXYLossDescriptor:];
```
