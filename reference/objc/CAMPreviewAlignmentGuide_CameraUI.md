# `CAMPreviewAlignmentGuide`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMPreviewAlignmentModelObserver`
- 3 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"CAMPreviewAlignmentModel" _alignmentModel;
@"CAMLevelCrosshair" __targetCrosshair;
@"CAMLevelCrosshair" __guidanceCrosshair;
```

## Properties

```
@property (T@"CAMLevelCrosshair",R,N,V__targetCrosshair) _targetCrosshair;
@property (T@"CAMLevelCrosshair",R,N,V__guidanceCrosshair) _guidanceCrosshair;
@property (T@"CAMPreviewAlignmentModel",R,N,V_alignmentModel) alignmentModel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMPreviewAlignmentGuide layoutSubviews];
-[CAMPreviewAlignmentGuide initWithFrame:];
-[CAMPreviewAlignmentGuide _guidanceCrosshair];
-[CAMPreviewAlignmentGuide _targetCrosshair];
-[CAMPreviewAlignmentGuide alignmentModel];
-[CAMPreviewAlignmentGuide previewAlignmentModelDidChangeAlignmentTransform:];
-[CAMPreviewAlignmentGuide previewAlignmentModelDidChangeOpacity:];
```
