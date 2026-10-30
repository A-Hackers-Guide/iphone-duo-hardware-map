# `BWDeferredCaptureAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 5 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
i _error;
i _processingType;
B _fileBacked;
I _commitDurationInMilliseconds;
I _flushDurationInMilliseconds;
```

## Properties

```
@property (Ti,N,V_error) error;
@property (Ti,N,V_processingType) processingType;
@property (TB,N,V_fileBacked) fileBacked;
@property (TI,N,V_commitDurationInMilliseconds) commitDurationInMilliseconds;
@property (TI,N,V_flushDurationInMilliseconds) flushDurationInMilliseconds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWDeferredCaptureAnalyticsPayload setError:];
-[BWDeferredCaptureAnalyticsPayload eventDictionary];
-[BWDeferredCaptureAnalyticsPayload init];
-[BWDeferredCaptureAnalyticsPayload dealloc];
-[BWDeferredCaptureAnalyticsPayload reset];
-[BWDeferredCaptureAnalyticsPayload error];
-[BWDeferredCaptureAnalyticsPayload eventName];
-[BWDeferredCaptureAnalyticsPayload setFlushDurationInMilliseconds:];
-[BWDeferredCaptureAnalyticsPayload commitDurationInMilliseconds];
-[BWDeferredCaptureAnalyticsPayload fileBacked];
-[BWDeferredCaptureAnalyticsPayload flushDurationInMilliseconds];
-[BWDeferredCaptureAnalyticsPayload processingType];
-[BWDeferredCaptureAnalyticsPayload setCommitDurationInMilliseconds:];
-[BWDeferredCaptureAnalyticsPayload setFileBacked:];
-[BWDeferredCaptureAnalyticsPayload setProcessingType:];
```
