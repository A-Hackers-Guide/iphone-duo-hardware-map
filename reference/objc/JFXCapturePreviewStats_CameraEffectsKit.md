# `JFXCapturePreviewStats`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"JFXCapturePreviewFrameStats" _runningAverage;
@"NSMutableArray" _stats;
@"NSObject<OS_dispatch_queue>" _q;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
```

## Instance methods

```
-[JFXCapturePreviewStats clear];
-[JFXCapturePreviewStats init];
-[JFXCapturePreviewStats add:];
-[JFXCapturePreviewStats setName:];
-[JFXCapturePreviewStats name];
-[JFXCapturePreviewStats print];
-[JFXCapturePreviewStats runningAverage];
-[JFXCapturePreviewStats _print_NoLock];
-[JFXCapturePreviewStats printSync];
```
