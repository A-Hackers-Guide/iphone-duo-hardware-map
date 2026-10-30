# `BWFlexGTCNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLCommandQueue>" _commandQueue;
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"NSMutableDictionary" _sensorIDDictionaryByPortType;
B _enableHighlightAdjustment;
@"CMIFlexGTCStage" _cmiFlexGTCStage;
```

## Class methods

```
+[BWFlexGTCNode initialize];
```

## Instance methods

```
-[BWFlexGTCNode prepareForCurrentConfigurationToBecomeLive];
-[BWFlexGTCNode renderSampleBuffer:forInput:];
-[BWFlexGTCNode dealloc];
-[BWFlexGTCNode initWithNodeConfiguration:sensorConfigurationsByPortType:metalCommandQueue:];
-[BWFlexGTCNode didReachEndOfDataForConfigurationID:input:];
-[BWFlexGTCNode nodeSubType];
-[BWFlexGTCNode didSelectFormat:forInput:];
-[BWFlexGTCNode nodeType];
```
