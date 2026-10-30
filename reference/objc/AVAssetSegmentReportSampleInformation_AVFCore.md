# `AVAssetSegmentReportSampleInformation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _presentationTimeStamp;
q _offset;
q _length;
B _isSyncSample;
```

## Properties

```
@property (T{?=qiIq},R,N,V_presentationTimeStamp) presentationTimeStamp;
@property (Tq,R,N,V_offset) offset;
@property (Tq,R,N,V_length) length;
@property (TB,R,N,V_isSyncSample) isSyncSample;
```

## Instance methods

```
-[AVAssetSegmentReportSampleInformation dealloc];
-[AVAssetSegmentReportSampleInformation presentationTimeStamp];
-[AVAssetSegmentReportSampleInformation length];
-[AVAssetSegmentReportSampleInformation offset];
-[AVAssetSegmentReportSampleInformation initWithFigSegmentReportSampleInformationDictionary:];
-[AVAssetSegmentReportSampleInformation isSyncSample];
```
