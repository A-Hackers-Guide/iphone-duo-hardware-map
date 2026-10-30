# `FigCaptureAncillaryDataEncoder`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _ancillaryData;
@"NSData" _lensData;
@"NSData" _cameraData;
@"NSData" _userData;
@"FigCaptureAncillaryDataHIDTransmitter" _HIDTransmitter;
B _HIDTransmitterReady;
B _shouldSendHIDData;
B _enabled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Class methods

```
+[FigCaptureAncillaryDataEncoder initialize];
```

## Instance methods

```
-[FigCaptureAncillaryDataEncoder init];
-[FigCaptureAncillaryDataEncoder dealloc];
-[FigCaptureAncillaryDataEncoder removeRDD18AncillaryDataForTag:];
-[FigCaptureAncillaryDataEncoder setRDD18AncillaryData:forTag:error:];
-[FigCaptureAncillaryDataEncoder _combineAllAncillaryDataForHID];
-[FigCaptureAncillaryDataEncoder _removeRDD18AncillaryDataForTag_locked:];
-[FigCaptureAncillaryDataEncoder _setRDD18AncillaryData_locked:forTag:error:];
-[FigCaptureAncillaryDataEncoder accumulateCameraAncillaryDataForSampleBuffer:];
-[FigCaptureAncillaryDataEncoder accumulateLensAncillaryDataForSampleBuffer:];
-[FigCaptureAncillaryDataEncoder createVANCPacketWithPSC:payload:];
-[FigCaptureAncillaryDataEncoder decodeBool:];
-[FigCaptureAncillaryDataEncoder encodeCameraAncillaryData];
-[FigCaptureAncillaryDataEncoder encodeForVANC];
-[FigCaptureAncillaryDataEncoder encodeHalfFloat:];
-[FigCaptureAncillaryDataEncoder encodeLensAncillaryData];
-[FigCaptureAncillaryDataEncoder encodeRationalWithNumerator:denominator:];
-[FigCaptureAncillaryDataEncoder encodeUserData];
-[FigCaptureAncillaryDataEncoder encodedAncillaryDataForHID];
-[FigCaptureAncillaryDataEncoder encodedAncillaryDataPacket];
-[FigCaptureAncillaryDataEncoder processSampleBuffer:forInput:];
-[FigCaptureAncillaryDataEncoder processUserAncillaryData:];
-[FigCaptureAncillaryDataEncoder sendAncillaryDataViaHID];
-[FigCaptureAncillaryDataEncoder setupHIDTransmitter];
-[FigCaptureAncillaryDataEncoder updateValue:forTag:];
```
