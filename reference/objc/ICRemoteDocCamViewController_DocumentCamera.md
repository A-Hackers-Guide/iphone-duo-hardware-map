# `ICRemoteDocCamViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 4 instance variables, 4 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"ICDocCamImageCache" _imageCache;
@"<ICRemoteDocCamViewControllerDelegate>" _delegate;
@"SidecarService" _sidecarService;
@"SidecarRequest" _sidecarRequest;
```

## Properties

```
@property (T@"SidecarService",&,N,V_sidecarService) sidecarService;
@property (T@"SidecarRequest",&,N,V_sidecarRequest) sidecarRequest;
@property (T@"ICDocCamImageCache",&,N,V_imageCache) imageCache;
@property (T@"<ICRemoteDocCamViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[ICRemoteDocCamViewController setImageCache:];
-[ICRemoteDocCamViewController observeValueForKeyPath:ofObject:change:context:];
-[ICRemoteDocCamViewController viewDidLoad];
-[ICRemoteDocCamViewController _canShowWhileLocked];
-[ICRemoteDocCamViewController setDelegate:];
-[ICRemoteDocCamViewController viewDidAppear:];
-[ICRemoteDocCamViewController imageCache];
-[ICRemoteDocCamViewController delegate];
-[ICRemoteDocCamViewController initWithImageCache:];
-[ICRemoteDocCamViewController cancelSidecarRequest];
-[ICRemoteDocCamViewController makeAlertControllerForError:];
-[ICRemoteDocCamViewController makeDevicesAlertController];
-[ICRemoteDocCamViewController makeNoDevicesAlertController];
-[ICRemoteDocCamViewController makeProgressAlertControllerForDevice:];
-[ICRemoteDocCamViewController makeSidecarRequestToDevice:];
-[ICRemoteDocCamViewController progressAlertMessageForDevice:];
-[ICRemoteDocCamViewController setSidecarRequest:];
-[ICRemoteDocCamViewController setSidecarService:];
-[ICRemoteDocCamViewController sidecarRequest];
-[ICRemoteDocCamViewController sidecarRequestDidFinish];
-[ICRemoteDocCamViewController sidecarService];
```
