# `AVMetricHLSMediaSegmentRequestEvent`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetricEvent`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _indexFileURL;
{_NSRange="location"Q"length"Q} _byteRange;
B _isMapSegment;
@"NSString" _mediaType;
d _segmentDuration;
@"AVMetricMediaResourceRequestEvent" _mediaResourceRequestEvent;
@"NSURL" _url;
```

## Properties

```
@property (T@"NSURL",R,V_url) url;
@property (TB,R) isMapSegment;
@property (T@"NSString",R) mediaType;
@property (T{_NSRange=QQ},R) byteRange;
@property (T@"NSURL",R) indexFileURL;
@property (Td,R) segmentDuration;
@property (T@"AVMetricMediaResourceRequestEvent",R) mediaResourceRequestEvent;
```

## Class methods

```
+[AVMetricHLSMediaSegmentRequestEvent supportsSecureCoding];
```

## Instance methods

```
-[AVMetricHLSMediaSegmentRequestEvent debugDescription];
-[AVMetricHLSMediaSegmentRequestEvent dealloc];
-[AVMetricHLSMediaSegmentRequestEvent encodeWithCoder:];
-[AVMetricHLSMediaSegmentRequestEvent initWithCoder:];
-[AVMetricHLSMediaSegmentRequestEvent mediaType];
-[AVMetricHLSMediaSegmentRequestEvent url];
-[AVMetricHLSMediaSegmentRequestEvent segmentDuration];
-[AVMetricHLSMediaSegmentRequestEvent byteRange];
-[AVMetricHLSMediaSegmentRequestEvent indexFileURL];
-[AVMetricHLSMediaSegmentRequestEvent initWithDate:mediaTime:sessionID:figMetricEvent:indexFileURL:byteRange:isMapSegment:mediaType:segmentDuration:mediaResourceRequestEvent:];
-[AVMetricHLSMediaSegmentRequestEvent isMapSegment];
-[AVMetricHLSMediaSegmentRequestEvent mediaResourceRequestEvent];
```
