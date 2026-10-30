# `PKMetalLiveStrokePaintRenderCache`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKStrokeRenderCache`
- 6 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _buffers;
Q _totalCost;
q _renderZoomFactor;
d _startTime;
d _duration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _animatedStrokeBounds;
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
-[PKMetalLiveStrokePaintRenderCache lockPurgeableResourcesAddToSet:];
-[PKMetalLiveStrokePaintRenderCache cacheCost];
-[PKMetalLiveStrokePaintRenderCache isCompatibleWithInk:renderZoomFactor:];
-[PKMetalLiveStrokePaintRenderCache needsCompute];
```
