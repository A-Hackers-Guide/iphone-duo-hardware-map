# `RAWLensCorrectionDNG`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 6 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"CIImage" inputImage;
@"CIVector" inputKr;
@"CIVector" inputKt;
@"CIVector" inputCenter;
@ inputColorSpace;
@"NSNumber" inputDraftMode;
```

## Class methods

```
+[RAWLensCorrectionDNG customAttributes];
```

## Instance methods

```
-[RAWLensCorrectionDNG customAttributes];
-[RAWLensCorrectionDNG outputImage];
-[RAWLensCorrectionDNG mapPoint:info:];
```
