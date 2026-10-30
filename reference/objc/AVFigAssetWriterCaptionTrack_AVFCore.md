# `AVFigAssetWriterCaptionTrack`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVFigAssetWriterTrack`
- 3 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"AVCaptionGrouper" _captionGrouper;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _previousCaptionTimeRange;
{?="value"q"timescale"i"flags"I"epoch"q} _nextGroupStartTime;
```

## Instance methods

```
-[AVFigAssetWriterCaptionTrack dealloc];
-[AVFigAssetWriterCaptionTrack _attachToFigAssetWriterUsingFormatSpecification:sourcePixelBufferAttributes:multiPass:error:];
-[AVFigAssetWriterCaptionTrack addCaption:error:];
-[AVFigAssetWriterCaptionTrack addCaptionGroup:error:];
-[AVFigAssetWriterCaptionTrack addCaptionGroupAsSampleBuffer:error:];
-[AVFigAssetWriterCaptionTrack addSampleBuffer:error:];
-[AVFigAssetWriterCaptionTrack flushCaptionsUntilTime:error:];
-[AVFigAssetWriterCaptionTrack flushCaptionsWithError:];
-[AVFigAssetWriterCaptionTrack markEndOfDataReturningError:];
-[AVFigAssetWriterCaptionTrack prepareToEndSession];
```
