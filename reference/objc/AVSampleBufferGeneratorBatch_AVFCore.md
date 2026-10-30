# `AVSampleBufferGeneratorBatch`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"AVSampleBufferGenerator" _sampleGenerator;
^{OpaqueFigSampleGeneratorBatch=} _sampleGeneratorBatch;
B _openToRequests;
^{OpaqueFigSimpleMutex=} _stateMutex;
@? _completionHandler;
```

## Properties

```
@property (T@"AVSampleBufferGenerator",R,N) _generator;
```

## Class methods

```
+[AVSampleBufferGeneratorBatch initialize];
```

## Instance methods

```
-[AVSampleBufferGeneratorBatch _generator];
-[AVSampleBufferGeneratorBatch init];
-[AVSampleBufferGeneratorBatch dealloc];
-[AVSampleBufferGeneratorBatch _completionHandler];
-[AVSampleBufferGeneratorBatch cancel];
-[AVSampleBufferGeneratorBatch initWithGenerator:];
-[AVSampleBufferGeneratorBatch createAndAddSampleBufferForRequest:error:];
-[AVSampleBufferGeneratorBatch isOpenToRequests];
-[AVSampleBufferGeneratorBatch makeDataReadyWithCompletionHandler:];
```
