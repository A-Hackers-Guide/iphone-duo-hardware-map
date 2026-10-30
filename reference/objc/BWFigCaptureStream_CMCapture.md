# `BWFigCaptureStream`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 11 properties, 41 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureStream=} _stream;
@"NSString" _portType;
@"NSString" _uniqueID;
B _staticPropertiesCacheEnabled;
@"NSString" _portTypeShortString;
@"NSDictionary" _supportedProperties;
@"NSMutableDictionary" _cachedProperties;
B _calibrationDataSent;
B _invalidated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _streaming;
I _ktraceCodePrefix;
B _createFakeISPMotionData;
@"FigWeakReference" _startStopDelegateWeakReference;
@"NSString" _loggingPrefix;
B _vibeMitigationEnabled;
B _vibeMitigationWhileCameraStreamingSupported;
B _workaroundToTurnTorchOnWhenStreamStartsIfNecessary;
B _workaroundShouldTurnOnTorchWhenNextStreamStarts;
B _cachingPropertiesWhileSuspended;
@"NSMutableArray" _cachedPropertiesWhileSuspended;
@? _reactionsInProgressChangedHandler;
@? _suppressedGestureHandler;
```

## Properties

```
@property (T@"NSString",R,N,V_portType) portType;
@property (T@"NSString",R,N,V_uniqueID) uniqueID;
@property (T@"NSDictionary",R,N,V_supportedProperties) supportedProperties;
@property (T@"<BWFigCaptureStreamStartStopDelegate>",W,N) startStopDelegate;
@property (TB,N,V_calibrationDataSent) calibrationDataSent;
@property (T@?,C,N,V_reactionsInProgressChangedHandler) reactionsInProgressChangedHandler;
@property (T@?,C,N,V_suppressedGestureHandler) suppressedGestureHandler;
@property (TB,N) vibeMitigationEnabled;
@property (TB,N,V_workaroundToTurnTorchOnWhenStreamStartsIfNecessary) workaroundToTurnTorchOnWhenStreamStartsIfNecessary;
@property (TB,R,N,V_streaming) streaming;
@property (TB,N,V_cachingPropertiesWhileSuspended) cachingPropertiesWhileSuspended;
```

## Class methods

```
+[BWFigCaptureStream initialize];
```

## Instance methods

```
-[BWFigCaptureStream didStop];
-[BWFigCaptureStream setWorkaroundToTurnTorchOnWhenStreamStartsIfNecessary:];
-[BWFigCaptureStream portType];
-[BWFigCaptureStream debugDescription];
-[BWFigCaptureStream setCalibrationDataSent:];
-[BWFigCaptureStream getPropertyIfSupported:error:];
-[BWFigCaptureStream addAttachmentsToSampleBuffer:options:];
-[BWFigCaptureStream reactionsInProgressChangedHandler];
-[BWFigCaptureStream stop];
-[BWFigCaptureStream setSuppressedGestureHandler:];
-[BWFigCaptureStream enqueueReactionEffect:];
-[BWFigCaptureStream invalidateWhilePreservingTorchState:];
-[BWFigCaptureStream dealloc];
-[BWFigCaptureStream setCachingPropertiesWhileSuspended:];
-[BWFigCaptureStream copyProperty:error:];
-[BWFigCaptureStream setReactionsInProgressChangedHandler:];
-[BWFigCaptureStream setProperty:value:];
-[BWFigCaptureStream start];
-[BWFigCaptureStream willStop];
-[BWFigCaptureStream workaroundToTurnTorchOnWhenStreamStartsIfNecessary];
-[BWFigCaptureStream setStartStopDelegate:];
-[BWFigCaptureStream initWithFigCaptureStream:deviceID:errOut:];
-[BWFigCaptureStream uniqueID];
-[BWFigCaptureStream unregisterForNotification:listener:];
-[BWFigCaptureStream registerForNotification:listener:callback:];
-[BWFigCaptureStream vibeMitigationEnabled];
-[BWFigCaptureStream flushCachedProperties];
-[BWFigCaptureStream calibrationDataSent];
-[BWFigCaptureStream suppressedGestureHandler];
-[BWFigCaptureStream getProperty:error:];
-[BWFigCaptureStream description];
-[BWFigCaptureStream copyPropertyIfSupported:error:];
-[BWFigCaptureStream sendCommandProperty:];
-[BWFigCaptureStream resetTorchState];
-[BWFigCaptureStream flushPropertyCache];
-[BWFigCaptureStream setVibeMitigationEnabled:];
-[BWFigCaptureStream setPropertyIfSupported:value:];
-[BWFigCaptureStream supportedProperties];
-[BWFigCaptureStream streaming];
-[BWFigCaptureStream startStopDelegate];
-[BWFigCaptureStream cachingPropertiesWhileSuspended];
```
