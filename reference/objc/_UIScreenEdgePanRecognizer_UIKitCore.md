# `_UIScreenEdgePanRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 12 properties, 32 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _screenBounds;
B _shouldUseGrapeFlags;
B _hasRecordedData;
B _hasDoneInitialBackProjectionTest;
{CGPoint="x"d"y"d} _initialTouchLocation;
d _initialTouchTimestamp;
q _initialInterfaceOrientation;
Q _touchedRegion;
@"UIDelayedAction" _recognitionTimer;
{CGPoint="x"d"y"d} _lastTouchLocation;
d _lastTouchTimestamp;
q _lastTouchModifier;
q _type;
B _requiresFlatThumb;
B _recognizeAlongEdge;
@"_UIScreenEdgePanRecognizerSettings" _settings;
Q _targetEdges;
q _state;
Q _recognizedRegion;
@"<_UIScreenEdgePanRecognizerDelegate>" _delegate;
```

## Properties

```
@property (T@"_UIScreenEdgePanRecognizerSettings",&,N,V_settings) settings;
@property (TB,R,N,V_hasRecordedData) hasRecordedData;
@property (TB,R,N) useGrapeFlags;
@property (TB,N,V_shouldUseGrapeFlags) shouldUseGrapeFlags;
@property (T{CGPoint=dd},R,N,V_lastTouchLocation) _lastTouchLocation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_screenBounds) screenBounds;
@property (TQ,N,V_targetEdges) targetEdges;
@property (TB,N,V_requiresFlatThumb) requiresFlatThumb;
@property (TB,N,V_recognizeAlongEdge) recognizeAlongEdge;
@property (Tq,R,N,V_state) state;
@property (TQ,R,N,V_recognizedRegion) recognizedRegion;
@property (T@"<_UIScreenEdgePanRecognizerDelegate>",V_delegate) delegate;
```

## Instance methods

```
-[_UIScreenEdgePanRecognizer _type];
-[_UIScreenEdgePanRecognizer recognizeAlongEdge];
-[_UIScreenEdgePanRecognizer _setState:];
-[_UIScreenEdgePanRecognizer setRecognizeAlongEdge:];
-[_UIScreenEdgePanRecognizer setSettings:];
-[_UIScreenEdgePanRecognizer settings];
-[_UIScreenEdgePanRecognizer initWithType:];
-[_UIScreenEdgePanRecognizer dealloc];
-[_UIScreenEdgePanRecognizer reset];
-[_UIScreenEdgePanRecognizer setTargetEdges:];
-[_UIScreenEdgePanRecognizer setDelegate:];
-[_UIScreenEdgePanRecognizer delegate];
-[_UIScreenEdgePanRecognizer targetEdges];
-[_UIScreenEdgePanRecognizer screenBounds];
-[_UIScreenEdgePanRecognizer state];
-[_UIScreenEdgePanRecognizer hasRecordedData];
-[_UIScreenEdgePanRecognizer _idleTimerElapsed:];
-[_UIScreenEdgePanRecognizer _incorporateIncrementalSampleAtLocation:timestamp:modifier:region:interfaceOrientation:forceState:];
-[_UIScreenEdgePanRecognizer _incorporateInitialTouchAtLocation:timestamp:modifier:region:interfaceOrientation:forceState:];
-[_UIScreenEdgePanRecognizer _lastTouchLocation];
-[_UIScreenEdgePanRecognizer _longPressTimerElapsed:];
-[_UIScreenEdgePanRecognizer _targetEdges];
-[_UIScreenEdgePanRecognizer incorporateTouchSampleAtLocation:timestamp:modifier:region:interfaceOrientation:forceState:];
-[_UIScreenEdgePanRecognizer initWithType:settings:];
-[_UIScreenEdgePanRecognizer recognizedRegion];
-[_UIScreenEdgePanRecognizer requiresFlatThumb];
-[_UIScreenEdgePanRecognizer setRequiresFlatThumb:];
-[_UIScreenEdgePanRecognizer setScreenBounds:];
-[_UIScreenEdgePanRecognizer setShouldUseGrapeFlags:];
-[_UIScreenEdgePanRecognizer shouldUseGrapeFlags];
-[_UIScreenEdgePanRecognizer touchedEdgesForInterfaceOrientation:];
-[_UIScreenEdgePanRecognizer useGrapeFlags];
```
