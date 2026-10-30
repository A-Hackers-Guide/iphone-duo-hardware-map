# `CAMFullscreenViewfinderLayout`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 22 instance methods, 2 class methods

## Instance variables

```
d _screenScale;
q _phoneAltLayout;
d _frontCameraInset;
{CGSize="width"d"height"d} _shutterIntrinsicSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceBounds;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __safeAreaInsets;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},R,N,V__safeAreaInsets) _safeAreaInsets;
@property (Td,N,V_frontCameraInset) frontCameraInset;
@property (Td,N) frontCameraInset;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_referenceBounds) referenceBounds;
@property (T{CGSize=dd},N,V_shutterIntrinsicSize) shutterIntrinsicSize;
@property (Td,N,V_screenScale) screenScale;
@property (Tq,N,V_phoneAltLayout) phoneAltLayout;
```

## Class methods

```
+[CAMFullscreenViewfinderLayout viewportFrameForAspectRatio:fullscreenBounds:screenScale:smartStyleControlsExpanded:phoneAltLayout:];
+[CAMFullscreenViewfinderLayout viewportSizeForAspectRatio:fullscreenSize:screenScale:];
```

## Instance methods

```
-[CAMFullscreenViewfinderLayout referenceBounds];
-[CAMFullscreenViewfinderLayout screenScale];
-[CAMFullscreenViewfinderLayout setScreenScale:];
-[CAMFullscreenViewfinderLayout frontCameraInset];
-[CAMFullscreenViewfinderLayout setReferenceBounds:];
-[CAMFullscreenViewfinderLayout _updateSafeAreaInsets];
-[CAMFullscreenViewfinderLayout phoneAltLayout];
-[CAMFullscreenViewfinderLayout setPhoneAltLayout:];
-[CAMFullscreenViewfinderLayout _safeAreaInsets];
-[CAMFullscreenViewfinderLayout alignmentRectForBottomRightControlOfSize:];
-[CAMFullscreenViewfinderLayout alignmentRectForShutterControl];
-[CAMFullscreenViewfinderLayout frameForContentClippingContainer];
-[CAMFullscreenViewfinderLayout frameForControlStatusBar];
-[CAMFullscreenViewfinderLayout frameForShutterControl:];
-[CAMFullscreenViewfinderLayout geometryForElapsedTimeView:viewportFrame:orientation:];
-[CAMFullscreenViewfinderLayout geometryForElapsedTimeView:viewportFrame:orientation:systemOverlayVisible:];
-[CAMFullscreenViewfinderLayout initWithReferenceBounds:shutterIntrinsicSize:];
-[CAMFullscreenViewfinderLayout setFrontCameraInset:];
-[CAMFullscreenViewfinderLayout setShutterIntrinsicSize:];
-[CAMFullscreenViewfinderLayout shutterIntrinsicSize];
-[CAMFullscreenViewfinderLayout viewportFrameForAspectRatio:smartStyleControlsExpanded:];
-[CAMFullscreenViewfinderLayout viewportSizeForAspectRatio:];
```
