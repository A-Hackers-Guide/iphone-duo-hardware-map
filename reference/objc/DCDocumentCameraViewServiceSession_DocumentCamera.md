# `DCDocumentCameraViewServiceSession`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
i _viewServicePid;
@"DCDocumentCameraViewServiceSessionRequest" _sessionRequest;
@"ICDocCamImageCache" _docCamImageCache;
```

## Properties

```
@property (T@"DCDocumentCameraViewServiceSessionRequest",R,N,V_sessionRequest) sessionRequest;
@property (Ti,R,N,V_viewServicePid) viewServicePid;
@property (T@"ICDocCamImageCache",R,N,V_docCamImageCache) docCamImageCache;
```

## Class methods

```
+[DCDocumentCameraViewServiceSession supportsSecureCoding];
```

## Instance methods

```
-[DCDocumentCameraViewServiceSession setup];
-[DCDocumentCameraViewServiceSession encodeWithCoder:];
-[DCDocumentCameraViewServiceSession initWithCoder:];
-[DCDocumentCameraViewServiceSession sessionRequest];
-[DCDocumentCameraViewServiceSession docCamImageCache];
-[DCDocumentCameraViewServiceSession initWithSessionRequest:];
-[DCDocumentCameraViewServiceSession viewServicePid];
```
