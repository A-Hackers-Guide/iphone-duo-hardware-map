# `RAWProfileGainTableMap`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 13 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSNumber" inputMapPointsV;
@"NSNumber" inputMapPointsH;
@"NSNumber" inputMapSpacingV;
@"NSNumber" inputMapSpacingH;
@"NSNumber" inputMapOriginV;
@"NSNumber" inputMapOriginH;
@"NSNumber" inputMapPointsN;
@"CIVector" inputWeights;
@"NSData" inputGainData;
@"NSNumber" inputGamma;
@"NSNumber" inputStrength;
@ inputColorSpace;
```

## Instance methods

```
-[RAWProfileGainTableMap outputImage];
-[RAWProfileGainTableMap gainImage];
```
