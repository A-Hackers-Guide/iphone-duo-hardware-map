# `AVCaptureSystemStylePicker`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 11 instance variables, 0 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _sessionReference;
@"NSArray" _styles;
@? _action;
@"NSArray" _titles;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _selectedStyleLock;
@"AVCaptureSmartStyle" _selectedStyle;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"CAMOverlayServicePicker" _overlayControl;
B _observing;
B _changeSmartStyleInProcess;
B _smartStyleHasChanged;
```

## Class methods

```
+[AVCaptureSystemStylePicker initialize];
```

## Instance methods

```
-[AVCaptureSystemStylePicker initWithSession:styles:action:];
-[AVCaptureSystemStylePicker observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureSystemStylePicker installObservers];
-[AVCaptureSystemStylePicker actionQueue];
-[AVCaptureSystemStylePicker dealloc];
-[AVCaptureSystemStylePicker enqueueActionWithUpdate:];
-[AVCaptureSystemStylePicker initWithSession:action:];
-[AVCaptureSystemStylePicker _automaticStylesWithSystemSmartStyle:];
-[AVCaptureSystemStylePicker overlayUpdate];
-[AVCaptureSystemStylePicker removeObservers];
-[AVCaptureSystemStylePicker initWithSession:];
-[AVCaptureSystemStylePicker overlayControl];
-[AVCaptureSystemStylePicker overlayVisibilityDidChange:];
```
