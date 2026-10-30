# `FigCaptureDeferredPhotoProcessorRequest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _applicationID;
@"NSString" _captureRequestIdentifier;
@"NSString" _photoIdentifier;
i _clientPID;
@"FigCaptureDeferredPhotoProcessorRequest" _parent;
@"NSObject<OS_xpc_object>" _message;
I _qosClass;
@"BWDeferredProcessingContainer" _container;
@"NSArray" _photoLibraryThumbnailDimensions;
```

## Properties

```
@property (T@"NSString",R,N,V_applicationID) applicationID;
@property (T@"NSString",R,N,V_captureRequestIdentifier) captureRequestIdentifier;
@property (T@"NSString",R,N,V_photoIdentifier) photoIdentifier;
@property (Ti,R,N,V_clientPID) clientPID;
@property (TI,R,N,V_qosClass) qosClass;
@property (T@"FigCaptureDeferredPhotoProcessorRequest",R,N,V_parent) parent;
@property (T@"BWDeferredProcessingContainer",&,N,V_container) container;
@property (T@"NSArray",&,N,V_photoLibraryThumbnailDimensions) photoLibraryThumbnailDimensions;
```

## Instance methods

```
-[FigCaptureDeferredPhotoProcessorRequest applicationID];
-[FigCaptureDeferredPhotoProcessorRequest dealloc];
-[FigCaptureDeferredPhotoProcessorRequest setContainer:];
-[FigCaptureDeferredPhotoProcessorRequest parent];
-[FigCaptureDeferredPhotoProcessorRequest captureRequestIdentifier];
-[FigCaptureDeferredPhotoProcessorRequest photoIdentifier];
-[FigCaptureDeferredPhotoProcessorRequest photoLibraryThumbnailDimensions];
-[FigCaptureDeferredPhotoProcessorRequest clientPID];
-[FigCaptureDeferredPhotoProcessorRequest hash];
-[FigCaptureDeferredPhotoProcessorRequest description];
-[FigCaptureDeferredPhotoProcessorRequest setPhotoLibraryThumbnailDimensions:];
-[FigCaptureDeferredPhotoProcessorRequest qosClass];
-[FigCaptureDeferredPhotoProcessorRequest isEqual:];
-[FigCaptureDeferredPhotoProcessorRequest container];
-[FigCaptureDeferredPhotoProcessorRequest initWithApplicationID:captureRequstIdentifier:photoIdentifier:clientPID:message:qosClass:parent:];
```
