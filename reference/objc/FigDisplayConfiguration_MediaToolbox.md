# `FigDisplayConfiguration`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 22 properties, 49 instance methods, 0 class methods

## Instance variables

```
^{__CFDictionary=} _fvdOptions;
^{OpaqueFigSimpleMutex=} _lock;
Q _preset;
```

## Properties

```
@property (T{CGSize=dd},N) maxDisplaySize;
@property (TI,N) refreshRate;
@property (TI,N) pixelFormat;
@property (TQ,N) preset;
@property (TB,N) useExtendedColor;
@property (Tq,N) numOfIdleFrames;
@property (Tq,N) imagePoolSize;
@property (T@"NSString",N) clientName;
@property (Tq,N) clientPID;
@property (Tq,N) displayMode;
@property (T@"NSString",N) displayLabel;
@property (T{CGSize=dd},N) canvasSize;
@property (Tq,N) preferredUIScaleFactor;
@property (TQ,N) toneMappingMode;
@property (TQ,N) mirroringRestrictions;
@property (TB,N) allowRemoteControlLayers;
@property (T@"NSString",N) chromaLocation;
@property (TQ,N) protectionFlags;
@property (TB,N) allowDynamicProtection;
@property (T@,N) encoderEncryptionData;
@property (T@"NSData",N) encoderEncryptionKeyID;
@property (T@"NSString",N) displayUUID;
```

## Instance methods

```
-[FigDisplayConfiguration canvasSize];
-[FigDisplayConfiguration refreshRate];
-[FigDisplayConfiguration preset];
-[FigDisplayConfiguration setClientName:];
-[FigDisplayConfiguration setDisplayLabel:];
-[FigDisplayConfiguration setDisplayMode:];
-[FigDisplayConfiguration init];
-[FigDisplayConfiguration displayUUID];
-[FigDisplayConfiguration dealloc];
-[FigDisplayConfiguration displayMode];
-[FigDisplayConfiguration setToneMappingMode:];
-[FigDisplayConfiguration setDisplayUUID:];
-[FigDisplayConfiguration setCanvasSize:];
-[FigDisplayConfiguration setClientPID:];
-[FigDisplayConfiguration clientName];
-[FigDisplayConfiguration displayLabel];
-[FigDisplayConfiguration toneMappingMode];
-[FigDisplayConfiguration clientPID];
-[FigDisplayConfiguration description];
-[FigDisplayConfiguration pixelFormat];
-[FigDisplayConfiguration setPreset:];
-[FigDisplayConfiguration setPixelFormat:];
-[FigDisplayConfiguration setRefreshRate:];
-[FigDisplayConfiguration setChromaLocation:];
-[FigDisplayConfiguration getLock];
-[FigDisplayConfiguration protectionFlags];
-[FigDisplayConfiguration numOfIdleFrames];
-[FigDisplayConfiguration allowDynamicProtection];
-[FigDisplayConfiguration allowRemoteControlLayers];
-[FigDisplayConfiguration chromaLocation];
-[FigDisplayConfiguration encoderEncryptionData];
-[FigDisplayConfiguration encoderEncryptionKeyID];
-[FigDisplayConfiguration getFVDOptions];
-[FigDisplayConfiguration imagePoolSize];
-[FigDisplayConfiguration maxDisplaySize];
-[FigDisplayConfiguration mirroringRestrictions];
-[FigDisplayConfiguration preferredUIScaleFactor];
-[FigDisplayConfiguration setAllowDynamicProtection:];
-[FigDisplayConfiguration setAllowRemoteControlLayers:];
-[FigDisplayConfiguration setEncoderEncryptionData:];
-[FigDisplayConfiguration setEncoderEncryptionKeyID:];
-[FigDisplayConfiguration setImagePoolSize:];
-[FigDisplayConfiguration setMaxDisplaySize:];
-[FigDisplayConfiguration setMirroringRestrictions:];
-[FigDisplayConfiguration setNumOfIdleFrames:];
-[FigDisplayConfiguration setPreferredUIScaleFactor:];
-[FigDisplayConfiguration setProtectionFlags:];
-[FigDisplayConfiguration setUseExtendedColor:];
-[FigDisplayConfiguration useExtendedColor];
```
