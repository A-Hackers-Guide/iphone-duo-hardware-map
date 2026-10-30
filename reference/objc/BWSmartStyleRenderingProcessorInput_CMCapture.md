# `BWSmartStyleRenderingProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 7 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _inputFrame;
B _addFrameFailed;
Q _inputBufferType;
B _applyOnly;
B _enqueued;
^{opaqueCMSampleBuffer=} _sampleBuffer;
Q _bufferType;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_inputFrame) inputFrame;
@property (TQ,R,N,V_inputBufferType) inputBufferType;
@property (TB,R,N,V_addFrameFailed) addFrameFailed;
@property (T^{opaqueCMSampleBuffer=},R,N,V_sampleBuffer) sampleBuffer;
@property (TQ,R,N,V_bufferType) bufferType;
@property (TB,N,GisEnqueued,V_enqueued) enqueued;
@property (TB,R,N,V_applyOnly) applyOnly;
```

## Instance methods

```
-[BWSmartStyleRenderingProcessorInput dealloc];
-[BWSmartStyleRenderingProcessorInput initWithSettings:portType:];
-[BWSmartStyleRenderingProcessorInput sampleBuffer];
-[BWSmartStyleRenderingProcessorInput inputFrame];
-[BWSmartStyleRenderingProcessorInput inputBufferType];
-[BWSmartStyleRenderingProcessorInput addFrameFailed];
-[BWSmartStyleRenderingProcessorInput addSampleBuffer:bufferType:];
-[BWSmartStyleRenderingProcessorInput applyOnly];
-[BWSmartStyleRenderingProcessorInput bufferType];
-[BWSmartStyleRenderingProcessorInput isEnqueued];
-[BWSmartStyleRenderingProcessorInput setEnqueued:];
```
