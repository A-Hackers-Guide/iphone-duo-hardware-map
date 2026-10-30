# `AVAssetWriterFinishWritingHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetWriterHelper`
- 5 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _finishWritingOperations;
@"NSOperation" _transitionToTerminalStatusOperation;
^v _figAssetWriterCallbackContextToken;
^{OpaqueFigAssetWriter=} _figAssetWriter;
B _figAssetWriterIsRemote;
```

## Properties

```
@property (T@"NSOperation",R,N,V_transitionToTerminalStatusOperation) transitionToTerminalStatusOperation;
```

## Instance methods

```
-[AVAssetWriterFinishWritingHelper _isDefunct];
-[AVAssetWriterFinishWritingHelper dealloc];
-[AVAssetWriterFinishWritingHelper status];
-[AVAssetWriterFinishWritingHelper cancelWriting];
-[AVAssetWriterFinishWritingHelper _finishWritingOperationsDidFinish];
-[AVAssetWriterFinishWritingHelper initWithConfigurationState:finishWritingOperations:figAssetWriterCallbackContextToken:figAssetWriter:figAssetWriterIsRemote:];
-[AVAssetWriterFinishWritingHelper transitionToTerminalStatusOperation];
```
