# `AVAssetSegmentTrackReport`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
i _trackID;
@"NSString" _mediaType;
{?="value"q"timescale"i"flags"I"epoch"q} _earliestPresentationTimeStamp;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
@"AVAssetSegmentReportSampleInformation" _firstVideoSampleInformation;
```

## Properties

```
@property (Ti,R,N,V_trackID) trackID;
@property (T@"NSString",R,N,V_mediaType) mediaType;
@property (T{?=qiIq},R,N,V_earliestPresentationTimeStamp) earliestPresentationTimeStamp;
@property (T{?=qiIq},R,N,V_duration) duration;
@property (T@"AVAssetSegmentReportSampleInformation",R,N,V_firstVideoSampleInformation) firstVideoSampleInformation;
```

## Instance methods

```
-[AVAssetSegmentTrackReport trackID];
-[AVAssetSegmentTrackReport dealloc];
-[AVAssetSegmentTrackReport duration];
-[AVAssetSegmentTrackReport mediaType];
-[AVAssetSegmentTrackReport earliestPresentationTimeStamp];
-[AVAssetSegmentTrackReport firstVideoSampleInformation];
-[AVAssetSegmentTrackReport initWithFigSegmentTrackReportDictionary:];
```
