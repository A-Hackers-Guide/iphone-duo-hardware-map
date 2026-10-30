# `BWSoftISPProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWSoftISPProcessorControllerInputUpdatesDelegate`, `SoftISPProcessorDelegate`
- 16 instance variables, 4 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"SoftISPProcessor" _processor;
@"NSDictionary" _sensorIDByPortType;
^{opaqueCMFormatDescription=} _inputFormatDescription;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _lscFormatDescription;
^{opaqueCMFormatDescription=} _flashLSCFormatDescription;
^{opaqueCMFormatDescription=} _auxSashimiRawFormatDescription;
^{opaqueCMFormatDescription=} _auxFocusPixelH0FormatDescription;
^{opaqueCMFormatDescription=} _auxFocusPixelH1FormatDescription;
B _awbPurgeAfterMaximumFrameCount;
@"NSMutableDictionary" _digitalFlashAWBMetadata;
@"NSMutableDictionary" _digitalFlashLTMMetadata;
d _digitalFlashLTMExposureTime;
f _digitalFlashLTMGain;
B _digitalFlashSFHREnabled;
@"NSMutableDictionary" _swfrPreviewAWBMetadata;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSoftISPProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWSoftISPProcessorController outputPixelFormatForInput:];
-[BWSoftISPProcessorController outputFrameCompleted:];
-[BWSoftISPProcessorController process];
-[BWSoftISPProcessorController dealloc];
-[BWSoftISPProcessorController reset];
-[BWSoftISPProcessorController outputFrameGPUFailure:];
-[BWSoftISPProcessorController initWithConfiguration:];
-[BWSoftISPProcessorController outputFrameEnqueueFailure:];
-[BWSoftISPProcessorController outputPixelFormatForCaptureType:captureFlags:processingMode:isQuadra:];
-[BWSoftISPProcessorController notifyLCBDatabaseUpdated:forPortType:];
-[BWSoftISPProcessorController prepare];
-[BWSoftISPProcessorController notifyProcessInputFrameForUniqueID:];
-[BWSoftISPProcessorController metalImageBufferProcessor];
-[BWSoftISPProcessorController input:addFrame:resolutionFlavor:];
-[BWSoftISPProcessorController requestForInput:delegate:errOut:];
-[BWSoftISPProcessorController newOutputPixelBufferForUniqueID:pixelFormat:width:height:];
-[BWSoftISPProcessorController externalMemoryDescriptorForResolutionFlavors:];
-[BWSoftISPProcessorController outputFrameEnqueued:];
-[BWSoftISPProcessorController outputPixelFormatForCaptureType:processingMode:];
-[BWSoftISPProcessorController outputPixelFormatForCaptureType:captureFlags:processingMode:];
-[BWSoftISPProcessorController newOutputAuxiliaryPixelBufferForUniqueID:pixelFormat:width:height:alignment:];
```
