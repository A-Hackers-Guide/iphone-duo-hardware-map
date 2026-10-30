# `FigCaptureSessionObservatory`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 6 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"NSMapTable" _captureSessionsStorage;
@"NSHashTable" _registeredObservers;
@"NSObject<OS_dispatch_queue>" _queue;
q _lastRunningIdentifier;
@"FigCaptureSessionAttachedSessionManager" _attachedSessionManager;
@"FigCaptureOSStateHandle" _osStateHandle;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureSessionObservatory initialize];
+[FigCaptureSessionObservatory sharedObservatory];
```

## Instance methods

```
-[FigCaptureSessionObservatory osStatePropertyList];
-[FigCaptureSessionObservatory init];
-[FigCaptureSessionObservatory dealloc];
-[FigCaptureSessionObservatory registerObserver:];
-[FigCaptureSessionObservatory unregisterObserver:];
-[FigCaptureSessionObservatory attachSessionToHostSession:];
-[FigCaptureSessionObservatory captureSessionInvalidated:];
-[FigCaptureSessionObservatory captureSessionWasCreated:];
-[FigCaptureSessionObservatory handleSessionNotificationWhileClientDeattached:notificationName:notificationPayload:];
```
