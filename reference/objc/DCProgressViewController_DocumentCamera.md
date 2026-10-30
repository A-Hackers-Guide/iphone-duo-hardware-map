# `DCProgressViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 6 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _showsCancel;
@"NSProgress" _observedProgress;
@"<DCProgressViewControllerDelegate>" _progressDelegate;
@"UILabel" _label;
@"UIActivityIndicatorView" _activityIndicator;
@"DCCircularProgressView" _circularProgressView;
```

## Properties

```
@property (T@"UIActivityIndicatorView",&,N,V_activityIndicator) activityIndicator;
@property (T@"DCCircularProgressView",&,N,V_circularProgressView) circularProgressView;
@property (T@"UILabel",&,N,V_label) label;
@property (T@"NSProgress",&,N,V_observedProgress) observedProgress;
@property (TB,N,V_showsCancel) showsCancel;
@property (T@"<DCProgressViewControllerDelegate>",W,N,V_progressDelegate) progressDelegate;
```

## Instance methods

```
-[DCProgressViewController initWithDelegate:];
-[DCProgressViewController viewWillDisappear:];
-[DCProgressViewController label];
-[DCProgressViewController setLabel:];
-[DCProgressViewController activityIndicator];
-[DCProgressViewController viewDidLoad];
-[DCProgressViewController viewWillAppear:];
-[DCProgressViewController _canShowWhileLocked];
-[DCProgressViewController observedProgress];
-[DCProgressViewController setActivityIndicator:];
-[DCProgressViewController setObservedProgress:];
-[DCProgressViewController progressDelegate];
-[DCProgressViewController setProgressDelegate:];
-[DCProgressViewController setShowsCancel:];
-[DCProgressViewController circularProgressView];
-[DCProgressViewController setCircularProgressView:];
-[DCProgressViewController showsCancel];
```
