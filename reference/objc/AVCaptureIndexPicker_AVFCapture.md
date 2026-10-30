# `AVCaptureIndexPicker`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 10 instance variables, 8 properties, 21 instance methods, 1 class methods

## Instance variables

```
q _selectedIndex;
q _numberOfIndexes;
@"NSString" _localizedTitle;
@"NSString" _symbolName;
@"NSString" _accessibilityIdentifier;
@"NSArray" _localizedIndexTitles;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"NSObject<OS_dispatch_queue>" _actionQueue;
@? _action;
@"CAMOverlayServicePicker" _overlayControl;
```

## Properties

```
@property (T@?,C,N,V_action) action;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_actionQueue) actionQueue;
@property (Tq,N,V_selectedIndex) selectedIndex;
@property (T@"NSString",R,C,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",R,C,N,V_symbolName) symbolName;
@property (Tq,R,N,V_numberOfIndexes) numberOfIndexes;
@property (T@"NSArray",R,C,N,V_localizedIndexTitles) localizedIndexTitles;
@property (T@"NSString",C,N,V_accessibilityIdentifier) accessibilityIdentifier;
```

## Class methods

```
+[AVCaptureIndexPicker initialize];
```

## Instance methods

```
-[AVCaptureIndexPicker localizedTitle];
-[AVCaptureIndexPicker selectedIndex];
-[AVCaptureIndexPicker symbolName];
-[AVCaptureIndexPicker actionQueue];
-[AVCaptureIndexPicker dealloc];
-[AVCaptureIndexPicker enqueueActionWithUpdate:];
-[AVCaptureIndexPicker setAction:];
-[AVCaptureIndexPicker action];
-[AVCaptureIndexPicker setAccessibilityIdentifier:];
-[AVCaptureIndexPicker setActionQueue:];
-[AVCaptureIndexPicker accessibilityIdentifier];
-[AVCaptureIndexPicker overlayUpdate];
-[AVCaptureIndexPicker setActionQueue:action:];
-[AVCaptureIndexPicker description];
-[AVCaptureIndexPicker setSelectedIndex:];
-[AVCaptureIndexPicker overlayControl];
-[AVCaptureIndexPicker numberOfIndexes];
-[AVCaptureIndexPicker initWithLocalizedTitle:symbolName:localizedIndexTitles:];
-[AVCaptureIndexPicker initWithLocalizedTitle:symbolName:numberOfIndexes:];
-[AVCaptureIndexPicker initWithLocalizedTitle:symbolName:numberOfIndexes:localizedTitleTransform:];
-[AVCaptureIndexPicker localizedIndexTitles];
```
