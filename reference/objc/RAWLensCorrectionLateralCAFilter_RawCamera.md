# `RAWLensCorrectionLateralCAFilter`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 7 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSNumber" inputLateralCAAmount;
@"NSData" inputLateralCAMap;
@"NSNumber" inputLateralCAMapWidth;
@"NSNumber" inputLateralCAMapHeight;
@ inputColorSpace;
@"CIImage" mapImg;
```

## Class methods

```
+[RAWLensCorrectionLateralCAFilter customAttributes];
```

## Instance methods

```
-[RAWLensCorrectionLateralCAFilter customAttributes];
-[RAWLensCorrectionLateralCAFilter outputImage];
-[RAWLensCorrectionLateralCAFilter setValue:forKey:];
-[RAWLensCorrectionLateralCAFilter makeMapImages];
```
