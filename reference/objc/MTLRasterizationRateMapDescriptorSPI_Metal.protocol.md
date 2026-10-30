# `MTLRasterizationRateMapDescriptorSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TB,N) skipSampleValidationAndInterpolation;
@property (TB,N) skipSampleValidationAndApplySampleAtTileGranularity;
@property (TQ,N) mutability;
@property (Tf,N) minFactor;
```

## Instance methods

```
-[MTLRasterizationRateMapDescriptorSPI formattedDescription:];
-[MTLRasterizationRateMapDescriptorSPI initWithScreenSize:];
-[MTLRasterizationRateMapDescriptorSPI layerPointer:];
-[MTLRasterizationRateMapDescriptorSPI minFactor];
-[MTLRasterizationRateMapDescriptorSPI mutability];
-[MTLRasterizationRateMapDescriptorSPI setMinFactor:];
-[MTLRasterizationRateMapDescriptorSPI setMutability:];
-[MTLRasterizationRateMapDescriptorSPI setSkipSampleValidationAndApplySampleAtTileGranularity:];
-[MTLRasterizationRateMapDescriptorSPI setSkipSampleValidationAndInterpolation:];
-[MTLRasterizationRateMapDescriptorSPI skipSampleValidationAndApplySampleAtTileGranularity];
-[MTLRasterizationRateMapDescriptorSPI skipSampleValidationAndInterpolation];
```
