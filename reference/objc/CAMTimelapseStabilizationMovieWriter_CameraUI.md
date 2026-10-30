# `CAMTimelapseStabilizationMovieWriter`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVOfflineVideoStabilizerDataProvider`, `CAMTimelapseMovieWriterProtocol`
- 33 instance variables, 37 properties, 55 instance methods, 1 class methods

## Instance variables

```
B _suspended;
B __preferHEVC;
@"NSArray" __frameFilePaths;
@"NSArray" __visMetadataFilePaths;
@"NSObject<OS_dispatch_queue>" __movieWritingQueue;
@"NSObject<OS_dispatch_queue>" __syncQueue;
@"NSObject<OS_dispatch_queue>" __readingQueue;
@"NSObject<OS_dispatch_queue>" __decodeQueue;
@"NSObject<OS_dispatch_queue>" __pixelTransferQueue;
@"NSObject<OS_dispatch_semaphore>" __semFrameGetter;
@"NSObject<OS_dispatch_semaphore>" __semFileReader;
^{__CFArray=} __frameList;
@"NSDate" __movieCreationDate;
@"CLLocation" __movieCreationLocation;
@"NSString" __movieOutputPath;
q __movieFramesPerSecond;
@"AVOfflineVideoStabilizer" __stabilizer;
@"AVAssetWriter" __writer;
@"AVAssetWriterInput" __videoInput;
@"AVAssetWriterInputPixelBufferAdaptor" __pixelBufferAdaptor;
q __frameCountWrittenToMovie;
q __nextSourceFrameIndex;
q __nextMetadataFrameIndex;
q __firstFrameIndex;
^{__CVBuffer=} __stashedSourceFrame;
@"NSMutableSet" __badFrameSet;
@"NSMutableSet" __badMetadataSet;
q __badMetadataErrorThreshold;
^{OpaqueVTPixelTransferSession=} __pixelTransferSession;
Q __frameLoadMode;
@? __completion;
^v __powerAssertion;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} __movieTransform;
```

## Properties

```
@property (T@"NSArray",R,N,V__frameFilePaths) _frameFilePaths;
@property (T@"NSArray",R,N,V__visMetadataFilePaths) _visMetadataFilePaths;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__movieWritingQueue) _movieWritingQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__syncQueue) _syncQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__readingQueue) _readingQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__decodeQueue) _decodeQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__pixelTransferQueue) _pixelTransferQueue;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V__semFrameGetter) _semFrameGetter;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V__semFileReader) _semFileReader;
@property (T^{__CFArray=},R,N,V__frameList) _frameList;
@property (T@"NSDate",R,N,V__movieCreationDate) _movieCreationDate;
@property (T@"CLLocation",R,N,V__movieCreationLocation) _movieCreationLocation;
@property (T@"NSString",R,N,V__movieOutputPath) _movieOutputPath;
@property (T{CGAffineTransform=dddddd},R,N,V__movieTransform) _movieTransform;
@property (Tq,R,N,V__movieFramesPerSecond) _movieFramesPerSecond;
@property (TB,R,N,V__preferHEVC) _preferHEVC;
@property (T@"AVOfflineVideoStabilizer",R,N,V__stabilizer) _stabilizer;
@property (T@"AVAssetWriter",R,N,V__writer) _writer;
@property (T@"AVAssetWriterInput",R,N,V__videoInput) _videoInput;
@property (T@"AVAssetWriterInputPixelBufferAdaptor",R,N,V__pixelBufferAdaptor) _pixelBufferAdaptor;
@property (Tq,R,N,V__frameCountWrittenToMovie) _frameCountWrittenToMovie;
@property (Tq,R,N,V__nextSourceFrameIndex) _nextSourceFrameIndex;
@property (Tq,R,N,V__nextMetadataFrameIndex) _nextMetadataFrameIndex;
@property (Tq,R,N,V__firstFrameIndex) _firstFrameIndex;
@property (T^{__CVBuffer=},R,N,V__stashedSourceFrame) _stashedSourceFrame;
@property (T@"NSMutableSet",R,N,V__badFrameSet) _badFrameSet;
@property (T@"NSMutableSet",R,N,V__badMetadataSet) _badMetadataSet;
@property (Tq,R,N,V__badMetadataErrorThreshold) _badMetadataErrorThreshold;
@property (T^{OpaqueVTPixelTransferSession=},R,N,V__pixelTransferSession) _pixelTransferSession;
@property (TQ,R,N,V__frameLoadMode) _frameLoadMode;
@property (T@?,R,C,N,V__completion) _completion;
@property (T^v,R,N,V__powerAssertion) _powerAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisSuspended,V_suspended) suspended;
```

## Class methods

```
+[CAMTimelapseStabilizationMovieWriter _desiredOutputSizeForSourcePixelBuffer:];
```

## Instance methods

```
-[CAMTimelapseStabilizationMovieWriter setSuspended:];
-[CAMTimelapseStabilizationMovieWriter _reset];
-[CAMTimelapseStabilizationMovieWriter _syncQueue];
-[CAMTimelapseStabilizationMovieWriter isSuspended];
-[CAMTimelapseStabilizationMovieWriter init];
-[CAMTimelapseStabilizationMovieWriter _cleanup];
-[CAMTimelapseStabilizationMovieWriter dealloc];
-[CAMTimelapseStabilizationMovieWriter _powerAssertion];
-[CAMTimelapseStabilizationMovieWriter copySourcePixelBufferForFrameNumber:outputSampleTime:stabilizer:];
-[CAMTimelapseStabilizationMovieWriter copySourceStabilizationMetadataForFrameNumber:outputSampleTime:stabilizer:];
-[CAMTimelapseStabilizationMovieWriter _badMetadataSet];
-[CAMTimelapseStabilizationMovieWriter _movieTransform];
-[CAMTimelapseStabilizationMovieWriter _semFrameGetter];
-[CAMTimelapseStabilizationMovieWriter writeMovieFromImageFiles:visMetadataFiles:startDate:location:outputPath:transform:framesPerSecond:preferHEVC:completionHandler:];
-[CAMTimelapseStabilizationMovieWriter _frameFilePaths];
-[CAMTimelapseStabilizationMovieWriter _writer];
-[CAMTimelapseStabilizationMovieWriter _appendPixelBufferToMovie:];
-[CAMTimelapseStabilizationMovieWriter _badFrameSet];
-[CAMTimelapseStabilizationMovieWriter _badMetadataErrorThreshold];
-[CAMTimelapseStabilizationMovieWriter _completion];
-[CAMTimelapseStabilizationMovieWriter _copyNextSampleBufferFromStabilizer:];
-[CAMTimelapseStabilizationMovieWriter _copySourcePixelBufferForNextFrame:skipBadFrames:];
-[CAMTimelapseStabilizationMovieWriter _cropPixelBufferIfNeeded:];
-[CAMTimelapseStabilizationMovieWriter _decodeFirstFrameAgain];
-[CAMTimelapseStabilizationMovieWriter _decodeQueue];
-[CAMTimelapseStabilizationMovieWriter _finishMovieWithCompletionHandler:];
-[CAMTimelapseStabilizationMovieWriter _finishMovieWithFailure];
-[CAMTimelapseStabilizationMovieWriter _finishMovieWithRestartUnstabilized];
-[CAMTimelapseStabilizationMovieWriter _firstFrameIndex];
-[CAMTimelapseStabilizationMovieWriter _frameCountWrittenToMovie];
-[CAMTimelapseStabilizationMovieWriter _frameList];
-[CAMTimelapseStabilizationMovieWriter _frameLoadMode];
-[CAMTimelapseStabilizationMovieWriter _movieCreationDate];
-[CAMTimelapseStabilizationMovieWriter _movieCreationLocation];
-[CAMTimelapseStabilizationMovieWriter _movieFramesPerSecond];
-[CAMTimelapseStabilizationMovieWriter _movieOutputPath];
-[CAMTimelapseStabilizationMovieWriter _movieWritingQueue];
-[CAMTimelapseStabilizationMovieWriter _nextMetadataFrameIndex];
-[CAMTimelapseStabilizationMovieWriter _nextSourceFrameIndex];
-[CAMTimelapseStabilizationMovieWriter _pixelBufferAdaptor];
-[CAMTimelapseStabilizationMovieWriter _pixelTransferQueue];
-[CAMTimelapseStabilizationMovieWriter _pixelTransferSession];
-[CAMTimelapseStabilizationMovieWriter _preferHEVC];
-[CAMTimelapseStabilizationMovieWriter _readingQueue];
-[CAMTimelapseStabilizationMovieWriter _requestNextFrameReadDecode];
-[CAMTimelapseStabilizationMovieWriter _restartUnstabilized];
-[CAMTimelapseStabilizationMovieWriter _semFileReader];
-[CAMTimelapseStabilizationMovieWriter _setMetadataOnVideoTrackAssetWriterInput:];
-[CAMTimelapseStabilizationMovieWriter _stabilizer];
-[CAMTimelapseStabilizationMovieWriter _startAsyncDecoding];
-[CAMTimelapseStabilizationMovieWriter _startWritingWithOutputPath:width:height:videoFormatDescription:transform:framesPerSecond:frameCount:preferHEVC:visMetadataCount:videoMetadata:];
-[CAMTimelapseStabilizationMovieWriter _stashedSourceFrame];
-[CAMTimelapseStabilizationMovieWriter _videoInput];
-[CAMTimelapseStabilizationMovieWriter _visMetadataFilePaths];
-[CAMTimelapseStabilizationMovieWriter _writeMovieAsynchronously];
```
