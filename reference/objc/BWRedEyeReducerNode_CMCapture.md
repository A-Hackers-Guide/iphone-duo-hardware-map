# `BWRedEyeReducerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _redEyeReductionParametersByPortType;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"CIContext" _ciContext;
@"CIDualRedEyeRepairSession" _redEyeRepairSession;
^{opaqueCMSampleBuffer=} _primaryImageSampleBuffer;
B _skipRepair;
i _redEyeReductionVersion;
i _inferenceType;
@"NSString" _inferenceAttachmentKey;
```

## Class methods

```
+[BWRedEyeReducerNode initialize];
```

## Instance methods

```
-[BWRedEyeReducerNode prepareForCurrentConfigurationToBecomeLive];
-[BWRedEyeReducerNode renderSampleBuffer:forInput:];
-[BWRedEyeReducerNode dealloc];
-[BWRedEyeReducerNode nodeSubType];
-[BWRedEyeReducerNode inferenceType];
-[BWRedEyeReducerNode didSelectFormat:forInput:];
-[BWRedEyeReducerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWRedEyeReducerNode handleNodeError:forInput:];
-[BWRedEyeReducerNode nodeType];
-[BWRedEyeReducerNode didReachEndOfDataForInput:];
-[BWRedEyeReducerNode inferenceAttachmentKey];
-[BWRedEyeReducerNode initWithVersion:sensorConfigurationsByPortType:];
-[BWRedEyeReducerNode setInferenceAttachmentKey:];
-[BWRedEyeReducerNode setInferenceType:];
```
