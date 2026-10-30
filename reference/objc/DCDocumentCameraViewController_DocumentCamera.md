# `DCDocumentCameraViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 2 instance variables, 2 properties, 8 instance methods, 4 class methods

## Instance variables

```
@"UIViewController" _childViewController;
@"<DCDocumentCameraViewControllerDelegate>" _docCamDelegate;
```

## Properties

```
@property (T@"UIViewController",&,N,SsetChildViewController:,V_childViewController) childViewController;
@property (T@"<DCDocumentCameraViewControllerDelegate>",W,N,V_docCamDelegate) docCamDelegate;
```

## Class methods

```
+[DCDocumentCameraViewController isAvailable];
+[DCDocumentCameraViewController defaultViewControllerWithDelegate:];
+[DCDocumentCameraViewController inProcessViewControllerWithDelegate:];
+[DCDocumentCameraViewController viewServiceViewControllerWithDelegate:];
```

## Instance methods

```
-[DCDocumentCameraViewController initWithDelegate:];
-[DCDocumentCameraViewController initWithNibName:bundle:];
-[DCDocumentCameraViewController initWithCoder:];
-[DCDocumentCameraViewController childViewController];
-[DCDocumentCameraViewController setChildViewController:];
-[DCDocumentCameraViewController docCamDelegate];
-[DCDocumentCameraViewController initWithDelegate:childViewController:];
-[DCDocumentCameraViewController setDocCamDelegate:];
```
