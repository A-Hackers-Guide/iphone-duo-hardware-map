# `RAWBayerFPCorrectionFilter`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CIFilter`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSDictionary" inputFocusPixelPatternsDict;
@"NSNumber" inputSensorPattern;
@"CIVector" inputBlacks;
@"NSDictionary" inputDNGMetadata;
```

## Properties

```
@property (T@"CIImage",&,VinputImage) inputImage;
@property (T@"NSDictionary",&,N,VinputFocusPixelPatternsDict) inputFocusPixelPatternsDict;
@property (T@"NSNumber",&,N,VinputSensorPattern) inputSensorPattern;
@property (T@"CIVector",&,N,VinputBlacks) inputBlacks;
@property (T@"NSDictionary",&,N,VinputDNGMetadata) inputDNGMetadata;
```

## Instance methods

```
-[RAWBayerFPCorrectionFilter setInputImage:];
-[RAWBayerFPCorrectionFilter outputImage];
-[RAWBayerFPCorrectionFilter inputImage];
-[RAWBayerFPCorrectionFilter initWithArguments:];
-[RAWBayerFPCorrectionFilter setInputFocusPixelPatternsDict:];
-[RAWBayerFPCorrectionFilter setInputBlacks:];
-[RAWBayerFPCorrectionFilter inputBlacks];
-[RAWBayerFPCorrectionFilter inputDNGMetadata];
-[RAWBayerFPCorrectionFilter inputFocusPixelPatternsDict];
-[RAWBayerFPCorrectionFilter inputSensorPattern];
-[RAWBayerFPCorrectionFilter patternsHaveValidBounds:];
-[RAWBayerFPCorrectionFilter setInputDNGMetadata:];
-[RAWBayerFPCorrectionFilter setInputSensorPattern:];
```
