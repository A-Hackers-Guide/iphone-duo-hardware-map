# `BWFigCaptureSynchronizedStreamsGroup`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureSynchronizedStreamsGroup=} _syncGroup;
@"NSDictionary" _supportedProperties;
@"NSMutableDictionary" _cachedProperties;
@"BWFigCaptureStream" _synchronizationMaster;
@"BWFigCaptureStream" _defaultSynchronizationMaster;
B _invalidated;
@"NSArray" _streams;
@"BWFigCaptureStreamsMapper" _streamsMapper;
@"NSArray" _activeStreams;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _stopSupported;
I _ktraceCodePrefix;
B _synchronizationMasterIsConfigurable;
```

## Properties

```
@property (T@"NSDictionary",R,V_supportedProperties) supportedProperties;
@property (T@"NSArray",R,V_streams) streams;
@property (TB,R,V_synchronizationMasterIsConfigurable) synchronizationMasterIsConfigurable;
@property (T@"BWFigCaptureStream",&) synchronizationMaster;
@property (TB,R,V_stopSupported) stopSupported;
```

## Class methods

```
+[BWFigCaptureSynchronizedStreamsGroup initialize];
```

## Instance methods

```
-[BWFigCaptureSynchronizedStreamsGroup initWithFigCaptureSynchronizedStreamsGroup:bwFigCaptureStreams:figCaptureStreams:];
-[BWFigCaptureSynchronizedStreamsGroup setActiveStreams:];
-[BWFigCaptureSynchronizedStreamsGroup synchronizationMasterIsConfigurable];
-[BWFigCaptureSynchronizedStreamsGroup stop];
-[BWFigCaptureSynchronizedStreamsGroup stopSupported];
-[BWFigCaptureSynchronizedStreamsGroup dealloc];
-[BWFigCaptureSynchronizedStreamsGroup copyProperty:error:];
-[BWFigCaptureSynchronizedStreamsGroup setProperty:value:];
-[BWFigCaptureSynchronizedStreamsGroup streams];
-[BWFigCaptureSynchronizedStreamsGroup activeStreams];
-[BWFigCaptureSynchronizedStreamsGroup setMasterStream:slaveConfigurationsByPortType:];
-[BWFigCaptureSynchronizedStreamsGroup invalidate];
-[BWFigCaptureSynchronizedStreamsGroup synchronizationMaster];
-[BWFigCaptureSynchronizedStreamsGroup invalidateCachedProperties];
-[BWFigCaptureSynchronizedStreamsGroup setSynchronizationMaster:];
-[BWFigCaptureSynchronizedStreamsGroup setCameraControlsMasterStream:];
-[BWFigCaptureSynchronizedStreamsGroup getProperty:error:];
-[BWFigCaptureSynchronizedStreamsGroup supportedProperties];
```
