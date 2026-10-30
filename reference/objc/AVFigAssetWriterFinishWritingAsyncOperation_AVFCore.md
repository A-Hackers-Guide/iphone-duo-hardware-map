# `AVFigAssetWriterFinishWritingAsyncOperation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVOperation`
- Protocols: `AVAssetWriterFigAssetWriterNotificationHandlerDelegate`
- 2 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigAssetWriter=} _figAssetWriter;
@"AVAssetWriterFigAssetWriterNotificationHandler" _notificationHandler;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVFigAssetWriterFinishWritingAsyncOperation init];
-[AVFigAssetWriterFinishWritingAsyncOperation isAsynchronous];
-[AVFigAssetWriterFinishWritingAsyncOperation dealloc];
-[AVFigAssetWriterFinishWritingAsyncOperation start];
-[AVFigAssetWriterFinishWritingAsyncOperation cancel];
-[AVFigAssetWriterFinishWritingAsyncOperation didEnterTerminalState];
-[AVFigAssetWriterFinishWritingAsyncOperation didReceiveFigAssetWriterNotificationWithSuccess:error:];
-[AVFigAssetWriterFinishWritingAsyncOperation initWithFigAssetWriter:];
```
