# `_UIMotionAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UIMotionAnalyzerSettings" _settings;
@"_UIViewerRelativeDevicePose" _viewerRelativeDevicePose;
```

## Properties

```
@property (T@"_UIMotionAnalyzerSettings",R,N,V_settings) settings;
@property (T@"_UIViewerRelativeDevicePose",R,N,V_viewerRelativeDevicePose) viewerRelativeDevicePose;
```

## Instance methods

```
-[_UIMotionAnalyzer init];
-[_UIMotionAnalyzer settings];
-[_UIMotionAnalyzer reset];
-[_UIMotionAnalyzer updateHistory];
-[_UIMotionAnalyzer applyHysteresisWithReceivedEventTimestamp:timeSinceLastNewMotionEvent:slowUpdatesEnabled:returningShouldToggleSlowUpdates:logger:];
-[_UIMotionAnalyzer description];
-[_UIMotionAnalyzer updateWithEvent:];
-[_UIMotionAnalyzer resetHysteresis];
-[_UIMotionAnalyzer initWithSettings:];
-[_UIMotionAnalyzer viewerRelativeDevicePose];
```
