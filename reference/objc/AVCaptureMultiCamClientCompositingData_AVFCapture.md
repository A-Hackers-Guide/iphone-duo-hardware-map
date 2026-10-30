# `AVCaptureMultiCamClientCompositingData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _primarySampleBuffer;
@"CIImage" _primaryImage;
^{opaqueCMSampleBuffer=} _primaryGainMapSampleBuffer;
@"CIImage" _primaryGainMapImage;
^{opaqueCMSampleBuffer=} _secondarySampleBuffer;
@"CIImage" _secondaryImage;
^{opaqueCMSampleBuffer=} _secondaryGainMapSampleBuffer;
@"CIImage" _secondaryGainMapImage;
^{opaqueCMSampleBuffer=} _outputSampleBuffer;
^{opaqueCMSampleBuffer=} _outputGainMapSampleBuffer;
@"NSDictionary" _compositingMetadata;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_primarySampleBuffer) primarySampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_primaryGainMapSampleBuffer) primaryGainMapSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_secondarySampleBuffer) secondarySampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_secondaryGainMapSampleBuffer) secondaryGainMapSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_outputSampleBuffer) outputSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_outputGainMapSampleBuffer) outputGainMapSampleBuffer;
@property (T@"NSDictionary",&,N,V_compositingMetadata) compositingMetadata;
```

## Instance methods

```
-[AVCaptureMultiCamClientCompositingData primarySampleBuffer];
-[AVCaptureMultiCamClientCompositingData dealloc];
-[AVCaptureMultiCamClientCompositingData secondaryImage];
-[AVCaptureMultiCamClientCompositingData primaryImage];
-[AVCaptureMultiCamClientCompositingData _imageForGainMapSampleBuffer:];
-[AVCaptureMultiCamClientCompositingData _imageForSampleBuffer:gainMapMetadata:];
-[AVCaptureMultiCamClientCompositingData _initWithPrimarySampleBuffer:primaryGainMapSampleBuffer:secondarySampleBuffer:secondaryGainMapSampleBuffer:outputSampleBuffer:outputGainMapSampleBuffer:];
-[AVCaptureMultiCamClientCompositingData compositingMetadata];
-[AVCaptureMultiCamClientCompositingData outputGainMapSampleBuffer];
-[AVCaptureMultiCamClientCompositingData outputSampleBuffer];
-[AVCaptureMultiCamClientCompositingData primaryGainMapImage];
-[AVCaptureMultiCamClientCompositingData primaryGainMapSampleBuffer];
-[AVCaptureMultiCamClientCompositingData secondaryGainMapImage];
-[AVCaptureMultiCamClientCompositingData secondaryGainMapSampleBuffer];
-[AVCaptureMultiCamClientCompositingData secondarySampleBuffer];
-[AVCaptureMultiCamClientCompositingData setCompositingMetadata:];
```
