# `MTLSamplerDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLSamplerDescriptor`
- 1 instance variables, 7 properties, 60 instance methods, 0 class methods

## Instance variables

```
{MTLSamplerDescriptorPrivate=""(?=""{?="minFilter"b2"magFilter"b2"mipFilter"b2"sAddressMode"b3"tAddressMode"b3"rAddressMode"b3"normalizedCoords"b1"borderColor"b2"lodAverage"b1"compareFunction"b3"supportArgumentBuffers"b1"reductionMode"b2"forceResourceIndex"b1"forceSeamsOnCubemapFiltering"b1}"miscHash"I)""(?="lodMinClampHash"I"lodMinClamp"f)""(?="lodMaxClampHash"I"lodMaxClamp"f)""(?="lodBiasHash"I"lodBias"f)"maxAnisotropy"Q"label"@"NSString""resourceIndex"Q"customBorderColorValue"[4I]"pixelFormat"Q} _private;
```

## Properties

```
@property (TQ,N) borderColorSPI;
@property (TI,N) customBorderColorValue_0;
@property (TI,N) customBorderColorValue_1;
@property (TI,N) customBorderColorValue_2;
@property (TI,N) customBorderColorValue_3;
@property (TQ,N) reductionMode;
@property (TB,N) forceSeamsOnCubemapFiltering;
```

## Instance methods

```
-[MTLSamplerDescriptorInternal setResourceIndex:];
-[MTLSamplerDescriptorInternal resourceIndex];
-[MTLSamplerDescriptorInternal setForceResourceIndex:];
-[MTLSamplerDescriptorInternal forceResourceIndex];
-[MTLSamplerDescriptorInternal setNormalizedCoordinates:];
-[MTLSamplerDescriptorInternal setBorderColor:];
-[MTLSamplerDescriptorInternal descriptorPrivate];
-[MTLSamplerDescriptorInternal setCustomBorderColorValue_0:];
-[MTLSamplerDescriptorInternal normalizedCoordinates];
-[MTLSamplerDescriptorInternal magFilter];
-[MTLSamplerDescriptorInternal formattedDescription:];
-[MTLSamplerDescriptorInternal setMinFilter:];
-[MTLSamplerDescriptorInternal setBorderColorSPI:];
-[MTLSamplerDescriptorInternal setTAddressMode:];
-[MTLSamplerDescriptorInternal init];
-[MTLSamplerDescriptorInternal label];
-[MTLSamplerDescriptorInternal setLabel:];
-[MTLSamplerDescriptorInternal reductionMode];
-[MTLSamplerDescriptorInternal dealloc];
-[MTLSamplerDescriptorInternal compareFunction];
-[MTLSamplerDescriptorInternal customBorderColorValue_0];
-[MTLSamplerDescriptorInternal setLodBias:];
-[MTLSamplerDescriptorInternal tAddressMode];
-[MTLSamplerDescriptorInternal setMaxAnisotropy:];
-[MTLSamplerDescriptorInternal minFilter];
-[MTLSamplerDescriptorInternal setCustomBorderColorValue_2:];
-[MTLSamplerDescriptorInternal rAddressMode];
-[MTLSamplerDescriptorInternal setLodAverage:];
-[MTLSamplerDescriptorInternal supportArgumentBuffers];
-[MTLSamplerDescriptorInternal setMipFilter:];
-[MTLSamplerDescriptorInternal setRAddressMode:];
-[MTLSamplerDescriptorInternal setCompareFunction:];
-[MTLSamplerDescriptorInternal mipFilter];
-[MTLSamplerDescriptorInternal forceSeamsOnCubemapFiltering];
-[MTLSamplerDescriptorInternal lodBias];
-[MTLSamplerDescriptorInternal setSAddressMode:];
-[MTLSamplerDescriptorInternal setCustomBorderColorValue_1:];
-[MTLSamplerDescriptorInternal hash];
-[MTLSamplerDescriptorInternal setReductionMode:];
-[MTLSamplerDescriptorInternal description];
-[MTLSamplerDescriptorInternal setSupportArgumentBuffers:];
-[MTLSamplerDescriptorInternal setLodMaxClamp:];
-[MTLSamplerDescriptorInternal setMagFilter:];
-[MTLSamplerDescriptorInternal customBorderColorValue_2];
-[MTLSamplerDescriptorInternal pixelFormat];
-[MTLSamplerDescriptorInternal setCustomBorderColorValue_3:];
-[MTLSamplerDescriptorInternal setForceSeamsOnCubemapFiltering:];
-[MTLSamplerDescriptorInternal lodAverage];
-[MTLSamplerDescriptorInternal borderColorSPI];
-[MTLSamplerDescriptorInternal lodMaxClamp];
-[MTLSamplerDescriptorInternal copyWithZone:];
-[MTLSamplerDescriptorInternal setLodMinClamp:];
-[MTLSamplerDescriptorInternal setPixelFormat:];
-[MTLSamplerDescriptorInternal sAddressMode];
-[MTLSamplerDescriptorInternal isEqual:];
-[MTLSamplerDescriptorInternal customBorderColorValue_1];
-[MTLSamplerDescriptorInternal lodMinClamp];
-[MTLSamplerDescriptorInternal customBorderColorValue_3];
-[MTLSamplerDescriptorInternal borderColor];
-[MTLSamplerDescriptorInternal maxAnisotropy];
```
