# `CALayerHost`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 3 instance variables, 17 properties, 42 instance methods, 4 class methods

## Instance variables

```
B _tokenNeedsPort;
f _asynchronousRenderMaxAPL;
f _asynchronousRenderMaxAPLStrength;
```

## Properties

```
@property (TI) contextId;
@property (T@"CAHostingToken",&,N) hostingToken;
@property (TB) inheritsSecurity;
@property (TB) rendersAsynchronously;
@property (TB) asynchronousOpaque;
@property (T@"NSArray",C) asynchronousRenderTimes;
@property (Td) asynchronousRenderPeriod;
@property (Tf,V_asynchronousRenderMaxAPL) asynchronousRenderMaxAPL;
@property (Tf,V_asynchronousRenderMaxAPLStrength) asynchronousRenderMaxAPLStrength;
@property (TB) resizesHostedContext;
@property (T@"NSString",C) hostedContextGravity;
@property (TB) preservesFlip;
@property (TB) stopsHitTestTransformAccumulation;
@property (TB) stopsSecureSuperlayersValidation;
@property (TB) transformsToScreenSpace;
@property (TB) sequestered;
@property (T@"NSString",C) zombificationMode;
```

## Class methods

```
+[CALayerHost defaultValueForKey:];
+[CALayerHost _hasRenderLayerSubclass];
+[CALayerHost allLayerHosts];
+[CALayerHost CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CALayerHost setRendersAsynchronously:];
-[CALayerHost stopsSecureSuperlayersValidation];
-[CALayerHost setAsynchronousRenderMaxAPLStrength:];
-[CALayerHost asynchronousRenderMaxAPLStrength];
-[CALayerHost setNeedsAuthoritativeHostingToken];
-[CALayerHost hostedContextGravity];
-[CALayerHost setAsynchronousOpaque:];
-[CALayerHost contextId];
-[CALayerHost setTransformsToScreenSpace:];
-[CALayerHost asynchronousRenderTimes];
-[CALayerHost setAsynchronousRenderMaxAPL:];
-[CALayerHost zombificationMode];
-[CALayerHost resizesHostedContext];
-[CALayerHost setSequestered:];
-[CALayerHost setAsynchronousRenderPeriod:];
-[CALayerHost stopsHitTestTransformAccumulation];
-[CALayerHost setPreservesFlip:];
-[CALayerHost setStopsSecureSuperlayersValidation:];
-[CALayerHost didChangeValueForKey:];
-[CALayerHost asynchronousOpaque];
-[CALayerHost setStopsHitTestTransformAccumulation:];
-[CALayerHost asynchronousRenderMaxAPL];
-[CALayerHost setHostedContextGravity:];
-[CALayerHost hostingToken];
-[CALayerHost setHostingToken:];
-[CALayerHost _copyRenderLayer:layerFlags:commitFlags:];
-[CALayerHost setZombificationMode:];
-[CALayerHost sequestered];
-[CALayerHost transformsToScreenSpace];
-[CALayerHost setContextId:];
-[CALayerHost asynchronousRenderPeriod];
-[CALayerHost setResizesHostedContext:];
-[CALayerHost setAsynchronousRenderTimes:];
-[CALayerHost preservesFlip];
-[CALayerHost rendersAsynchronously];
-[CALayerHost init];
-[CALayerHost _renderLayerDefinesProperty:];
-[CALayerHost dealloc];
-[CALayerHost layerDidBecomeVisible:];
-[CALayerHost shouldArchiveValueForKey:];
-[CALayerHost setInheritsSecurity:];
-[CALayerHost inheritsSecurity];
```
