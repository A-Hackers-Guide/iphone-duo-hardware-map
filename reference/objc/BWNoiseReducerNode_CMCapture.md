# `BWNoiseReducerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _cameraTuningOptions;
@"NSDictionary" _noiseReductionOptions;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{NoiseReductionCtx_s=} _context;
i _contextSynchronization;
i _gpuPriority;
B _threaded;
B _processLuma;
B _useInPlaceAlgorithm;
```

## Class methods

```
+[BWNoiseReducerNode initialize];
```

## Instance methods

```
-[BWNoiseReducerNode prepareForCurrentConfigurationToBecomeLive];
-[BWNoiseReducerNode renderSampleBuffer:forInput:];
-[BWNoiseReducerNode dealloc];
-[BWNoiseReducerNode nodeSubType];
-[BWNoiseReducerNode didSelectFormat:forInput:];
-[BWNoiseReducerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWNoiseReducerNode nodeType];
-[BWNoiseReducerNode didReachEndOfDataForInput:];
-[BWNoiseReducerNode initWithCameraTuningDictionary:sensorIDDictionary:];
```
