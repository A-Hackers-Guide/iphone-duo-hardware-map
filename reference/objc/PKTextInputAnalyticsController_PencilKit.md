# `PKTextInputAnalyticsController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextInputSessionActionAnalyticsEndingObserver`
- 7 instance variables, 5 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
q _lastEventSource;
Q _lastEventSourceChangeTimestamp;
[9Q] _eventSourceUsage;
q _lastActivePencilType;
d _activePencilUsage;
@"NSTimer" _eventSourceTimer;
```

## Properties

```
@property (T@"NSTimer",&,N,V_eventSourceTimer) eventSourceTimer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputAnalyticsController sharedInstance];
+[PKTextInputAnalyticsController beginObservingSessionAnalytics];
```

## Instance methods

```
-[PKTextInputAnalyticsController init];
-[PKTextInputAnalyticsController dealloc];
-[PKTextInputAnalyticsController didBeginSession];
-[PKTextInputAnalyticsController didEndMatchingAccumulatorName:];
-[PKTextInputAnalyticsController matchingAccumulatorNames];
-[PKTextInputAnalyticsController _dispatchAnalytics];
-[PKTextInputAnalyticsController _dispatchPencilSettingsAnalytics];
-[PKTextInputAnalyticsController _setupAnalyticsTimer];
-[PKTextInputAnalyticsController _updateAnalyticsTracking];
-[PKTextInputAnalyticsController activePencilUsage:];
-[PKTextInputAnalyticsController configuredSystemActionBundleIdentifier];
-[PKTextInputAnalyticsController didUpdateToEventSource:];
-[PKTextInputAnalyticsController eventSourceDidChange:];
-[PKTextInputAnalyticsController eventSourceTimer];
-[PKTextInputAnalyticsController messageHandwritingAnalyticsWithProxyBlock:];
-[PKTextInputAnalyticsController q_didBeginSession];
-[PKTextInputAnalyticsController q_didEndMatchingAccumulatorName:inputMode:];
-[PKTextInputAnalyticsController setEventSourceTimer:];
```
