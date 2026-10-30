# `MTLRasterizationRateMapDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLRasterizationRateMapDescriptor`
- Protocols: `MTLRasterizationRateMapDescriptorSPI`
- 8 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
{?="width"Q"height"Q"depth"Q} _screenSize;
@"NSString" _label;
{vector<MTLRasterizationRateLayerDescriptor *, std::allocator<MTLRasterizationRateLayerDescriptor *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _layers;
@"MTLRasterizationRateLayerArrayInternal" _layerAccessor;
B _skipSampleValidationAndInterpolation;
B _skipSampleValidationAndApplySampleAtTileGranularity;
f _minFactor;
Q _mutability;
```

## Properties

```
@property (TB,N,V_skipSampleValidationAndInterpolation) skipSampleValidationAndInterpolation;
@property (TB,N,V_skipSampleValidationAndApplySampleAtTileGranularity) skipSampleValidationAndApplySampleAtTileGranularity;
@property (TQ,N,V_mutability) mutability;
@property (Tf,N,V_minFactor) minFactor;
```

## Instance methods

```
-[MTLRasterizationRateMapDescriptorInternal screenSize];
-[MTLRasterizationRateMapDescriptorInternal layers];
-[MTLRasterizationRateMapDescriptorInternal formattedDescription:];
-[MTLRasterizationRateMapDescriptorInternal init];
-[MTLRasterizationRateMapDescriptorInternal label];
-[MTLRasterizationRateMapDescriptorInternal setLabel:];
-[MTLRasterizationRateMapDescriptorInternal dealloc];
-[MTLRasterizationRateMapDescriptorInternal hash];
-[MTLRasterizationRateMapDescriptorInternal description];
-[MTLRasterizationRateMapDescriptorInternal copyWithZone:];
-[MTLRasterizationRateMapDescriptorInternal isEqual:];
-[MTLRasterizationRateMapDescriptorInternal setScreenSize:];
-[MTLRasterizationRateMapDescriptorInternal layerCount];
-[MTLRasterizationRateMapDescriptorInternal initWithScreenSize:];
-[MTLRasterizationRateMapDescriptorInternal layerAtIndex:];
-[MTLRasterizationRateMapDescriptorInternal layerPointer:];
-[MTLRasterizationRateMapDescriptorInternal minFactor];
-[MTLRasterizationRateMapDescriptorInternal mutability];
-[MTLRasterizationRateMapDescriptorInternal setLayer:atIndex:];
-[MTLRasterizationRateMapDescriptorInternal setMinFactor:];
-[MTLRasterizationRateMapDescriptorInternal setMutability:];
-[MTLRasterizationRateMapDescriptorInternal setSkipSampleValidationAndApplySampleAtTileGranularity:];
-[MTLRasterizationRateMapDescriptorInternal setSkipSampleValidationAndInterpolation:];
-[MTLRasterizationRateMapDescriptorInternal skipSampleValidationAndApplySampleAtTileGranularity];
-[MTLRasterizationRateMapDescriptorInternal skipSampleValidationAndInterpolation];
```
