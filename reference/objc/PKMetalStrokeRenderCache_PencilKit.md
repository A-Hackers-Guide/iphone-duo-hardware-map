# `PKMetalStrokeRenderCache`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKStrokeRenderCache`
- 5 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _buffers;
@"NSMutableArray" _secondaryBuffers;
Q _totalCost;
q _renderZoomFactor;
@"PKInk" _ink;
```

## Properties

```
@property (T@"NSArray",R,N) buffers;
@property (T@"NSArray",R,N) secondaryBuffers;
@property (T@"PKInk",R,N,V_ink) ink;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKMetalStrokeRenderCache buffers];
-[PKMetalStrokeRenderCache ink];
-[PKMetalStrokeRenderCache addSecondaryBuffer:];
-[PKMetalStrokeRenderCache lockPurgeableResourcesAddToSet:];
-[PKMetalStrokeRenderCache addBuffer:];
-[PKMetalStrokeRenderCache cacheCost];
-[PKMetalStrokeRenderCache initWithInk:renderZoomFactor:];
-[PKMetalStrokeRenderCache isCompatibleWithInk:renderZoomFactor:];
-[PKMetalStrokeRenderCache needsCompute];
-[PKMetalStrokeRenderCache secondaryBuffers];
```
