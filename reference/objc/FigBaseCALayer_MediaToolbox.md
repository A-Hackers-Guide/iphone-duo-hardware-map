# `FigBaseCALayer`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `FigPiPableLayer`
- 7 instance variables, 1 properties, 22 instance methods, 1 class methods

## Instance variables

```
B _preventsChangesToSublayerHierarchy;
@"CAShapeLayer" _DRMFallbackIconLayer;
@"CATextLayer" _DRMFallbackTextLayer;
{CGSize="width"d"height"d} _DRMFallbackIconSize;
B _enabledDRMFallback;
@ _snapshotObserverForAppKit;
@ _snapshotObserverForWebKit;
```

## Properties

```
@property (TB,N,V_preventsChangesToSublayerHierarchy) preventsChangesToSublayerHierarchy;
```

## Class methods

```
+[FigBaseCALayer defaultActionForKey:];
```

## Instance methods

```
-[FigBaseCALayer actionForKey:];
-[FigBaseCALayer setNeedsDisplay];
-[FigBaseCALayer init];
-[FigBaseCALayer initWithDeferredTransaction:];
-[FigBaseCALayer dealloc];
-[FigBaseCALayer setPreventsChangesToSublayerHierarchy:];
-[FigBaseCALayer setBounds:];
-[FigBaseCALayer preventsChangesToSublayerHierarchy];
-[FigBaseCALayer removeFromSuperlayer];
-[FigBaseCALayer addSublayer:];
-[FigBaseCALayer insertSublayer:above:];
-[FigBaseCALayer setFrame:];
-[FigBaseCALayer layoutSublayers];
-[FigBaseCALayer insertSublayer:atIndex:];
-[FigBaseCALayer setPosition:];
-[FigBaseCALayer replaceSublayer:with:];
-[FigBaseCALayer insertSublayer:below:];
-[FigBaseCALayer setSublayers:];
-[FigBaseCALayer getDisplayScale];
-[FigBaseCALayer getLayerDisplay];
-[FigBaseCALayer layoutDRMLayerPositionsAndSizes];
-[FigBaseCALayer enableDRMFallback];
```
