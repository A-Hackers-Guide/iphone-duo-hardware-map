# `CAContentStreamOptions`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 15 instance variables, 15 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _alwaysScaleToFit;
B _preserveAspectRatioKey;
B _showCursorKey;
C _YCbCrMatrix;
C _ChromaLocation;
I _targetDisplayId;
I _pixelFormat;
I _queueDepth;
d _minimumFrameTime;
^{CGColorSpace=} _colorSpaceKey;
^{CGColor=} _backgroundColorKey;
Q _trackedLayerIDContent;
{CGSize="width"d"height"d} _frameSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _destinationRect;
```

## Properties

```
@property (TI,V_targetDisplayId) targetDisplayId;
@property (TI,V_pixelFormat) pixelFormat;
@property (T{CGSize=dd},V_frameSize) frameSize;
@property (TI,V_queueDepth) queueDepth;
@property (Td,V_minimumFrameTime) minimumFrameTime;
@property (TB,V_alwaysScaleToFit) alwaysScaleToFit;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_sourceRect) sourceRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_destinationRect) destinationRect;
@property (TB,V_preserveAspectRatioKey) preserveAspectRatioKey;
@property (T^{CGColorSpace=},V_colorSpaceKey) colorSpaceKey;
@property (T^{CGColor=},V_backgroundColorKey) backgroundColorKey;
@property (TB,V_showCursorKey) showCursorKey;
@property (TC,V_YCbCrMatrix) YCbCrMatrix;
@property (TC,V_ChromaLocation) ChromaLocation;
@property (TQ,V_trackedLayerIDContent) trackedLayerIDContent;
```

## Instance methods

```
-[CAContentStreamOptions setSourceRect:];
-[CAContentStreamOptions sourceRect];
-[CAContentStreamOptions minimumFrameTime];
-[CAContentStreamOptions setQueueDepth:];
-[CAContentStreamOptions YCbCrMatrix];
-[CAContentStreamOptions queueDepth];
-[CAContentStreamOptions pixelFormat];
-[CAContentStreamOptions copyWithZone:];
-[CAContentStreamOptions setPixelFormat:];
-[CAContentStreamOptions setYCbCrMatrix:];
-[CAContentStreamOptions frameSize];
-[CAContentStreamOptions destinationRect];
-[CAContentStreamOptions ChromaLocation];
-[CAContentStreamOptions targetDisplayId];
-[CAContentStreamOptions alwaysScaleToFit];
-[CAContentStreamOptions backgroundColorKey];
-[CAContentStreamOptions colorSpaceKey];
-[CAContentStreamOptions preserveAspectRatioKey];
-[CAContentStreamOptions setAlwaysScaleToFit:];
-[CAContentStreamOptions setBackgroundColorKey:];
-[CAContentStreamOptions setChromaLocation:];
-[CAContentStreamOptions setColorSpaceKey:];
-[CAContentStreamOptions setDestinationRect:];
-[CAContentStreamOptions setFrameSize:];
-[CAContentStreamOptions setMinimumFrameTime:];
-[CAContentStreamOptions setPreserveAspectRatioKey:];
-[CAContentStreamOptions setShowCursorKey:];
-[CAContentStreamOptions setTargetDisplayId:];
-[CAContentStreamOptions setTrackedLayerIDContent:];
-[CAContentStreamOptions showCursorKey];
-[CAContentStreamOptions trackedLayerIDContent];
```
