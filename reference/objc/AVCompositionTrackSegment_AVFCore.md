# `AVCompositionTrackSegment`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetTrackSegment`
- Protocols: `NSSecureCoding`
- 1 instance variables, 3 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"AVCompositionTrackSegmentInternal" _priv;
```

## Properties

```
@property (TB,R,N,GisEmpty) empty;
@property (T@"NSURL",R,N) sourceURL;
@property (Ti,R,N) sourceTrackID;
```

## Class methods

```
+[AVCompositionTrackSegment supportsSecureCoding];
+[AVCompositionTrackSegment compositionTrackSegmentWithTimeRange:];
+[AVCompositionTrackSegment compositionTrackSegmentWithURL:trackID:sourceTimeRange:targetTimeRange:];
```

## Instance methods

```
-[AVCompositionTrackSegment sourceURL];
-[AVCompositionTrackSegment init];
-[AVCompositionTrackSegment dealloc];
-[AVCompositionTrackSegment isEmpty];
-[AVCompositionTrackSegment encodeWithCoder:];
-[AVCompositionTrackSegment hash];
-[AVCompositionTrackSegment description];
-[AVCompositionTrackSegment initWithCoder:];
-[AVCompositionTrackSegment isEqual:];
-[AVCompositionTrackSegment _initWithTimeMapping:];
-[AVCompositionTrackSegment initWithTimeRange:];
-[AVCompositionTrackSegment initWithURL:trackID:sourceTimeRange:targetTimeRange:];
-[AVCompositionTrackSegment sourceTrackID];
```
