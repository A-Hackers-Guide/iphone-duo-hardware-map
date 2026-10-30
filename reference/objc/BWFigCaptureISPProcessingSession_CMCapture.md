# `BWFigCaptureISPProcessingSession`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureISPProcessingSession=} _session;
i _type;
@"NSDictionary" _supportedProperties;
@"NSMutableDictionary" _cachedProperties;
@"<BWFigCaptureISPProcessingSessionDelegate>" _delegate;
B _invalidated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (T@"<BWFigCaptureISPProcessingSessionDelegate>",N) delegate;
@property (T@"NSDictionary",R) supportedProperties;
@property (T^{OpaqueFigCaptureISPProcessingSession=},R) figCaptureISPProcessingSession;
@property (Ti,R,N,V_type) type;
```

## Class methods

```
+[BWFigCaptureISPProcessingSession initialize];
```

## Instance methods

```
-[BWFigCaptureISPProcessingSession flush];
-[BWFigCaptureISPProcessingSession dealloc];
-[BWFigCaptureISPProcessingSession copyProperty:error:];
-[BWFigCaptureISPProcessingSession setProperty:value:];
-[BWFigCaptureISPProcessingSession invalidate];
-[BWFigCaptureISPProcessingSession setDelegate:];
-[BWFigCaptureISPProcessingSession type];
-[BWFigCaptureISPProcessingSession delegate];
-[BWFigCaptureISPProcessingSession getProperty:error:];
-[BWFigCaptureISPProcessingSession supportedProperties];
-[BWFigCaptureISPProcessingSession figCaptureISPProcessingSession];
-[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:type:];
-[BWFigCaptureISPProcessingSession prepareWithHandler:];
-[BWFigCaptureISPProcessingSession processBuffer:refCon:outputDescriptors:numOutputDescriptors:parameters:];
```
