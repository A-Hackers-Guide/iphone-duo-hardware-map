# `BWFigCaptureDevice`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFigCaptureISPProcessingSessionDelegate`
- 14 instance variables, 10 properties, 30 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureDevice=} _device;
q _uniqueID;
@"NSString" _deviceID;
@"NSDictionary" _supportedProperties;
@"NSDictionary" _streamsByPortType;
@"NSArray" _streams;
@"BWFigCaptureStreamsMapper" _streamsMapper;
@"NSArray" _synchronizedStreamsGroups;
@"NSArray" _figCaptureSynchronizedStreamsGroups;
@"NSMutableArray" _activeProcessingSessions;
B _invalidated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
I _ktraceCodePrefix;
@"NSString" _loggingPrefix;
```

## Properties

```
@property (Tq,R,V_uniqueID) uniqueID;
@property (T@"NSString",R,V_deviceID) deviceID;
@property (T@"NSDictionary",R,V_supportedProperties) supportedProperties;
@property (T@"NSArray",R,V_streams) streams;
@property (T@"NSArray",R,V_synchronizedStreamsGroups) synchronizedStreamsGroups;
@property (TB,R) invalidated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWFigCaptureDevice initialize];
```

## Instance methods

```
-[BWFigCaptureDevice copyStreamWithPortType:error:];
-[BWFigCaptureDevice processingSessionHasBeenInvalidated:];
-[BWFigCaptureDevice requestControlOfStreams:clientPriority:];
-[BWFigCaptureDevice debugDescription];
-[BWFigCaptureDevice invalidated];
-[BWFigCaptureDevice getPropertyIfSupported:error:];
-[BWFigCaptureDevice deviceID];
-[BWFigCaptureDevice supportsISPProcessingSessionType:error:];
-[BWFigCaptureDevice enqueueReactionEffect:];
-[BWFigCaptureDevice dealloc];
-[BWFigCaptureDevice copyProperty:error:];
-[BWFigCaptureDevice setProperty:value:];
-[BWFigCaptureDevice streams];
-[BWFigCaptureDevice relinquishControlOfStreams:];
-[BWFigCaptureDevice synchronizedStreamsGroups];
-[BWFigCaptureDevice uniqueID];
-[BWFigCaptureDevice invalidate];
-[BWFigCaptureDevice resetSynchronizedStreamsGroups];
-[BWFigCaptureDevice getProperty:error:];
-[BWFigCaptureDevice description];
-[BWFigCaptureDevice copyPropertyIfSupported:error:];
-[BWFigCaptureDevice resetTorchState];
-[BWFigCaptureDevice copyStreamsWithPortTypes:error:];
-[BWFigCaptureDevice setPropertyIfSupported:value:];
-[BWFigCaptureDevice supportedProperties];
-[BWFigCaptureDevice copySynchronizedStreamsGroupForStreams:error:];
-[BWFigCaptureDevice initWithFigCaptureDevice:deviceID:];
-[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:];
-[BWFigCaptureDevice copyISPProcessingSessionWithType:error:];
-[BWFigCaptureDevice postNotificationOnBehalfOfFigCaptureDevice:payload:];
```
