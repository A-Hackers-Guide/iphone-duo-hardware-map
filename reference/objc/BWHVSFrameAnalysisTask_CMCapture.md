# `BWHVSFrameAnalysisTask`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
^{opaqueCMSampleBuffer=} _yuvSampleBuffer;
^{opaqueCMSampleBuffer=} _matchingMainSensorRawSampleBuffer;
^{opaqueCMSampleBuffer=} _matchingSIFRSensorRawSampleBuffer;
^{opaqueCMSampleBuffer=} _imageEmbeddingSampleBuffer;
^{opaqueCMSampleBuffer=} _faceQualitySampleBuffer;
@"NSObject<OS_dispatch_group>" _subtaskGroup;
B _analysisEnabled;
@"FigCaptureWorkInterval" _subtaskWorkInterval;
@"NSDictionary" _workIntervalDictionary;
i _numberOfSubtaskThreads;
Ai _remainingSubtaskLeaves;
@"FigCaptureWorkIntervalInfo" _workIntervalInfo;
@"NSDictionary" _sharpnessResults;
@"NSArray" _faceObservations;
@"NSDictionary" _imageEmbedding;
@"NSData" _personMaskPNGData;
@"NSString" _loggingPrefix;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_yuvSampleBuffer) yuvSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_matchingMainSensorRawSampleBuffer) matchingMainSensorRawSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_matchingSIFRSensorRawSampleBuffer) matchingSIFRSensorRawSampleBuffer;
@property (TB,R,N,V_analysisEnabled) analysisEnabled;
@property (T@"NSDictionary",C,N,V_sharpnessResults) sharpnessResults;
@property (T@"NSArray",C,N,V_faceObservations) faceObservations;
@property (T@"NSDictionary",C,N,V_imageEmbedding) imageEmbedding;
@property (T@"NSData",C,N,V_personMaskPNGData) personMaskPNGData;
```

## Instance methods

```
-[BWHVSFrameAnalysisTask setFaceObservations:];
-[BWHVSFrameAnalysisTask dealloc];
-[BWHVSFrameAnalysisTask waitUntilComplete];
-[BWHVSFrameAnalysisTask faceObservations];
-[BWHVSFrameAnalysisTask description];
-[BWHVSFrameAnalysisTask imageEmbedding];
-[BWHVSFrameAnalysisTask yuvSampleBuffer];
-[BWHVSFrameAnalysisTask analysisEnabled];
-[BWHVSFrameAnalysisTask initWithYUVSampleBuffer:matchingMainSensorRawSampleBuffer:matchingSIFRSensorRawSampleBuffer:imageEmbeddingSampleBuffer:faceQualitySampleBuffer:subtaskGroup:subtaskWorkInterval:numberOfSubtaskThreads:];
-[BWHVSFrameAnalysisTask joinSubtaskThreadWithName:];
-[BWHVSFrameAnalysisTask leaveSubtaskThread];
-[BWHVSFrameAnalysisTask matchingMainSensorRawSampleBuffer];
-[BWHVSFrameAnalysisTask matchingSIFRSensorRawSampleBuffer];
-[BWHVSFrameAnalysisTask personMaskPNGData];
-[BWHVSFrameAnalysisTask setImageEmbedding:];
-[BWHVSFrameAnalysisTask setPersonMaskPNGData:];
-[BWHVSFrameAnalysisTask setSharpnessResults:];
-[BWHVSFrameAnalysisTask sharpnessResults];
```
