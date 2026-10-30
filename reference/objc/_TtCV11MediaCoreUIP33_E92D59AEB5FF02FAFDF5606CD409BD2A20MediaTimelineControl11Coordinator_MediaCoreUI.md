# `_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator`

- Image: [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](../userland/System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVMediaTimelineControlSource`, `AVTimeRangeMarkUIProvider`, `AVMediaTimelineControlDelegate`
- 14 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
f maxValue;
f currentValue;
? timeRangeMarks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 viewModel;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 timelineControl;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 markers;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 scrubState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 seekUpdateLink;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 seekAnimationFromPosition;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 seekAnimationStartDate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 animatedSeekPosition;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 contrast;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isDisabled;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 markerGesture;
```

## Properties

```
@property (Tf,N,R) minValue;
@property (Tf,N,VmaxValue) maxValue;
@property (Tf,N,VcurrentValue) currentValue;
@property (TB,N,R) playing;
@property (TB,N,R) loading;
@property (T@"NSString",N,R) currentValueText;
@property (T@"NSString",N,R) maxValueText;
@property (T@"NSArray",N,C) timeRangeMarks;
```

## Instance methods

```
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator minValue];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator maxValue];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator init];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator timeRangeMarks];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator dealloc];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator isPlaying];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator currentValue];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator setCurrentValue:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator isLoading];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator setMaxValue:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator setTimeRangeMarks:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator mediaTimelineControl:didChangeValue:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator mediaTimelineControlDidEndChanging:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator mediaTimelineControlWillBeginChanging:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator currentValueText];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator maxValueText];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator mediaTimelineControl:didChangeScrubbingRate:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator mediaTimelineControl:didExtendWithInsets:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator mediaTimelineControlDidEndDecelerating:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator timeRangeMark:sizeInFrame:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator uiProxyForTimeRangeMark:withSource:];
-[_TtCV11MediaCoreUIP33_E92D59AEB5FF02FAFDF5606CD409BD2A20MediaTimelineControl11Coordinator handleMarkerGesture:];
```
