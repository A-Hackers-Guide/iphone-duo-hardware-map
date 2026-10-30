# `MTLRasterizationRateMapDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 4 properties, 3 instance methods, 4 class methods

## Properties

```
@property (T@"MTLRasterizationRateLayerArray",R,D,N) layers;
@property (T{?=QQQ},D,N) screenSize;
@property (T@"NSString",C,D,N) label;
@property (TQ,R,D,N) layerCount;
```

## Class methods

```
+[MTLRasterizationRateMapDescriptor allocWithZone:];
+[MTLRasterizationRateMapDescriptor rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:];
+[MTLRasterizationRateMapDescriptor rasterizationRateMapDescriptorWithScreenSize:];
+[MTLRasterizationRateMapDescriptor rasterizationRateMapDescriptorWithScreenSize:layer:];
```

## Instance methods

```
-[MTLRasterizationRateMapDescriptor copyWithZone:];
-[MTLRasterizationRateMapDescriptor layerAtIndex:];
-[MTLRasterizationRateMapDescriptor setLayer:atIndex:];
```
