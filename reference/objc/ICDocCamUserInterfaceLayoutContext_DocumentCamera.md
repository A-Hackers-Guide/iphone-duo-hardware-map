# `ICDocCamUserInterfaceLayoutContext`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
q _layout;
q _orientation;
```

## Properties

```
@property (Tq,N,V_layout) layout;
@property (Tq,N,V_orientation) orientation;
@property (TB,R,N) isPhone;
@property (TB,R,N) isPad;
@property (TB,R,N) supportsConfigurableVideoGravity;
@property (TB,R,N) shouldCropImageToVisibleBounds;
```

## Class methods

```
+[ICDocCamUserInterfaceLayoutContext defaultContext];
```

## Instance methods

```
-[ICDocCamUserInterfaceLayoutContext isPad];
-[ICDocCamUserInterfaceLayoutContext setOrientation:];
-[ICDocCamUserInterfaceLayoutContext orientation];
-[ICDocCamUserInterfaceLayoutContext description];
-[ICDocCamUserInterfaceLayoutContext layout];
-[ICDocCamUserInterfaceLayoutContext isEqual:];
-[ICDocCamUserInterfaceLayoutContext isPhone];
-[ICDocCamUserInterfaceLayoutContext setLayout:];
-[ICDocCamUserInterfaceLayoutContext captureControlsToolbarEdgeForTraitCollection:orientation:];
-[ICDocCamUserInterfaceLayoutContext effectiveInterfaceOrientationWithOrientation:];
-[ICDocCamUserInterfaceLayoutContext initWithLayout:orientation:];
-[ICDocCamUserInterfaceLayoutContext shouldCropImageToVisibleBounds];
-[ICDocCamUserInterfaceLayoutContext supportsConfigurableVideoGravity];
-[ICDocCamUserInterfaceLayoutContext toolbarEdgeForTraitCollection:];
```
