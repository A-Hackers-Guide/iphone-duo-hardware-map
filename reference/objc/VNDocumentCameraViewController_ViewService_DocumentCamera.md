# `VNDocumentCameraViewController_ViewService`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VNDocumentCameraViewController`
- Protocols: `BKSAccelerometerDelegate`, `DCDocumentCameraPublicViewController`
- 2 instance variables, 8 properties, 23 instance methods, 0 class methods

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
-[VNDocumentCameraViewController_ViewService didFailWithError:];
-[VNDocumentCameraViewController_ViewService dismiss];
-[VNDocumentCameraViewController_ViewService init];
-[VNDocumentCameraViewController_ViewService dealloc];
-[VNDocumentCameraViewController_ViewService remoteViewController];
-[VNDocumentCameraViewController_ViewService viewDidLoad];
-[VNDocumentCameraViewController_ViewService accelerometer:didChangeDeviceOrientation:];
-[VNDocumentCameraViewController_ViewService setType:];
-[VNDocumentCameraViewController_ViewService type];
-[VNDocumentCameraViewController_ViewService didCancel];
-[VNDocumentCameraViewController_ViewService accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:];
-[VNDocumentCameraViewController_ViewService childViewControllerForPreferredContainerBackgroundStyle];
-[VNDocumentCameraViewController_ViewService preferredContainerBackgroundStyle];
-[VNDocumentCameraViewController_ViewService accelerometer];
-[VNDocumentCameraViewController_ViewService setAccelerometer:];
-[VNDocumentCameraViewController_ViewService extrudeQuadByPercentage:];
-[VNDocumentCameraViewController_ViewService removeSaveActionBlockerForFiles];
-[VNDocumentCameraViewController_ViewService castedChildViewController];
-[VNDocumentCameraViewController_ViewService didFinishWithDocumentInfoCollection:];
-[VNDocumentCameraViewController_ViewService setViewServiceSession:];
-[VNDocumentCameraViewController_ViewService viewServicePreferredSizeDidChange:];
-[VNDocumentCameraViewController_ViewService viewServiceSession];
-[VNDocumentCameraViewController_ViewService viewServiceViewController];
```
