# `MTLRasterizationRateLayerDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLRasterizationRateLayerDescriptor`
- 5 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
^f _data;
{?="width"Q"height"Q"depth"Q} _size;
{?="width"Q"height"Q"depth"Q} _currentSampleCount;
@"MTLRasterizationRateSampleArrayInternal" _horizontal;
@"MTLRasterizationRateSampleArrayInternal" _vertical;
```

## Instance methods

```
-[MTLRasterizationRateLayerDescriptorInternal setSampleCount:];
-[MTLRasterizationRateLayerDescriptorInternal formattedDescription:];
-[MTLRasterizationRateLayerDescriptorInternal init];
-[MTLRasterizationRateLayerDescriptorInternal dealloc];
-[MTLRasterizationRateLayerDescriptorInternal sampleCount];
-[MTLRasterizationRateLayerDescriptorInternal hash];
-[MTLRasterizationRateLayerDescriptorInternal description];
-[MTLRasterizationRateLayerDescriptorInternal copyWithZone:];
-[MTLRasterizationRateLayerDescriptorInternal isEqual:];
-[MTLRasterizationRateLayerDescriptorInternal horizontal];
-[MTLRasterizationRateLayerDescriptorInternal maxSampleCount];
-[MTLRasterizationRateLayerDescriptorInternal horizontalSampleStorage];
-[MTLRasterizationRateLayerDescriptorInternal initWithSampleCount:];
-[MTLRasterizationRateLayerDescriptorInternal initWithSampleCount:horizontal:vertical:];
-[MTLRasterizationRateLayerDescriptorInternal vertical];
-[MTLRasterizationRateLayerDescriptorInternal verticalSampleStorage];
```
