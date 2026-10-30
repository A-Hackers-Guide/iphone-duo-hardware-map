# `RAWLocalToneMap`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 9 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSNumber" inputShadowAmount;
@"NSNumber" inputHighlightAmount;
@"NSNumber" inputShadowCutoff;
@"NSNumber" inputHighlightCutoff;
@"NSNumber" inputAmount;
@"NSNumber" inputBlurRadius;
@ inputColorSpace;
@"CIImage" tcImage;
```

## Class methods

```
+[RAWLocalToneMap customAttributes];
```

## Instance methods

```
-[RAWLocalToneMap outputImage];
-[RAWLocalToneMap makeToneCurveImage];
```
