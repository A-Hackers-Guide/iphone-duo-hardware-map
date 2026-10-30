# `RAWSimpleLensCorrectionFilter`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 8 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSNumber" inputDistortionScaleHalfMinorRadius;
@"NSNumber" inputDistortionScaleMinorRadius;
@"NSNumber" inputDistortionScaleMajorRadius;
@"NSNumber" inputDistortionScaleMaxRadius;
@"NSNumber" inputDraftMode;
@ inputColorSpace;
@"NSNumber" inputFocalLength;
```

## Class methods

```
+[RAWSimpleLensCorrectionFilter customAttributes];
```

## Instance methods

```
-[RAWSimpleLensCorrectionFilter customAttributes];
-[RAWSimpleLensCorrectionFilter outputImage];
```
