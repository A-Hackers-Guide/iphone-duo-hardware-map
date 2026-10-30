# `CUIPSDGradientEvaluator`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSCopying`
- 8 instance variables, 1 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSArray" colorStops;
@"NSArray" colorMidpointLocations;
@"NSArray" opacityStops;
@"NSArray" opacityMidpointLocations;
d smoothingCoefficient;
{_psdGradientColor="red"d"green"d"blue"d"alpha"d} fillColor;
i blendMode;
{?="colorEdgePixel"b2"opacityEdgePixel"b2"isDithered"b1"reserved"b3} pgeFlags;
```

## Properties

```
@property (Ti,N,VblendMode) blendMode;
```

## Class methods

```
+[CUIPSDGradientEvaluator initialize];
```

## Instance methods

```
-[CUIPSDGradientEvaluator colorStops];
-[CUIPSDGradientEvaluator fillColor];
-[CUIPSDGradientEvaluator dealloc];
-[CUIPSDGradientEvaluator isDithered];
-[CUIPSDGradientEvaluator encodeWithCoder:];
-[CUIPSDGradientEvaluator description];
-[CUIPSDGradientEvaluator initWithCoder:];
-[CUIPSDGradientEvaluator copyWithZone:];
-[CUIPSDGradientEvaluator blendMode];
-[CUIPSDGradientEvaluator setBlendMode:];
-[CUIPSDGradientEvaluator fillCoefficient];
-[CUIPSDGradientEvaluator _cleanedUpMidpointLocationsFromLocations:];
-[CUIPSDGradientEvaluator _createOrderedStops:midpoints:fromStops:midpoints:edgePixel:];
-[CUIPSDGradientEvaluator _smoothedGradientColorAtLocation:];
-[CUIPSDGradientEvaluator _smoothedInterpolationOfLocation:betweenLower:upper:scaledMidpoint:];
-[CUIPSDGradientEvaluator colorMidpointLocations];
-[CUIPSDGradientEvaluator customizeForDistance:];
-[CUIPSDGradientEvaluator hasEdgePixel];
-[CUIPSDGradientEvaluator initWithColorStops:colorMidpoints:opacityStops:opacityMidpoints:smoothingCoefficient:fillCoefficient:];
-[CUIPSDGradientEvaluator initWithColorStops:colorMidpoints:opacityStops:opacityMidpoints:smoothingCoefficient:fillColor:dither:];
-[CUIPSDGradientEvaluator opacityMidpointLocations];
-[CUIPSDGradientEvaluator opacityStops];
-[CUIPSDGradientEvaluator setColorStops:midpoints:];
-[CUIPSDGradientEvaluator setFillCoefficient:];
-[CUIPSDGradientEvaluator setOpacityStops:midpoints:];
-[CUIPSDGradientEvaluator setSmoothingCoefficient:];
-[CUIPSDGradientEvaluator smoothingCoefficient];
```
