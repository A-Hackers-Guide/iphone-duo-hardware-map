# `BWVisionRequestInferenceDescriptor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
# _requestClass;
@"VNProcessingDevice" _processingDevice;
q _ioSurfaceMemoryPoolId;
Q _revision;
```

## Properties

```
@property (T#,R,N,V_requestClass) requestClass;
@property (TQ,R,N,V_revision) revision;
@property (T@"VNProcessingDevice",R,&,N,V_processingDevice) processingDevice;
@property (Tq,R,N,V_ioSurfaceMemoryPoolId) ioSurfaceMemoryPoolId;
@property (T@"NSString",R,N) requestCacheKey;
```

## Class methods

```
+[BWVisionRequestInferenceDescriptor initialize];
```

## Instance methods

```
-[BWVisionRequestInferenceDescriptor revision];
-[BWVisionRequestInferenceDescriptor dealloc];
-[BWVisionRequestInferenceDescriptor requestCacheKey];
-[BWVisionRequestInferenceDescriptor hash];
-[BWVisionRequestInferenceDescriptor description];
-[BWVisionRequestInferenceDescriptor copyWithZone:];
-[BWVisionRequestInferenceDescriptor isEqual:];
-[BWVisionRequestInferenceDescriptor ioSurfaceMemoryPoolId];
-[BWVisionRequestInferenceDescriptor processingDevice];
-[BWVisionRequestInferenceDescriptor requestClass];
-[BWVisionRequestInferenceDescriptor initWithRequestClass:processingDevice:ioSurfaceMemoryPoolId:revision:];
```
