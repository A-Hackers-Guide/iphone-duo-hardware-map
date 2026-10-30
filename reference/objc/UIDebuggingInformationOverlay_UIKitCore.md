# `UIDebuggingInformationOverlay`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindow`
- Protocols: `UISplitViewControllerDelegate`
- 7 instance variables, 9 properties, 23 instance methods, 2 class methods

## Instance variables

```
B _isFullscreen;
B _checkingTouches;
B _touchCaptureEnabled;
@"NSMutableArray" _touchObservers;
@"UIWindow" _inspectedWindow;
@"UIEvent" _lastTouch;
{CGPoint="x"d"y"d} _drawingOrigin;
```

## Properties

```
@property (T@"UIEvent",&,N,V_lastTouch) lastTouch;
@property (T{CGPoint=dd},N,V_drawingOrigin) drawingOrigin;
@property (TB,N,V_isFullscreen) isFullscreen;
@property (T@"UIDebuggingInformationOverlayViewController",R,N) overlayViewController;
@property (T@"UIDebuggingInformationRootTableViewController",&,N) rootTableViewController;
@property (TB,N,V_checkingTouches) checkingTouches;
@property (TB,N,V_touchCaptureEnabled) touchCaptureEnabled;
@property (T@"NSMutableArray",&,N,V_touchObservers) touchObservers;
@property (T@"UIWindow",&,N,V_inspectedWindow) inspectedWindow;
```

## Class methods

```
+[UIDebuggingInformationOverlay overlay];
+[UIDebuggingInformationOverlay prepareDebuggingOverlay];
```

## Instance methods

```
-[UIDebuggingInformationOverlay init];
-[UIDebuggingInformationOverlay isFullscreen];
-[UIDebuggingInformationOverlay hitTest:withEvent:];
-[UIDebuggingInformationOverlay _setHidden:];
-[UIDebuggingInformationOverlay initWithFrame:];
-[UIDebuggingInformationOverlay checkingTouches];
-[UIDebuggingInformationOverlay inspectedWindow];
-[UIDebuggingInformationOverlay drawingOrigin];
-[UIDebuggingInformationOverlay lastTouch];
-[UIDebuggingInformationOverlay overlayViewController];
-[UIDebuggingInformationOverlay rootTableViewController];
-[UIDebuggingInformationOverlay setCheckingTouches:];
-[UIDebuggingInformationOverlay setDrawingOrigin:];
-[UIDebuggingInformationOverlay setInspectedWindow:];
-[UIDebuggingInformationOverlay setIsFullscreen:];
-[UIDebuggingInformationOverlay setLastTouch:];
-[UIDebuggingInformationOverlay setRootTableViewController:];
-[UIDebuggingInformationOverlay setTouchCaptureEnabled:];
-[UIDebuggingInformationOverlay setTouchObservers:];
-[UIDebuggingInformationOverlay toggleFullscreen];
-[UIDebuggingInformationOverlay toggleVisibility];
-[UIDebuggingInformationOverlay touchCaptureEnabled];
-[UIDebuggingInformationOverlay touchObservers];
```
