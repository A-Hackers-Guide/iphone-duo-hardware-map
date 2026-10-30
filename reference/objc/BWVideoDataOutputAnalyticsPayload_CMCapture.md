# `BWVideoDataOutputAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 15 instance variables, 19 properties, 35 instance methods, 0 class methods

## Instance variables

```
i _deviceMask;
i _devicePosition;
B _videoMirrored;
@"NSString" _clientApplicationID;
d _duration;
f _nominalFramerate;
i _height;
i _width;
B _hdrVideo;
B _proresVideo;
i _colorSpace;
Q _numberOfFramesDropped;
Q _numberOfISPFramesDropped;
Q _numberOfFrames;
I _pixelFormat;
```

## Properties

```
@property (Ti,N,V_deviceMask) deviceMask;
@property (Ti,N,V_devicePosition) devicePosition;
@property (TB,N,V_videoMirrored) videoMirrored;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (Td,N,V_duration) duration;
@property (Tf,N,V_nominalFramerate) nominalFramerate;
@property (Ti,N,V_height) height;
@property (Ti,N,V_width) width;
@property (TB,N,V_hdrVideo) hdrVideo;
@property (TB,N,V_proresVideo) proresVideo;
@property (TQ,N,V_numberOfFramesDropped) numberOfFramesDropped;
@property (TQ,N,V_numberOfISPFramesDropped) numberOfISPFramesDropped;
@property (TQ,N,V_numberOfFrames) numberOfFrames;
@property (Ti,N,V_colorSpace) colorSpace;
@property (TI,N,V_pixelFormat) pixelFormat;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWVideoDataOutputAnalyticsPayload proresVideo];
-[BWVideoDataOutputAnalyticsPayload nominalFramerate];
-[BWVideoDataOutputAnalyticsPayload eventDictionary];
-[BWVideoDataOutputAnalyticsPayload setColorSpace:];
-[BWVideoDataOutputAnalyticsPayload hdrVideo];
-[BWVideoDataOutputAnalyticsPayload setVideoMirrored:];
-[BWVideoDataOutputAnalyticsPayload init];
-[BWVideoDataOutputAnalyticsPayload setHdrVideo:];
-[BWVideoDataOutputAnalyticsPayload dealloc];
-[BWVideoDataOutputAnalyticsPayload setNumberOfISPFramesDropped:];
-[BWVideoDataOutputAnalyticsPayload reset];
-[BWVideoDataOutputAnalyticsPayload setNumberOfFramesDropped:];
-[BWVideoDataOutputAnalyticsPayload setClientApplicationID:];
-[BWVideoDataOutputAnalyticsPayload duration];
-[BWVideoDataOutputAnalyticsPayload colorSpace];
-[BWVideoDataOutputAnalyticsPayload eventName];
-[BWVideoDataOutputAnalyticsPayload setHeight:];
-[BWVideoDataOutputAnalyticsPayload setNominalFramerate:];
-[BWVideoDataOutputAnalyticsPayload devicePosition];
-[BWVideoDataOutputAnalyticsPayload setProresVideo:];
-[BWVideoDataOutputAnalyticsPayload numberOfISPFramesDropped];
-[BWVideoDataOutputAnalyticsPayload videoMirrored];
-[BWVideoDataOutputAnalyticsPayload pixelFormat];
-[BWVideoDataOutputAnalyticsPayload setDuration:];
-[BWVideoDataOutputAnalyticsPayload setWidth:];
-[BWVideoDataOutputAnalyticsPayload width];
-[BWVideoDataOutputAnalyticsPayload setPixelFormat:];
-[BWVideoDataOutputAnalyticsPayload deviceMask];
-[BWVideoDataOutputAnalyticsPayload numberOfFrames];
-[BWVideoDataOutputAnalyticsPayload setDeviceMask:];
-[BWVideoDataOutputAnalyticsPayload height];
-[BWVideoDataOutputAnalyticsPayload numberOfFramesDropped];
-[BWVideoDataOutputAnalyticsPayload setNumberOfFrames:];
-[BWVideoDataOutputAnalyticsPayload setDevicePosition:];
-[BWVideoDataOutputAnalyticsPayload clientApplicationID];
```
