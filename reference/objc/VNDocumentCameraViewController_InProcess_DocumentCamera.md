# `VNDocumentCameraViewController_InProcess`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VNDocumentCameraViewController`
- Protocols: `ICDocCamViewControllerDelegate`, `ICRemoteDocCamViewControllerDelegate`
- 2 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UIViewController" _viewController;
@"ICDocCamUserInterfaceLayoutHelper" _userInterfaceLayoutHelper;
```

## Properties

```
@property (T@"UIViewController",&,N,V_viewController) viewController;
@property (T@"ICDocCamUserInterfaceLayoutHelper",&,N,V_userInterfaceLayoutHelper) userInterfaceLayoutHelper;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VNDocumentCameraViewController_InProcess setViewController:];
-[VNDocumentCameraViewController_InProcess init];
-[VNDocumentCameraViewController_InProcess viewController];
-[VNDocumentCameraViewController_InProcess setType:];
-[VNDocumentCameraViewController_InProcess type];
-[VNDocumentCameraViewController_InProcess didReceiveMemoryWarning];
-[VNDocumentCameraViewController_InProcess viewWillLayoutSubviews];
-[VNDocumentCameraViewController_InProcess _preferredModalPresentationStyle];
-[VNDocumentCameraViewController_InProcess _autoDismiss];
-[VNDocumentCameraViewController_InProcess preferredContainerBackgroundStyle];
-[VNDocumentCameraViewController_InProcess scanDataDelegateWithIdentifier:];
-[VNDocumentCameraViewController_InProcess documentCameraController:canAddImages:];
-[VNDocumentCameraViewController_InProcess documentCameraController:didFinishWithDocInfoCollection:imageCache:warnUser:];
-[VNDocumentCameraViewController_InProcess documentCameraController:didFinishWithImage:];
-[VNDocumentCameraViewController_InProcess documentCameraControllerCreateDataCryptorIfNecessary];
-[VNDocumentCameraViewController_InProcess documentCameraControllerDidCancel:];
-[VNDocumentCameraViewController_InProcess documentCameraControllerExtrusionIsConstrained:];
-[VNDocumentCameraViewController_InProcess extrudeQuadByPercentage:];
-[VNDocumentCameraViewController_InProcess remoteDocumentCameraController:didFailWithError:];
-[VNDocumentCameraViewController_InProcess remoteDocumentCameraController:didFinishWithInfoCollection:];
-[VNDocumentCameraViewController_InProcess remoteDocumentCameraControllerDidCancel:];
-[VNDocumentCameraViewController_InProcess removeSaveActionBlockerForFiles];
-[VNDocumentCameraViewController_InProcess setUserInterfaceLayoutHelper:];
-[VNDocumentCameraViewController_InProcess userInterfaceLayoutHelper];
```
