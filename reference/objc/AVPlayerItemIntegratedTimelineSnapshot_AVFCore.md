# `AVPlayerItemIntegratedTimelineSnapshot`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{?="value"q"timescale"i"flags"I"epoch"q} _currentTime;
@"NSDate" _currentDate;
@"AVPlayerItemSegment" _currentSegment;
@"NSArray" _segments;
```

## Properties

```
@property (T{?=qiIq},R,N) duration;
@property (T@"AVPlayerItemSegment",R) currentSegment;
@property (T@"NSArray",R) segments;
@property (T{?=qiIq},R) currentTime;
@property (T@"NSDate",R) currentDate;
```

## Instance methods

```
-[AVPlayerItemIntegratedTimelineSnapshot segments];
-[AVPlayerItemIntegratedTimelineSnapshot currentDate];
-[AVPlayerItemIntegratedTimelineSnapshot dealloc];
-[AVPlayerItemIntegratedTimelineSnapshot currentTime];
-[AVPlayerItemIntegratedTimelineSnapshot duration];
-[AVPlayerItemIntegratedTimelineSnapshot copyWithZone:];
-[AVPlayerItemIntegratedTimelineSnapshot currentSegment];
-[AVPlayerItemIntegratedTimelineSnapshot initWithSegments:duration:currentTime:currentDate:currentSegment:];
-[AVPlayerItemIntegratedTimelineSnapshot mapTime:toSegment:atSegmentOffset:];
```
