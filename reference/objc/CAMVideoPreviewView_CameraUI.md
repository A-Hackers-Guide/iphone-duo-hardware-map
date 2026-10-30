# `CAMVideoPreviewView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _square;
@"AVCaptureVideoPreviewLayer" _videoPreviewLayer;
@"UIView" _previewLayerView;
q _previewViewAspectMode;
q _previewViewAspectModeWindowed;
```

## Properties

```
@property (T@"AVCaptureVideoPreviewLayer",&,N,V_videoPreviewLayer) videoPreviewLayer;
@property (T@"UIView",R,N,V_previewLayerView) previewLayerView;
@property (Tq,N,V_previewViewAspectMode) previewViewAspectMode;
@property (Tq,N,V_previewViewAspectModeWindowed) previewViewAspectModeWindowed;
@property (TB,R,N) previewViewWindowIsFullScreen;
@property (TB,N,GisSquare,V_square) square;
```

## Instance methods

```
-[CAMVideoPreviewView setVideoPreviewLayer:];
-[CAMVideoPreviewView isSquare];
-[CAMVideoPreviewView previewViewAspectMode];
-[CAMVideoPreviewView dealloc];
-[CAMVideoPreviewView layoutSubviews];
-[CAMVideoPreviewView previewViewAspectModeWindowed];
-[CAMVideoPreviewView videoPreviewLayer];
-[CAMVideoPreviewView _modeForCurrentWindowSize];
-[CAMVideoPreviewView _frameForSubviewsAccountForSquare:];
-[CAMVideoPreviewView setPreviewViewAspectModeWindowed:];
-[CAMVideoPreviewView previewViewWindowIsFullScreen];
-[CAMVideoPreviewView setSquare:animated:];
-[CAMVideoPreviewView setPreviewViewAspectMode:];
-[CAMVideoPreviewView _updateAspectModeForSublayers];
-[CAMVideoPreviewView previewLayerView];
-[CAMVideoPreviewView setSquare:];
-[CAMVideoPreviewView initWithFrame:];
```
