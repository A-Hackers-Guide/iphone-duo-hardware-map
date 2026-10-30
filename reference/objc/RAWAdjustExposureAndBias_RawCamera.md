# `RAWAdjustExposureAndBias`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 5 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CIImage" inputImage;
@ inputColorSpace;
@"NSNumber" inputBaselineExposure;
@"NSNumber" inputExposure;
@"NSNumber" inputBias;
```

## Class methods

```
+[RAWAdjustExposureAndBias customAttributes];
+[RAWAdjustExposureAndBias automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[RAWAdjustExposureAndBias customAttributes];
-[RAWAdjustExposureAndBias outputImage];
-[RAWAdjustExposureAndBias setInputExposure:];
-[RAWAdjustExposureAndBias setInputBias:];
-[RAWAdjustExposureAndBias outputMatrix];
```
