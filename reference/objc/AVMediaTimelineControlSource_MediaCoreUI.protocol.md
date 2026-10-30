# `AVMediaTimelineControlSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](../userland/System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (Tf,R,N) minValue;
@property (Tf,R,N) maxValue;
@property (Tf,R,N) currentValue;
@property (TB,R,N,GisPlaying) playing;
@property (TB,R,N,GisLoading) loading;
@property (T@"NSString",R,N) currentValueText;
@property (T@"NSString",R,N) maxValueText;
@property (T@"NSArray",C,N) timeRangeMarks;
```

## Instance methods

```
-[AVMediaTimelineControlSource minValue];
-[AVMediaTimelineControlSource maxValue];
-[AVMediaTimelineControlSource timeRangeMarks];
-[AVMediaTimelineControlSource isPlaying];
-[AVMediaTimelineControlSource currentValue];
-[AVMediaTimelineControlSource isLoading];
-[AVMediaTimelineControlSource setTimeRangeMarks:];
-[AVMediaTimelineControlSource currentValueText];
-[AVMediaTimelineControlSource maxValueText];
```
