# `RAWLensCorrectionVignetteFilter`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 5 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSData" inputVignetteTable;
@"NSNumber" inputVignetteAmount;
@ inputColorSpace;
@"CIImage" vigImg;
```

## Class methods

```
+[RAWLensCorrectionVignetteFilter customAttributes];
```

## Instance methods

```
-[RAWLensCorrectionVignetteFilter customAttributes];
-[RAWLensCorrectionVignetteFilter outputImage];
-[RAWLensCorrectionVignetteFilter setValue:forKey:];
-[RAWLensCorrectionVignetteFilter makeMapImages];
```
