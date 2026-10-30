# `UIEventSessionActionAnalytics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 2 properties, 39 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"_UIEventSessionAction" _lastAction;
@"NSMutableSet" _accumulators;
Q _maxDepth;
@"UIEventSessionTouchEventAnalyzer" touchAnalyzer;
@"UIEventSessionHeatMapAnalyzer" heatMapAnalyzer;
q _magicKeyboardState;
q _lastMagicKeyboardState;
q _hardwareKeyboardState;
q _lastHardwareKeyboardState;
q _uiInterfaceOrientation;
q _lastUIInterfaceOrientation;
B _needToFlushUIEventSessionActionAnalytics;
B _pencilIsHovering;
@"NSNumber" _sessionID;
@"NSString" _bundleID;
```

## Properties

```
@property (T@"NSNumber",&,N,V_sessionID) sessionID;
@property (T@"NSString",R,N,V_bundleID) bundleID;
```

## Class methods

```
+[UIEventSessionActionAnalytics sharedInstance];
```

## Instance methods

```
-[UIEventSessionActionAnalytics sessionID];
-[UIEventSessionActionAnalytics setSessionID:];
-[UIEventSessionActionAnalytics init];
-[UIEventSessionActionAnalytics bundleID];
-[UIEventSessionActionAnalytics didHardwareConfigurationChange:];
-[UIEventSessionActionAnalytics didTouch:withLocationInWindow:withWindowBounds:withWindowFrameInScreen:withTrackpadFingerDownCount:withSystemDisplayIdentifier:];
-[UIEventSessionActionAnalytics addAccumulator:];
-[UIEventSessionActionAnalytics _instanceOfActionClass:source:];
-[UIEventSessionActionAnalytics _setPencilIsHoveringTo:];
-[UIEventSessionActionAnalytics allAccumulatorNames];
-[UIEventSessionActionAnalytics checkForUIEventSessionActionAnalytics:forWindow:isFrontBoard:isFrontBoardTransitioningToForeground:];
-[UIEventSessionActionAnalytics didKeyboardShortcut:];
-[UIEventSessionActionAnalytics didPencilDoubleTap];
-[UIEventSessionActionAnalytics didPencilHover:withPhase:];
-[UIEventSessionActionAnalytics didPencilSqueezeWithPhase:];
-[UIEventSessionActionAnalytics didPointerClick:withLocationInWindow:withWindowBounds:];
-[UIEventSessionActionAnalytics didPointerHover:withLocationInWindow:withWindowBounds:];
-[UIEventSessionActionAnalytics didScroll:withSource:];
-[UIEventSessionActionAnalytics didShowContextualMenuFromLocation:withSource:];
-[UIEventSessionActionAnalytics didTap:withSource:];
-[UIEventSessionActionAnalytics didTextSelectionWithSource:];
-[UIEventSessionActionAnalytics didTypingWithSource:];
-[UIEventSessionActionAnalytics getAIDState];
-[UIEventSessionActionAnalytics q_addAccumulator:];
-[UIEventSessionActionAnalytics q_addActionAndUpdate:];
-[UIEventSessionActionAnalytics q_enumerateAnalytics:];
-[UIEventSessionActionAnalytics q_flushRecentActions];
-[UIEventSessionActionAnalytics q_setupDefaultAnalytics];
-[UIEventSessionActionAnalytics q_updateAnalyticsFromAccumulators];
-[UIEventSessionActionAnalytics q_updateHardwareState];
-[UIEventSessionActionAnalytics q_updateUIInterfaceOrientation];
-[UIEventSessionActionAnalytics q_writeAnalytics];
-[UIEventSessionActionAnalytics resetSessionID];
-[UIEventSessionActionAnalytics shouldEnableTouchHeatMapAnalyzer];
-[UIEventSessionActionAnalytics updateAIDState];
-[UIEventSessionActionAnalytics updateHardwareKeyboardState];
-[UIEventSessionActionAnalytics updateUIInterfaceOrientation];
-[UIEventSessionActionAnalytics writeAnalytics];
-[UIEventSessionActionAnalytics writeEventWithFields:andName:];
```
