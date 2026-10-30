# `FigScreenCaptureConfiguration`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 21 properties, 47 instance methods, 0 class methods

## Instance variables

```
^{__CFDictionary=} _fvdOptions;
^{OpaqueFigSimpleMutex=} _lock;
Q _preset;
```

## Properties

```
@property (T{CGSize=dd},N) size;
@property (T{?=qiIq},N) minFrameInterval;
@property (TI,N) pixelFormat;
@property (TQ,N) preset;
@property (TB,N) useExtendedColor;
@property (Tq,N) numOfIdleFrames;
@property (Tq,N) imagePoolSize;
@property (T@"NSString",N) clientName;
@property (T@,N) contentIDs;
@property (TB,N) includePrivateContent;
@property (Tq,N) displayID;
@property (TQ,N) toneMappingMode;
@property (TQ,N) mirroringRestrictions;
@property (TB,N) fillDisplay;
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
-[FigScreenCaptureConfiguration setDisplayID:];
-[FigScreenCaptureConfiguration preset];
-[FigScreenCaptureConfiguration setClientName:];
-[FigScreenCaptureConfiguration init];
-[FigScreenCaptureConfiguration displayUUID];
-[FigScreenCaptureConfiguration dealloc];
-[FigScreenCaptureConfiguration displayID];
-[FigScreenCaptureConfiguration setToneMappingMode:];
-[FigScreenCaptureConfiguration size];
-[FigScreenCaptureConfiguration setDisplayUUID:];
-[FigScreenCaptureConfiguration clientName];
-[FigScreenCaptureConfiguration toneMappingMode];
-[FigScreenCaptureConfiguration description];
-[FigScreenCaptureConfiguration pixelFormat];
-[FigScreenCaptureConfiguration setPreset:];
-[FigScreenCaptureConfiguration setPixelFormat:];
-[FigScreenCaptureConfiguration setSize:];
-[FigScreenCaptureConfiguration setChromaLocation:];
-[FigScreenCaptureConfiguration getLock];
-[FigScreenCaptureConfiguration protectionFlags];
-[FigScreenCaptureConfiguration setFillDisplay:];
-[FigScreenCaptureConfiguration numOfIdleFrames];
-[FigScreenCaptureConfiguration allowDynamicProtection];
-[FigScreenCaptureConfiguration allowRemoteControlLayers];
-[FigScreenCaptureConfiguration chromaLocation];
-[FigScreenCaptureConfiguration contentIDs];
-[FigScreenCaptureConfiguration encoderEncryptionData];
-[FigScreenCaptureConfiguration encoderEncryptionKeyID];
-[FigScreenCaptureConfiguration fillDisplay];
-[FigScreenCaptureConfiguration getFVDOptions];
-[FigScreenCaptureConfiguration imagePoolSize];
-[FigScreenCaptureConfiguration includePrivateContent];
-[FigScreenCaptureConfiguration minFrameInterval];
-[FigScreenCaptureConfiguration mirroringRestrictions];
-[FigScreenCaptureConfiguration setAllowDynamicProtection:];
-[FigScreenCaptureConfiguration setAllowRemoteControlLayers:];
-[FigScreenCaptureConfiguration setContentIDs:];
-[FigScreenCaptureConfiguration setEncoderEncryptionData:];
-[FigScreenCaptureConfiguration setEncoderEncryptionKeyID:];
-[FigScreenCaptureConfiguration setImagePoolSize:];
-[FigScreenCaptureConfiguration setIncludePrivateContent:];
-[FigScreenCaptureConfiguration setMinFrameInterval:];
-[FigScreenCaptureConfiguration setMirroringRestrictions:];
-[FigScreenCaptureConfiguration setNumOfIdleFrames:];
-[FigScreenCaptureConfiguration setProtectionFlags:];
-[FigScreenCaptureConfiguration setUseExtendedColor:];
-[FigScreenCaptureConfiguration useExtendedColor];
```
