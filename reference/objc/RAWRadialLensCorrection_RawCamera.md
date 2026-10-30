# `RAWRadialLensCorrection`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 7 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"CIImage" inputImage;
@"CIVector" inputScales;
@ inputColorSpace;
@"NSNumber" inputDraftMode;
@"NSNumber" inputLDCExecuteFlags;
@"NSNumber" inputVersion;
@"CIImage" mapImg;
```

## Class methods

```
+[RAWRadialLensCorrection customAttributes];
```

## Instance methods

```
-[RAWRadialLensCorrection outputImage];
-[RAWRadialLensCorrection setValue:forKey:];
-[RAWRadialLensCorrection makeMapImages];
```
