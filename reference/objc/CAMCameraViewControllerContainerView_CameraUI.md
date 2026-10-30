# `CAMCameraViewControllerContainerView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"UIView" _viewfinderView;
@"UIView" _customOverlayView;
@"UIView" _additionalContentView;
```

## Properties

```
@property (T@"UIView",&,N,V_viewfinderView) viewfinderView;
@property (T@"UIView",&,N,V_customOverlayView) customOverlayView;
@property (T@"UIView",&,N,V_additionalContentView) additionalContentView;
```

## Class methods

```
+[CAMCameraViewControllerContainerView layerClass];
```

## Instance methods

```
-[CAMCameraViewControllerContainerView systemLayoutSizeFittingSize:];
-[CAMCameraViewControllerContainerView layoutSubviews];
-[CAMCameraViewControllerContainerView setCustomOverlayView:];
-[CAMCameraViewControllerContainerView initWithCoder:];
-[CAMCameraViewControllerContainerView customOverlayView];
-[CAMCameraViewControllerContainerView initWithFrame:];
-[CAMCameraViewControllerContainerView viewfinderView];
-[CAMCameraViewControllerContainerView verifyViewOrdering];
-[CAMCameraViewControllerContainerView _commonCAMCameraViewControllerContainerViewInitialization];
-[CAMCameraViewControllerContainerView additionalContentView];
-[CAMCameraViewControllerContainerView setAdditionalContentView:];
-[CAMCameraViewControllerContainerView setViewfinderView:];
```
