# `BWStreamStartStopSynchronizer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _streamStatesByPortType;
f _timeoutInSeconds;
B _masterStartedGroupEntered;
@"BWFigVideoCaptureStream" _synchronizationPrimary;
@"NSArray" _synchronizationSlavesOrderedByPriority;
```

## Properties

```
@property (T@"BWFigVideoCaptureStream",R,N,V_synchronizationPrimary) synchronizationPrimary;
@property (TB,N) waitForMasterAEToSettle;
@property (T@"NSArray",&,N) synchronizationSlavesOrderedByPriority;
```

## Class methods

```
+[BWStreamStartStopSynchronizer initialize];
```

## Instance methods

```
-[BWStreamStartStopSynchronizer dealloc];
-[BWStreamStartStopSynchronizer streamWillStop:];
-[BWStreamStartStopSynchronizer streamDidStart:];
-[BWStreamStartStopSynchronizer initWithStreams:synchronizationPrimary:timeoutInSeconds:];
-[BWStreamStartStopSynchronizer setSynchronizationSlavesOrderedByPriority:];
-[BWStreamStartStopSynchronizer setWaitForMasterAEToSettle:];
-[BWStreamStartStopSynchronizer streamDidStop:];
-[BWStreamStartStopSynchronizer streamWillStart:];
-[BWStreamStartStopSynchronizer synchronizationPrimary];
-[BWStreamStartStopSynchronizer synchronizationSlavesOrderedByPriority];
-[BWStreamStartStopSynchronizer waitForMasterAEToSettle];
```
