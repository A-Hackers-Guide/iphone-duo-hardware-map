# `CAMTimelapseMovieWriter`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMTimelapseMovieWriterProtocol`
- 19 instance variables, 23 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _suspended;
@"NSArray" __frameFilePaths;
q __nextReadFileIndex;
q __residentImageDataCount;
q __residentPixelBufferCount;
@"NSMutableDictionary" __availableImageData;
@"NSMutableDictionary" __availablePixelBuffers;
@"NSMutableSet" __inFlightReadFrameIndexes;
@"NSObject<OS_dispatch_queue>" __synchronizationQueue;
@"NSOperationQueue" __imageReadQueue;
@"NSOperationQueue" __imageDecodeQueue;
@"NSObject<OS_dispatch_queue>" __movieWritingQueue;
@"AVAssetWriter" __writer;
@"AVAssetWriterInput" __videoInput;
@"AVAssetWriterInputPixelBufferAdaptor" __pixelBufferAdaptor;
q __framesPerSecond;
q __nextWriteFileIndex;
q __currentOutputFrameIndex;
@? __completion;
```

## Properties

```
@property (T@"NSArray",R,N,V__frameFilePaths) _frameFilePaths;
@property (Tq,R,N,V__nextReadFileIndex) _nextReadFileIndex;
@property (Tq,R,N,V__residentImageDataCount) _residentImageDataCount;
@property (Tq,R,N,V__residentPixelBufferCount) _residentPixelBufferCount;
@property (T@"NSMutableDictionary",R,N,V__availableImageData) _availableImageData;
@property (T@"NSMutableDictionary",R,N,V__availablePixelBuffers) _availablePixelBuffers;
@property (T@"NSMutableSet",R,N,V__inFlightReadFrameIndexes) _inFlightReadFrameIndexes;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__synchronizationQueue) _synchronizationQueue;
@property (T@"NSOperationQueue",R,N,V__imageReadQueue) _imageReadQueue;
@property (T@"NSOperationQueue",R,N,V__imageDecodeQueue) _imageDecodeQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__movieWritingQueue) _movieWritingQueue;
@property (T@"AVAssetWriter",R,N,V__writer) _writer;
@property (T@"AVAssetWriterInput",R,N,V__videoInput) _videoInput;
@property (T@"AVAssetWriterInputPixelBufferAdaptor",R,N,V__pixelBufferAdaptor) _pixelBufferAdaptor;
@property (Tq,R,N,V__framesPerSecond) _framesPerSecond;
@property (Tq,R,N,V__nextWriteFileIndex) _nextWriteFileIndex;
@property (Tq,R,N,V__currentOutputFrameIndex) _currentOutputFrameIndex;
@property (T@?,R,C,N,V__completion) _completion;
@property (TB,N,GisSuspended,V_suspended) suspended;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTimelapseMovieWriter setSuspended:];
-[CAMTimelapseMovieWriter _reset];
-[CAMTimelapseMovieWriter observeValueForKeyPath:ofObject:change:context:];
-[CAMTimelapseMovieWriter isSuspended];
-[CAMTimelapseMovieWriter init];
-[CAMTimelapseMovieWriter _synchronizationQueue];
-[CAMTimelapseMovieWriter _desiredOutputSizeForFrameSize:];
-[CAMTimelapseMovieWriter _imageReadQueue];
-[CAMTimelapseMovieWriter writeMovieFromImageFiles:visMetadataFiles:startDate:location:outputPath:transform:framesPerSecond:preferHEVC:completionHandler:];
-[CAMTimelapseMovieWriter _frameFilePaths];
-[CAMTimelapseMovieWriter _writer];
-[CAMTimelapseMovieWriter _appendPixelBuffer:];
-[CAMTimelapseMovieWriter _availableImageData];
-[CAMTimelapseMovieWriter _availablePixelBuffers];
-[CAMTimelapseMovieWriter _completion];
-[CAMTimelapseMovieWriter _currentOutputFrameIndex];
-[CAMTimelapseMovieWriter _enqueueNextDecode];
-[CAMTimelapseMovieWriter _enqueueNextRead];
-[CAMTimelapseMovieWriter _enqueueNextWrite];
-[CAMTimelapseMovieWriter _finishMovieWithCompletionHandler:];
-[CAMTimelapseMovieWriter _framesPerSecond];
-[CAMTimelapseMovieWriter _imageDecodeQueue];
-[CAMTimelapseMovieWriter _inFlightReadFrameIndexes];
-[CAMTimelapseMovieWriter _movieWritingQueue];
-[CAMTimelapseMovieWriter _nextReadFileIndex];
-[CAMTimelapseMovieWriter _nextWriteFileIndex];
-[CAMTimelapseMovieWriter _pixelBufferAdaptor];
-[CAMTimelapseMovieWriter _residentImageDataCount];
-[CAMTimelapseMovieWriter _residentPixelBufferCount];
-[CAMTimelapseMovieWriter _setMetadataOnVideoTrackAssetWriterInput:];
-[CAMTimelapseMovieWriter _startWritingWithOutputPath:width:height:videoFormatDescription:transform:framesPerSecond:frameCount:preferHEVC:videoMetadata:];
-[CAMTimelapseMovieWriter _videoInput];
```
