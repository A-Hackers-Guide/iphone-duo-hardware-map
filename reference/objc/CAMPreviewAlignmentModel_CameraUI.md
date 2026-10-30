# `CAMPreviewAlignmentModel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _aligned;
@"<CAMPreviewAlignmentModelObserver>" _observer;
d _opacity;
@"CMDeviceMotion" __referenceDeviceMotion;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _alignmentTransform;
```

## Properties

```
@property (T{CATransform3D=dddddddddddddddd},N,S_setAlignmentTransform:,V_alignmentTransform) alignmentTransform;
@property (TB,N,GisAligned,S_setAligned:,V_aligned) aligned;
@property (Td,N,S_setOpacity:,V_opacity) opacity;
@property (T@"CMDeviceMotion",&,N,S_setReferenceDeviceMotion:,V__referenceDeviceMotion) _referenceDeviceMotion;
@property (T@"<CAMPreviewAlignmentModelObserver>",W,N,V_observer) observer;
```

## Class methods

```
+[CAMPreviewAlignmentModel desiredUpdateInterval];
```

## Instance methods

```
-[CAMPreviewAlignmentModel observer];
-[CAMPreviewAlignmentModel init];
-[CAMPreviewAlignmentModel reset];
-[CAMPreviewAlignmentModel opacity];
-[CAMPreviewAlignmentModel setObserver:];
-[CAMPreviewAlignmentModel _setOpacity:];
-[CAMPreviewAlignmentModel alignmentTransform];
-[CAMPreviewAlignmentModel isAligned];
-[CAMPreviewAlignmentModel _referenceDeviceMotion];
-[CAMPreviewAlignmentModel _setAligned:];
-[CAMPreviewAlignmentModel _setAlignmentTransform:];
-[CAMPreviewAlignmentModel _setReferenceDeviceMotion:];
-[CAMPreviewAlignmentModel applyDeviceMotion:];
```
