# `SRHMediaEventsCollector`

- Image: [`/System/Library/PrivateFrameworks/SensorKitHelper.framework/SensorKitHelper`](../userland/System__Library__PrivateFrameworks__SensorKitHelper.framework__SensorKitHelper.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIScrollViewMonitorDelegate`
- 3 instance variables, 0 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"UIScrollViewMonitor" _scrollViewMonitor;
@"SRHMediaViewsStore" _mediaViewsStore;
```

## Class methods

```
+[SRHMediaEventsCollector initialize];
```

## Instance methods

```
-[SRHMediaEventsCollector didBecomeActive];
-[SRHMediaEventsCollector willResignActive];
-[SRHMediaEventsCollector dealloc];
-[SRHMediaEventsCollector initWithScrollView:scrollMonitor:];
-[SRHMediaEventsCollector scrollViewMonitorDidStartMonitoring:];
-[SRHMediaEventsCollector scrollViewMonitorDidStopMonitoring:];
-[SRHMediaEventsCollector scrollViewMonitorScrollDid:addView:removeView:];
-[SRHMediaEventsCollector scrollViewMonitorScrollDidScrolled:];
-[SRHMediaEventsCollector _addMediaSubviewsOfView:];
-[SRHMediaEventsCollector _checkViewForMediaContent:withCompletionHandler:];
-[SRHMediaEventsCollector _addMediaSubviewsOfView:viewsTraversed:];
-[SRHMediaEventsCollector _removeMediaSubviewsOfView:];
-[SRHMediaEventsCollector _removeMediaSubviewsOfView:viewsTraversed:];
-[SRHMediaEventsCollector initWithScrollView:scrollMonitor:mediaViewsStore:];
```
