# `FigCaptureDisplayLayoutMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 11 instance variables, 9 properties, 16 instance methods, 4 class methods

## Instance variables

```
q _displayType;
^{OpaqueFigSimpleMutex=} _layoutObserversLock;
@"NSMutableArray" _layoutObservers;
^{OpaqueFigSimpleMutex=} _layoutLock;
B _displayConnected;
@"FigCaptureDisplayLayout" _layout;
@"NSArray" _elementIdentifiersToIgnore;
@"FBSDisplayLayoutMonitor" _layoutMonitor;
@"SBSExternalDisplayService" _externalDisplayService;
@"FigCaptureOSStateHandle" _osStateHandle;
B _isV68Device;
```

## Properties

```
@property (Tq,R,N,V_displayType) displayType;
@property (TB,R,N,GisDisplayConnected,V_displayConnected) displayConnected;
@property (T@"FigCaptureDisplayLayout",R,N) currentLayout;
@property (TB,R,N,GisOnHomeScreen) onHomeScreen;
@property (TB,R,N,GisOnLockScreen) onLockScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureDisplayLayoutMonitor initialize];
+[FigCaptureDisplayLayoutMonitor sharedContinuityDisplayLayoutMonitor];
+[FigCaptureDisplayLayoutMonitor sharedDisplayLayoutMonitor];
+[FigCaptureDisplayLayoutMonitor sharedExternalDisplayLayoutMonitor];
```

## Instance methods

```
-[FigCaptureDisplayLayoutMonitor osStatePropertyList];
-[FigCaptureDisplayLayoutMonitor isOnLockScreen];
-[FigCaptureDisplayLayoutMonitor isDisplayConnected];
-[FigCaptureDisplayLayoutMonitor displayType];
-[FigCaptureDisplayLayoutMonitor debugDescription];
-[FigCaptureDisplayLayoutMonitor initWithFBSDisplayLayoutMonitorCreateFunction:displayType:isV68Device:];
-[FigCaptureDisplayLayoutMonitor dealloc];
-[FigCaptureDisplayLayoutMonitor externalDisplayWillDisconnect:];
-[FigCaptureDisplayLayoutMonitor currentLayout];
-[FigCaptureDisplayLayoutMonitor removeLayoutObserver:];
-[FigCaptureDisplayLayoutMonitor externalDisplayDidConnect:];
-[FigCaptureDisplayLayoutMonitor isOnHomeScreen];
-[FigCaptureDisplayLayoutMonitor addLayoutObserver:];
-[FigCaptureDisplayLayoutMonitor description];
-[FigCaptureDisplayLayoutMonitor initWithFBSDisplayLayoutMonitorCreateFunction:displayType:];
-[FigCaptureDisplayLayoutMonitor addLayoutObserverWithoutImmediateCallback:];
```
