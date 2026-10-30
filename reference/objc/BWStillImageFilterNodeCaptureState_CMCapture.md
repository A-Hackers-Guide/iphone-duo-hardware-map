# `BWStillImageFilterNodeCaptureState`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _faceAdjustedBlurMapFromStandardResolutionImage;
@"NSDictionary" _attachedMediaFromStandardResolutionImage;
@"NSDictionary" _inferenceResultsFromStandardResolutionImage;
^{CGImageMetadata=} _portraitStillImageAuxDepthMetadata;
^{opaqueCMSampleBuffer=} _blurredGainMapSbuf;
@"NSError" _blurMapRenderErrorFromStandardResolutionImage;
^{opaqueCMSampleBuffer=} _learnedCoefficientsSbuf;
^{opaqueCMSampleBuffer=} _commonEffectsSbuf;
^{opaqueCMSampleBuffer=} _unstyledFullResolutionSbuf;
^{opaqueCMSampleBuffer=} _styledFullResolutionSbuf;
@"BWSmartStyleAttachmentTransferManager" _transferManager;
i _pendingSbufEmits;
B _consumed;
B _unneeded;
```

## Properties

```
@property (T@"NSError",&,N,V_blurMapRenderErrorFromStandardResolutionImage) blurMapRenderErrorFromStandardResolutionImage;
@property (T^{__CVBuffer=},&,N,V_faceAdjustedBlurMapFromStandardResolutionImage) faceAdjustedBlurMapFromStandardResolutionImage;
@property (T^{opaqueCMSampleBuffer=},&,N,V_blurredGainMapSbuf) blurredGainMapSbuf;
@property (T@"NSDictionary",&,N,V_attachedMediaFromStandardResolutionImage) attachedMediaFromStandardResolutionImage;
@property (T@"NSDictionary",&,N,V_inferenceResultsFromStandardResolutionImage) inferenceResultsFromStandardResolutionImage;
@property (T^{CGImageMetadata=},&,N,V_portraitStillImageAuxDepthMetadata) portraitStillImageAuxDepthMetadata;
@property (T^{opaqueCMSampleBuffer=},&,N,V_learnedCoefficientsSbuf) learnedCoefficientsSbuf;
@property (T^{opaqueCMSampleBuffer=},&,N,V_unstyledFullResolutionSbuf) unstyledFullResolutionSbuf;
@property (T^{opaqueCMSampleBuffer=},&,N,V_styledFullResolutionSbuf) styledFullResolutionSbuf;
@property (T^{opaqueCMSampleBuffer=},&,N,V_commonEffectsSbuf) commonEffectsSbuf;
@property (T@"BWSmartStyleAttachmentTransferManager",R,N,V_transferManager) transferManager;
@property (TB,R,N,V_consumed) consumed;
@property (TB,N) unneeded;
```

## Instance methods

```
-[BWStillImageFilterNodeCaptureState dealloc];
-[BWStillImageFilterNodeCaptureState description];
-[BWStillImageFilterNodeCaptureState consumed];
-[BWStillImageFilterNodeCaptureState transferManager];
-[BWStillImageFilterNodeCaptureState attachedMediaFromStandardResolutionImage];
-[BWStillImageFilterNodeCaptureState blurMapRenderErrorFromStandardResolutionImage];
-[BWStillImageFilterNodeCaptureState blurredGainMapSbuf];
-[BWStillImageFilterNodeCaptureState commonEffectsSbuf];
-[BWStillImageFilterNodeCaptureState faceAdjustedBlurMapFromStandardResolutionImage];
-[BWStillImageFilterNodeCaptureState inferenceResultsFromStandardResolutionImage];
-[BWStillImageFilterNodeCaptureState initWithExpectedSbufEmits:];
-[BWStillImageFilterNodeCaptureState learnedCoefficientsSbuf];
-[BWStillImageFilterNodeCaptureState portraitStillImageAuxDepthMetadata];
-[BWStillImageFilterNodeCaptureState releaseStashedAttachedMediaAndInferenceResultsFromStandardRes];
-[BWStillImageFilterNodeCaptureState releaseStyledUnstyledSynchronizationBuffers];
-[BWStillImageFilterNodeCaptureState sbufEmitted];
-[BWStillImageFilterNodeCaptureState setAttachedMediaFromStandardResolutionImage:];
-[BWStillImageFilterNodeCaptureState setBlurMapRenderErrorFromStandardResolutionImage:];
-[BWStillImageFilterNodeCaptureState setBlurredGainMapSbuf:];
-[BWStillImageFilterNodeCaptureState setCommonEffectsSbuf:];
-[BWStillImageFilterNodeCaptureState setFaceAdjustedBlurMapFromStandardResolutionImage:];
-[BWStillImageFilterNodeCaptureState setInferenceResultsFromStandardResolutionImage:];
-[BWStillImageFilterNodeCaptureState setLearnedCoefficientsSbuf:];
-[BWStillImageFilterNodeCaptureState setPortraitStillImageAuxDepthMetadata:];
-[BWStillImageFilterNodeCaptureState setStyledFullResolutionSbuf:];
-[BWStillImageFilterNodeCaptureState setUnneeded:];
-[BWStillImageFilterNodeCaptureState setUnstyledFullResolutionSbuf:];
-[BWStillImageFilterNodeCaptureState stashMediaFromRenderedBlurMap:];
-[BWStillImageFilterNodeCaptureState styledFullResolutionSbuf];
-[BWStillImageFilterNodeCaptureState unneeded];
-[BWStillImageFilterNodeCaptureState unstyledFullResolutionSbuf];
```
