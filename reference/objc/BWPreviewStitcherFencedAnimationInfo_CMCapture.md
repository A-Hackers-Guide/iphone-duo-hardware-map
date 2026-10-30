# `BWPreviewStitcherFencedAnimationInfo`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFencedAnimationInfo`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _primaryCaptureRectCenterXPixelOffset;
i _primaryCaptureRectCenterYPixelOffset;
d _primaryCaptureAspectRatio;
{CGPoint="x"d"y"d} _primaryCaptureRectCenter;
```

## Properties

```
@property (Td,V_primaryCaptureAspectRatio) primaryCaptureAspectRatio;
@property (T{CGPoint=dd},V_primaryCaptureRectCenter) primaryCaptureRectCenter;
@property (Ti,V_primaryCaptureRectCenterXPixelOffset) primaryCaptureRectCenterXPixelOffset;
@property (Ti,V_primaryCaptureRectCenterYPixelOffset) primaryCaptureRectCenterYPixelOffset;
```

## Class methods

```
+[BWPreviewStitcherFencedAnimationInfo fencedAnimationInfoWithAspectRatio:center:centerXPixelOffset:centerYPixelOffset:fencePortSendRight:];
```

## Instance methods

```
-[BWPreviewStitcherFencedAnimationInfo setPrimaryCaptureRectCenter:];
-[BWPreviewStitcherFencedAnimationInfo primaryCaptureRectCenter];
-[BWPreviewStitcherFencedAnimationInfo description];
-[BWPreviewStitcherFencedAnimationInfo primaryCaptureAspectRatio];
-[BWPreviewStitcherFencedAnimationInfo primaryCaptureRectCenterXPixelOffset];
-[BWPreviewStitcherFencedAnimationInfo primaryCaptureRectCenterYPixelOffset];
-[BWPreviewStitcherFencedAnimationInfo setPrimaryCaptureAspectRatio:];
-[BWPreviewStitcherFencedAnimationInfo setPrimaryCaptureRectCenterXPixelOffset:];
-[BWPreviewStitcherFencedAnimationInfo setPrimaryCaptureRectCenterYPixelOffset:];
```
