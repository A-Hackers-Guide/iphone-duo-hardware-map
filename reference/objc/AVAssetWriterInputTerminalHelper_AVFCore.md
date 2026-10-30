# `AVAssetWriterInputTerminalHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetWriterInputHelper`
- Protocols: `AVAssetWriterInputMediaDataRequesterDelegate`
- 2 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _terminalStatus;
B _didRequestMediaDataOnce;
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
-[AVAssetWriterInputTerminalHelper isReadyForMoreMediaData];
-[AVAssetWriterInputTerminalHelper stopRequestingMediaData];
-[AVAssetWriterInputTerminalHelper requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVAssetWriterInputTerminalHelper status];
-[AVAssetWriterInputTerminalHelper appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInputTerminalHelper markAsFinished];
-[AVAssetWriterInputTerminalHelper appendCaption:error:];
-[AVAssetWriterInputTerminalHelper appendCaptionGroup:error:];
-[AVAssetWriterInputTerminalHelper appendSampleBuffer:error:];
-[AVAssetWriterInputTerminalHelper appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInputTerminalHelper canStartRespondingToEachPassDescriptionReturningReason:];
-[AVAssetWriterInputTerminalHelper initWithConfigurationState:];
-[AVAssetWriterInputTerminalHelper initWithConfigurationState:terminalStatus:];
-[AVAssetWriterInputTerminalHelper markCurrentPassAsFinished];
-[AVAssetWriterInputTerminalHelper mediaDataRequesterShouldRequestMediaData];
-[AVAssetWriterInputTerminalHelper requestMediaDataOnceIfNecessaryWithMediaDataRequester:];
-[AVAssetWriterInputTerminalHelper transitionToAndReturnTerminalHelperWithTerminalStatus:];
```
