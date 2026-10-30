# `JFXVideoWriter`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 37 instance variables, 16 properties, 60 instance methods, 8 class methods

## Instance variables

```
@"AVAssetWriter" _videoAssetWriter;
@"AVAssetWriterInput" _videoAssetWriterInput;
@"AVAssetWriterInput" _audioAssetWriterInput;
^{opaqueCMFormatDescription=} _audioFormatHint;
@"AVAssetWriter" _metadataAssetWriter;
@"AVAssetWriterInput" _depthAssetWriterInput;
@"AVAssetWriterInput" _compressedDepthAssetWriterInput;
@"AVAssetWriterInput" _exposureMetadataAssetWriterInput;
@"AVAssetWriterInput" _faceMetadataAssetWriterInput;
@"AVAssetWriterInput" _JFXARMetadataAssetWriterInput;
@"AVAssetWriterInputPixelBufferAdaptor" _depthAdaptor;
@"AVAssetWriterInputMetadataAdaptor" _exposureMetadataAdaptor;
@"AVAssetWriterInputMetadataAdaptor" _faceMetadataAdaptor;
@"AVAssetWriterInputMetadataAdaptor" _JFXARMetadataMetadataAdaptor;
B _wroteSessionStartTime;
B _wroteFirstAudioSample;
{?="value"q"timescale"i"flags"I"epoch"q} _sessionStartTime;
{?="value"q"timescale"i"flags"I"epoch"q} _sessionVideoEndTime;
{?="value"q"timescale"i"flags"I"epoch"q} _sessionMetadataEndTime;
AB _preparingWriter;
AB _finishingWritingMovie;
@"NSLock" _finishingLock;
@"WriterReorderQ" _reorderQ;
@"NSMutableArray" _audioBufferQ;
B _storeFaceMetadata;
B _storeDepthDataAsVideoTrack;
B _trackOutOfOrderVideoBuffers;
i _depthCodecType;
{?="width"i"height"i} _depthDimensions;
@"NSData" _animojiMetadata;
@"<JFXVideoWriterDelegate>" _delegate;
@"NSURL" _folderURL;
@"NSDictionary" _videoOutputSettings;
@"NSDictionary" _audioOutputSettings;
@"JFXDepthCompressor" _depthCompressor;
@"NSDictionary" _depthBGRAPixelBufferAttributes;
Q _signPostID;
```

## Properties

```
@property (T@"NSURL",&,N,V_folderURL) folderURL;
@property (T@"NSURL",R,N) videoURL;
@property (T@"NSURL",R,N) metadataURL;
@property (T@"NSDictionary",C,N,V_videoOutputSettings) videoOutputSettings;
@property (T@"NSDictionary",C,N,V_audioOutputSettings) audioOutputSettings;
@property (T@"JFXDepthCompressor",&,N,V_depthCompressor) depthCompressor;
@property (T@"NSDictionary",C,N,V_depthBGRAPixelBufferAttributes) depthBGRAPixelBufferAttributes;
@property (TQ,N,V_signPostID) signPostID;
@property (TB,R,N,V_wroteSessionStartTime) wroteSessionStartTime;
@property (TB,N,V_storeFaceMetadata) storeFaceMetadata;
@property (TB,N,V_storeDepthDataAsVideoTrack) storeDepthDataAsVideoTrack;
@property (T{?=ii},N,V_depthDimensions) depthDimensions;
@property (T@"NSData",&,N,V_animojiMetadata) animojiMetadata;
@property (T@"<JFXVideoWriterDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_trackOutOfOrderVideoBuffers) trackOutOfOrderVideoBuffers;
@property (Ti,N,V_depthCodecType) depthCodecType;
```

## Class methods

```
+[JFXVideoWriter JFX_faceAnchorMetadataIdentifier];
+[JFXVideoWriter JFX_funcamCameraPositionMetadataIdentifier];
+[JFXVideoWriter META_JFXARMetadataIdentifier];
+[JFXVideoWriter META_metadataForVideo:completion:];
+[JFXVideoWriter JFX_animojiMetadataIdentifier];
+[JFXVideoWriter JFX_funcamCaptureInterfaceOrientationMetadataIdentifier];
+[JFXVideoWriter META_ARMetadataTrackForAsset:];
+[JFXVideoWriter META_metadataAssetTrackFromAsset:metadataIdentifier:];
```

## Instance methods

```
-[JFXVideoWriter setDepthDimensions:];
-[JFXVideoWriter metadataURL];
-[JFXVideoWriter setDelegate:];
-[JFXVideoWriter depthDimensions];
-[JFXVideoWriter delegate];
-[JFXVideoWriter videoURL];
-[JFXVideoWriter finishWritingWithCompletionHandler:];
-[JFXVideoWriter startSessionAtSourceTime:];
-[JFXVideoWriter audioOutputSettings];
-[JFXVideoWriter setAudioOutputSettings:];
-[JFXVideoWriter JFX_writeSampleBuffer:assetWriterInput:sampleType:depthAdaptor:];
-[JFXVideoWriter animojiMetadata];
-[JFXVideoWriter JFX_copyDepthBufferAsBGRA:];
-[JFXVideoWriter JFX_queueAudioBufferBeforeSessionStart:];
-[JFXVideoWriter JFX_removeFileAtURL:];
-[JFXVideoWriter JFX_setupAudioOutput:];
-[JFXVideoWriter JFX_setupCompressedDepthOutputWithTransform:error:];
-[JFXVideoWriter JFX_setupFaceMetadataOutput:];
-[JFXVideoWriter JFX_setupMetadataWriterWithTransform:error:];
-[JFXVideoWriter JFX_setupVideoOutput:error:];
-[JFXVideoWriter JFX_startSessionAtSourceTime_noLock:];
-[JFXVideoWriter JFX_writeBuffer:sampleType:];
-[JFXVideoWriter JFX_writeDepthBufferForAVDepthData:withTimingInfo:];
-[JFXVideoWriter JFX_writeFaceDetectMetadata:pts:];
-[JFXVideoWriter JFX_writeJFXARMetadata:time:];
-[JFXVideoWriter setTrackOutOfOrderVideoBuffers:];
-[JFXVideoWriter JFX_drainQueuedAudioBufferBeforeSessionStart_noLock];
-[JFXVideoWriter JFX_fileLevelMetadata];
-[JFXVideoWriter depthCompressor];
-[JFXVideoWriter JFX_setupAutoExposureMetadataOutput:];
-[JFXVideoWriter JFX_setupDepthOutputWithTransform:error:];
-[JFXVideoWriter JFX_setupJFXARMetadataTrack:];
-[JFXVideoWriter JFX_setupVideoWriterWithTransform:error:];
-[JFXVideoWriter JFX_writeAutoExposureMetadata:];
-[JFXVideoWriter JFX_writeBuffer:sampleType:arMetadata:];
-[JFXVideoWriter JFX_writeDepthData:timingInfo:];
-[JFXVideoWriter JFX_writeFaceMetadata:withTimingInfo:];
-[JFXVideoWriter JFX_writerCanBegin:];
-[JFXVideoWriter depthBGRAPixelBufferAttributes];
-[JFXVideoWriter depthCodecType];
-[JFXVideoWriter folderURL];
-[JFXVideoWriter initWithFolderURL:videoOutputSettings:audioOutputSettings:audioFormatHint:];
-[JFXVideoWriter setAnimojiMetadata:];
-[JFXVideoWriter setDepthBGRAPixelBufferAttributes:];
-[JFXVideoWriter setDepthCodecType:];
-[JFXVideoWriter setDepthCompressor:];
-[JFXVideoWriter setFolderURL:];
-[JFXVideoWriter setSignPostID:];
-[JFXVideoWriter setStoreDepthDataAsVideoTrack:];
-[JFXVideoWriter setStoreFaceMetadata:];
-[JFXVideoWriter setVideoOutputSettings:];
-[JFXVideoWriter signPostID];
-[JFXVideoWriter startWriterWithVideoTransform:error:];
-[JFXVideoWriter storeDepthDataAsVideoTrack];
-[JFXVideoWriter storeFaceMetadata];
-[JFXVideoWriter trackOutOfOrderVideoBuffers];
-[JFXVideoWriter videoOutputSettings];
-[JFXVideoWriter writeAudioBuffer:];
-[JFXVideoWriter writeCameraFrameSet:];
-[JFXVideoWriter wroteSessionStartTime];
```
