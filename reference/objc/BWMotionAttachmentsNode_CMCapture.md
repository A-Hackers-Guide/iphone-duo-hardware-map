# `BWMotionAttachmentsNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 7 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSampleBufferProcessor=} _sampleBufferProcessor;
@"NSDictionary" _optionsDict;
@"BWNodeOutput" _sourceVideoWithMotionAttachmentsOutput;
@"BWNodeOutput" _offlineVISMotionDataOutput;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
B _adjustsValidBufferRectForDarkShade;
B _emitMotionAttachmentsSBufForOfflineProResRawVIS;
```

## Properties

```
@property (T@"BWNodeOutput",R,N,V_sourceVideoWithMotionAttachmentsOutput) sourceVideoWithMotionAttachmentsOutput;
@property (T@"BWNodeOutput",R,N,V_offlineVISMotionDataOutput) offlineVISMotionDataOutput;
@property (TB,N,V_adjustsValidBufferRectForDarkShade) adjustsValidBufferRectForDarkShade;
```

## Class methods

```
+[BWMotionAttachmentsNode initialize];
```

## Instance methods

```
-[BWMotionAttachmentsNode prepareForCurrentConfigurationToBecomeLive];
-[BWMotionAttachmentsNode renderSampleBuffer:forInput:];
-[BWMotionAttachmentsNode sourceVideoWithMotionAttachmentsOutput];
-[BWMotionAttachmentsNode initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:inputFormatIsProResRaw:errorOut:];
-[BWMotionAttachmentsNode dealloc];
-[BWMotionAttachmentsNode setAdjustsValidBufferRectForDarkShade:];
-[BWMotionAttachmentsNode hasNonLiveConfigurationChanges];
-[BWMotionAttachmentsNode offlineVISMotionDataOutput];
-[BWMotionAttachmentsNode didReachEndOfDataForConfigurationID:input:];
-[BWMotionAttachmentsNode nodeSubType];
-[BWMotionAttachmentsNode adjustsValidBufferRectForDarkShade];
-[BWMotionAttachmentsNode didSelectFormat:forInput:];
-[BWMotionAttachmentsNode nodeType];
```
