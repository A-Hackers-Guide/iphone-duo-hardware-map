# `AUAppleViewControllerBase`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 9 instance variables, 3 properties, 26 instance methods, 2 class methods

## Instance variables

```
^{AUListenerBase=} eventListener;
d lastRenderedSampleTime;
B auRendering;
B initialized;
B _needsRealtimeDrawing;
^{OpaqueAudioComponentInstance=} AU;
@"NSArray" topLevelObjects;
d _realtimeDrawingInterval;
@"UIColor" _tintColor;
```

## Properties

```
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (TB,V_needsRealtimeDrawing) needsRealtimeDrawing;
@property (Td,V_realtimeDrawingInterval) realtimeDrawingInterval;
```

## Class methods

```
+[AUAppleViewControllerBase getLocalizedString:];
+[AUAppleViewControllerBase customViewLogger];
```

## Instance methods

```
-[AUAppleViewControllerBase cleanup];
-[AUAppleViewControllerBase viewWillDisappear:];
-[AUAppleViewControllerBase viewDidLoad];
-[AUAppleViewControllerBase viewWillAppear:];
-[AUAppleViewControllerBase setTintColor:];
-[AUAppleViewControllerBase tintColor];
-[AUAppleViewControllerBase priv_eventListener:event:value:];
-[AUAppleViewControllerBase au];
-[AUAppleViewControllerBase doRealtimeDrawing];
-[AUAppleViewControllerBase getParameterInfo:scope:];
-[AUAppleViewControllerBase handleBeginGesture:];
-[AUAppleViewControllerBase handleEndGesture:];
-[AUAppleViewControllerBase handleParameterListChanged];
-[AUAppleViewControllerBase needsRealtimeDrawing];
-[AUAppleViewControllerBase postBeginGestureNotificationForParameter:];
-[AUAppleViewControllerBase postEndGestureNotificationForParameter:];
-[AUAppleViewControllerBase prepareData];
-[AUAppleViewControllerBase priv_addListenerForParameter:scope:element:];
-[AUAppleViewControllerBase priv_removeListenerForParameter:scope:element:];
-[AUAppleViewControllerBase priv_removeListeners];
-[AUAppleViewControllerBase realtimeDrawingInterval];
-[AUAppleViewControllerBase registerParameters];
-[AUAppleViewControllerBase setAU:];
-[AUAppleViewControllerBase setNeedsRealtimeDrawing:];
-[AUAppleViewControllerBase setRealtimeDrawingInterval:];
-[AUAppleViewControllerBase synchronizeUIWithParameterValues];
```
