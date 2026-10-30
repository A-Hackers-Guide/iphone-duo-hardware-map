# `AVCaptureToggle`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 9 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSString" _localizedTitle;
@"NSString" _onSymbolName;
@"NSString" _offSymbolName;
B _on;
@"NSString" _accessibilityIdentifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"NSObject<OS_dispatch_queue>" _actionQueue;
@? _action;
@"CAMOverlayServiceToggle" _overlayControl;
```

## Properties

```
@property (T@?,C,N,V_action) action;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_actionQueue) actionQueue;
@property (TB,N,GisOn,V_on) on;
@property (T@"NSString",R,C,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",R,C,N,V_onSymbolName) onSymbolName;
@property (T@"NSString",R,C,N,V_offSymbolName) offSymbolName;
@property (T@"NSString",C,N,V_accessibilityIdentifier) accessibilityIdentifier;
```

## Class methods

```
+[AVCaptureToggle initialize];
```

## Instance methods

```
-[AVCaptureToggle localizedTitle];
-[AVCaptureToggle actionQueue];
-[AVCaptureToggle dealloc];
-[AVCaptureToggle enqueueActionWithUpdate:];
-[AVCaptureToggle setAction:];
-[AVCaptureToggle action];
-[AVCaptureToggle setAccessibilityIdentifier:];
-[AVCaptureToggle setActionQueue:];
-[AVCaptureToggle accessibilityIdentifier];
-[AVCaptureToggle overlayUpdate];
-[AVCaptureToggle setActionQueue:action:];
-[AVCaptureToggle setOn:];
-[AVCaptureToggle description];
-[AVCaptureToggle isOn];
-[AVCaptureToggle overlayControl];
-[AVCaptureToggle initWithLocalizedTitle:onSymbolName:offSymbolName:];
-[AVCaptureToggle offSymbolName];
-[AVCaptureToggle onSymbolName];
```
