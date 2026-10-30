# `BWDeepFusionProcessorRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"BWDeepFusionProcessorInput" _input;
@"<BWDeepFusionProcessorControllerDelegate>" _delegate;
i _expectedEVZeroFrameCount;
@"NSSet" _expectedBufferTypes;
@"<IBPDeepFusionOutput>" _output;
i _err;
i _demosaicedRawErr;
B _cacheBuffers;
```

## Properties

```
@property (T@"BWDeepFusionProcessorInput",R,N,V_input) input;
@property (T@"<BWDeepFusionProcessorControllerDelegate>",R,N,V_delegate) delegate;
@property (T@"NSSet",R,N,V_expectedBufferTypes) expectedBufferTypes;
@property (T@"<IBPDeepFusionOutput>",&,N,V_output) output;
@property (Ti,N,V_err) err;
@property (Ti,N,V_demosaicedRawErr) demosaicedRawErr;
@property (TB,N,V_cacheBuffers) cacheBuffers;
```

## Instance methods

```
-[BWDeepFusionProcessorRequest input];
-[BWDeepFusionProcessorRequest setErr:];
-[BWDeepFusionProcessorRequest setOutput:];
-[BWDeepFusionProcessorRequest dealloc];
-[BWDeepFusionProcessorRequest setDemosaicedRawErr:];
-[BWDeepFusionProcessorRequest demosaicedRawErr];
-[BWDeepFusionProcessorRequest err];
-[BWDeepFusionProcessorRequest delegate];
-[BWDeepFusionProcessorRequest description];
-[BWDeepFusionProcessorRequest output];
-[BWDeepFusionProcessorRequest cacheBuffers];
-[BWDeepFusionProcessorRequest expectedBufferTypes];
-[BWDeepFusionProcessorRequest setCacheBuffers:];
```
