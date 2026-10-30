# `CMCaptureFrameSenderEndpoints`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _frameSenderEndpoints;
```

## Properties

```
@property (T@"NSDictionary",R,&,N) endpointsByPID;
```

## Instance methods

```
-[CMCaptureFrameSenderEndpoints init];
-[CMCaptureFrameSenderEndpoints dealloc];
-[CMCaptureFrameSenderEndpoints _pruneStalePIDsFromDictionary];
-[CMCaptureFrameSenderEndpoints addEndpoint:endpointUniqueID:endpointType:endpointPID:endpointProxyPID:endpointAuditToken:endpointProxyAuditToken:endpointCameraUniqueID:];
-[CMCaptureFrameSenderEndpoints createXPCArrayOfFrameSenderEndpoints];
-[CMCaptureFrameSenderEndpoints endpointsByPID];
-[CMCaptureFrameSenderEndpoints initWithXPCArrayOfFrameSenderEndpoints:];
-[CMCaptureFrameSenderEndpoints removeAllEndpointsWithPID:];
-[CMCaptureFrameSenderEndpoints removeAllEndpointsWithPID:pruneStalePIDs:];
-[CMCaptureFrameSenderEndpoints removeEndpointWithUniqueID:];
```
