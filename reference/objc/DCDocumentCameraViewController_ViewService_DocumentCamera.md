# `DCDocumentCameraViewController_ViewService`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DCDocumentCameraViewController`
- Protocols: `BKSAccelerometerDelegate`, `DCDocumentCameraPublicViewController`
- 2 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"DCDocumentCameraViewServiceSession" _viewServiceSession;
@"BKSAccelerometer" _accelerometer;
```

## Properties

```
@property (T@"<DCDocumentCameraViewServiceViewController>",R,N,GviewServiceViewController) viewServiceViewController;
@property (T@"DCDocumentCameraRemoteViewController",R,N,GremoteViewController) remoteViewController;
@property (T@"DCDocumentCameraViewServiceSession",&,N,V_viewServiceSession) viewServiceSession;
@property (T@"BKSAccelerometer",&,N,V_accelerometer) accelerometer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DCDocumentCameraViewController_ViewService didFailWithError:];
-[DCDocumentCameraViewController_ViewService initWithDelegate:];
-[DCDocumentCameraViewController_ViewService dismiss];
-[DCDocumentCameraViewController_ViewService dealloc];
-[DCDocumentCameraViewController_ViewService remoteViewController];
-[DCDocumentCameraViewController_ViewService viewDidLoad];
-[DCDocumentCameraViewController_ViewService accelerometer:didChangeDeviceOrientation:];
-[DCDocumentCameraViewController_ViewService didCancel];
-[DCDocumentCameraViewController_ViewService accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:];
-[DCDocumentCameraViewController_ViewService accelerometer];
-[DCDocumentCameraViewController_ViewService setAccelerometer:];
-[DCDocumentCameraViewController_ViewService castedChildViewController];
-[DCDocumentCameraViewController_ViewService didFinishWithDocumentInfoCollection:];
-[DCDocumentCameraViewController_ViewService setViewServiceSession:];
-[DCDocumentCameraViewController_ViewService viewServicePreferredSizeDidChange:];
-[DCDocumentCameraViewController_ViewService viewServiceSession];
-[DCDocumentCameraViewController_ViewService viewServiceViewController];
```
