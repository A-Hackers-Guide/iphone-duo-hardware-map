# `AVAssetWriterInputFigAssetWriterEndPassOperation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVOperation`
- 3 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigAssetWriter=} _figAssetWriter;
i _trackID;
@"AVAssetWriterInputPassDescription" _nextPassDescription;
```

## Properties

```
@property (T@"AVAssetWriterInputPassDescription",R,N,V_nextPassDescription) descriptionForNextPass;
```

## Instance methods

```
-[AVAssetWriterInputFigAssetWriterEndPassOperation init];
-[AVAssetWriterInputFigAssetWriterEndPassOperation isAsynchronous];
-[AVAssetWriterInputFigAssetWriterEndPassOperation dealloc];
-[AVAssetWriterInputFigAssetWriterEndPassOperation start];
-[AVAssetWriterInputFigAssetWriterEndPassOperation initWithFigAssetWriter:trackID:];
-[AVAssetWriterInputFigAssetWriterEndPassOperation _notifyWhetherMorePassesAreNeeded:timeRanges:forTrackWithID:];
-[AVAssetWriterInputFigAssetWriterEndPassOperation descriptionForNextPass];
```
