# `CMCaptureLocalSessionOutputStream`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"<CMCaptureLocalSessionOutputStreamSampleBufferReceiver>" _sampleBufferReceiver;
@"CMCaptureLocalSessionVideoConfiguration" _videoConfiguration;
@"NSArray" _associatedSinkIDs;
@"NSMutableSet" _requestedMetadataObjects;
@"NSMutableDictionary" _faceTrackingAttributes;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_requestedMetadataObjects) requestedMetadataObjects;
@property (T@"NSDictionary",&,N,V_faceTrackingAttributes) faceTrackingAttributes;
@property (T@"<CMCaptureLocalSessionOutputStreamSampleBufferReceiver>",R,N,V_sampleBufferReceiver) sampleBufferReceiver;
@property (T@"CMCaptureLocalSessionVideoConfiguration",R,N,V_videoConfiguration) videoConfiguration;
@property (T@"NSArray",R,N,V_associatedSinkIDs) associatedSinkIDs;
```

## Class methods

```
+[CMCaptureLocalSessionOutputStream initialize];
```

## Instance methods

```
-[CMCaptureLocalSessionOutputStream videoConfiguration];
-[CMCaptureLocalSessionOutputStream _handleLocalQueueMessage:];
-[CMCaptureLocalSessionOutputStream dealloc];
-[CMCaptureLocalSessionOutputStream handleNotification:payload:];
-[CMCaptureLocalSessionOutputStream _copyMetadataOnlySampleBufferFromSampleBuffer:];
-[CMCaptureLocalSessionOutputStream associatedSinkIDs];
-[CMCaptureLocalSessionOutputStream faceTrackingAttributes];
-[CMCaptureLocalSessionOutputStream initWithSampleBufferReceiver:];
-[CMCaptureLocalSessionOutputStream prepareForStreamRestartDueToUnrecoverableError];
-[CMCaptureLocalSessionOutputStream requestedMetadataObjects];
-[CMCaptureLocalSessionOutputStream sampleBufferReceiver];
-[CMCaptureLocalSessionOutputStream setFaceTrackingAttributes:];
-[CMCaptureLocalSessionOutputStream setRequestedMetadataObjects:];
```
