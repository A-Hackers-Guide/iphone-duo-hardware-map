# `PKMetalSDFPenRenderCache`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKStrokeRenderCache`
- 4 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _buffers;
Q _totalCost;
q _renderZoomFactor;
B _purgeableBuffers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKMetalSDFPenRenderCache lockPurgeableResourcesAddToSet:];
-[PKMetalSDFPenRenderCache cacheCost];
-[PKMetalSDFPenRenderCache isCompatibleWithInk:renderZoomFactor:];
-[PKMetalSDFPenRenderCache needsCompute];
```
