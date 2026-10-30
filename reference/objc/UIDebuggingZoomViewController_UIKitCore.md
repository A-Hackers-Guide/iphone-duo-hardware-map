# `UIDebuggingZoomViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIDebuggingZoomDelegate`, `UIDebuggingInformationViewController`
- 12 instance variables, 12 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _useViewForEdges;
Q _currentDirection;
@"UIDebuggingZoomLoupeView" _loupe;
@"UIDebuggingZoomLineView" _lineView;
@"UIPanGestureRecognizer" _pan;
@"NSObject<OS_dispatch_group>" _group;
@"NSObject<OS_dispatch_queue>" _queue;
^{CGImage=} _image;
@"UILabel" _label;
@"UILabel" _distanceLabel;
@"UISegmentedControl" _directionSegmentedControl;
@"UIView" _lastViewSeen;
```

## Properties

```
@property (TQ,N,V_currentDirection) currentDirection;
@property (T@"UIDebuggingZoomLoupeView",&,N,V_loupe) loupe;
@property (T@"UIDebuggingZoomLineView",&,N,V_lineView) lineView;
@property (T@"UIPanGestureRecognizer",&,N,V_pan) pan;
@property (T@"NSObject<OS_dispatch_group>",&,N,V_group) group;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T^{CGImage=},N,V_image) image;
@property (T@"UILabel",&,N,V_label) label;
@property (T@"UILabel",&,N,V_distanceLabel) distanceLabel;
@property (T@"UISegmentedControl",&,N,V_directionSegmentedControl) directionSegmentedControl;
@property (TB,N,V_useViewForEdges) useViewForEdges;
@property (T@"UIView",&,N,V_lastViewSeen) lastViewSeen;
```

## Instance methods

```
-[UIDebuggingZoomViewController pan];
-[UIDebuggingZoomViewController setGroup:];
-[UIDebuggingZoomViewController viewWillDisappear:];
-[UIDebuggingZoomViewController label];
-[UIDebuggingZoomViewController setLabel:];
-[UIDebuggingZoomViewController dealloc];
-[UIDebuggingZoomViewController group];
-[UIDebuggingZoomViewController setLoupe:];
-[UIDebuggingZoomViewController viewDidLoad];
-[UIDebuggingZoomViewController queue];
-[UIDebuggingZoomViewController initWithNibName:bundle:];
-[UIDebuggingZoomViewController viewDidAppear:];
-[UIDebuggingZoomViewController lineView];
-[UIDebuggingZoomViewController image];
-[UIDebuggingZoomViewController loupe];
-[UIDebuggingZoomViewController setPan:];
-[UIDebuggingZoomViewController setQueue:];
-[UIDebuggingZoomViewController setImage:];
-[UIDebuggingZoomViewController useViewForEdges];
-[UIDebuggingZoomViewController currentDirection];
-[UIDebuggingZoomViewController directionSegmentedControl];
-[UIDebuggingZoomViewController distanceLabel];
-[UIDebuggingZoomViewController drawLinesAtPoint:];
-[UIDebuggingZoomViewController drawViewLinesAtPoint:forView:];
-[UIDebuggingZoomViewController lastViewSeen];
-[UIDebuggingZoomViewController newCaptureSnapshotAtRect:window:];
-[UIDebuggingZoomViewController setCurrentDirection:];
-[UIDebuggingZoomViewController setDirectionSegmentedControl:];
-[UIDebuggingZoomViewController setDistanceLabel:];
-[UIDebuggingZoomViewController setLastViewSeen:];
-[UIDebuggingZoomViewController setLineView:];
-[UIDebuggingZoomViewController setUseViewForEdges:];
-[UIDebuggingZoomViewController toggleDirection:];
-[UIDebuggingZoomViewController toggleMeasuring:];
-[UIDebuggingZoomViewController toggleMode:];
-[UIDebuggingZoomViewController updateGesture:];
```
