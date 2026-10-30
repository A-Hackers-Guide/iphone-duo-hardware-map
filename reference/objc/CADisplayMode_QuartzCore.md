# `CADisplayMode`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 20 properties, 31 instance methods, 3 class methods

## Instance variables

```
^{CADisplayModePriv={Mode=(?={?=b14b14b1b24b1b1b5b2b1b1}Q)}@QQII@{PerModeInfo=IICCfIC}IIQIQI} _priv;
```

## Properties

```
@property (TQ,R,N) width;
@property (TQ,R,N) height;
@property (Td,R,N) pixelAspectRatio;
@property (Td,R,N) refreshRate;
@property (Td,R,N) lineTime;
@property (TB,R,N) isVirtual;
@property (TB,R,N,GisHighBandwidth) highBandwidth;
@property (T@"NSString",R,C,N) colorMode;
@property (TB,R,N) colorModeIsYCbCr;
@property (TQ,R,N) preferredScale;
@property (T@"NSString",R,C,N) hdrMode;
@property (T@"NSString",R,C,N) colorGamut;
@property (TQ,R,N) bitDepth;
@property (TB,R,N) isVRR;
@property (TB,R,N) isExternalSync;
@property (Td,R,N) externalSyncMultiplier;
@property (TQ,R,N) internalRepresentation;
@property (TI,R,N) maximumSourceWidth;
@property (TI,R,N) maximumSourceHeight;
@property (TQ,R,N) maximumSourceBandwidth;
```

## Class methods

```
+[CADisplayMode displayModeWithWidth:height:refreshRate:isVRR:];
+[CADisplayMode displayModeWithWidth:height:refreshRate:];
+[CADisplayMode _displayModeWithMode:display:rates:perMode:maxSourceBandwidthPerPipe:maxMultiPipeAggregateBandwidth:admProvidedBandwidthAvailable:admProvidedwidthAvailable:admProvidedBandwidthExternalSync:admProvidedWidthExternalSync:];
```

## Instance methods

```
-[CADisplayMode hdrMode];
-[CADisplayMode _mode];
-[CADisplayMode bitDepth];
-[CADisplayMode colorMode];
-[CADisplayMode refreshRate];
-[CADisplayMode dealloc];
-[CADisplayMode colorGamut];
-[CADisplayMode isVirtual];
-[CADisplayMode preferredScale];
-[CADisplayMode pixelAspectRatio];
-[CADisplayMode hash];
-[CADisplayMode description];
-[CADisplayMode width];
-[CADisplayMode isEqual:];
-[CADisplayMode height];
-[CADisplayMode _setPointScale:];
-[CADisplayMode isHighBandwidth];
-[CADisplayMode _display];
-[CADisplayMode _initWithMode:display:rates:perMode:maxSourceBandwidthPerPipe:maxMultiPipeAggregateBandwidth:admProvidedBandwidthAvailable:admProvidedwidthAvailable:admProvidedBandwidthExternalSync:admProvidedWidthExternalSync:];
-[CADisplayMode _setPreferredUIScale:];
-[CADisplayMode _setWidth:height:];
-[CADisplayMode colorModeIsYCbCr];
-[CADisplayMode copyPrivateRepresentation];
-[CADisplayMode externalSyncMultiplier];
-[CADisplayMode internalRepresentation];
-[CADisplayMode isExternalSync];
-[CADisplayMode isVRR];
-[CADisplayMode lineTime];
-[CADisplayMode maximumSourceBandwidth];
-[CADisplayMode maximumSourceHeight];
-[CADisplayMode maximumSourceWidth];
```
