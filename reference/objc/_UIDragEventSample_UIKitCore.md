# `_UIDragEventSample`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isApplicationEnter;
B _isApplicationWithin;
B _isApplicationExit;
B _isPolicyDriven;
B _isDragEnd;
B _hasBeenDelivered;
I _windowServerHitTestContextID;
@"UIWindow" _window;
{CAPoint3D="x"d"y"d"z"d} _sceneLocation;
{CAPoint3D="x"d"y"d"z"d} _locationInWindow;
```

## Properties

```
@property (T@"UIWindow",R,N,V_window) window;
@property (T{CAPoint3D=ddd},R,N,V_sceneLocation) sceneLocation;
@property (T{CAPoint3D=ddd},R,N,V_locationInWindow) locationInWindow;
@property (TB,R,N,V_isApplicationEnter) isApplicationEnter;
@property (TB,R,N,V_isApplicationWithin) isApplicationWithin;
@property (TB,R,N,V_isApplicationExit) isApplicationExit;
@property (TB,R,N,V_isPolicyDriven) isPolicyDriven;
@property (TB,R,N,V_isDragEnd) isDragEnd;
@property (TI,R,N,V_windowServerHitTestContextID) windowServerHitTestContextID;
@property (TB,N,V_hasBeenDelivered) hasBeenDelivered;
```

## Class methods

```
+[_UIDragEventSample sampleFromHIDEvent:];
```

## Instance methods

```
-[_UIDragEventSample window];
-[_UIDragEventSample description];
-[_UIDragEventSample locationInWindow];
-[_UIDragEventSample copyWithSampleFlags:];
-[_UIDragEventSample hasBeenDelivered];
-[_UIDragEventSample hitTestWithEvent:];
-[_UIDragEventSample isApplicationEnter];
-[_UIDragEventSample isApplicationExit];
-[_UIDragEventSample isApplicationWithin];
-[_UIDragEventSample isDragEnd];
-[_UIDragEventSample isPolicyDriven];
-[_UIDragEventSample sampleFlags];
-[_UIDragEventSample sceneLocation];
-[_UIDragEventSample setHasBeenDelivered:];
-[_UIDragEventSample windowServerHitTestContextID];
```
