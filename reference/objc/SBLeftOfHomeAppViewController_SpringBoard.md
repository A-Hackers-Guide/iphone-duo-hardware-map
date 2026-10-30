# `SBLeftOfHomeAppViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBHVisibleContentPresenter`, `SBApplicationHosting`
- 3 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
Q _contentVisibility;
@"SBAppViewController" _appViewController;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"SBAppViewController",&,N,V_appViewController) appViewController;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (TQ,N,V_contentVisibility) contentVisibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBLeftOfHomeAppViewController isEnabled];
```

## Instance methods

```
-[SBLeftOfHomeAppViewController applicationController];
-[SBLeftOfHomeAppViewController initWithApplicationController:];
-[SBLeftOfHomeAppViewController setApplicationController:];
-[SBLeftOfHomeAppViewController viewDidLoad];
-[SBLeftOfHomeAppViewController handlesRotationIndependentOfCoverSheet];
-[SBLeftOfHomeAppViewController hostedAppWillRotateToInterfaceOrientation:];
-[SBLeftOfHomeAppViewController conformsToSBApplicationHosting];
-[SBLeftOfHomeAppViewController setHostedAppReferenceSize:withInterfaceOrientation:];
-[SBLeftOfHomeAppViewController hostedAppSceneHandle];
-[SBLeftOfHomeAppViewController contentVisibility];
-[SBLeftOfHomeAppViewController canHostAnApp];
-[SBLeftOfHomeAppViewController setContentVisibility:];
-[SBLeftOfHomeAppViewController hostedAppSceneHandles];
-[SBLeftOfHomeAppViewController isHostingAnApp];
-[SBLeftOfHomeAppViewController appViewController];
-[SBLeftOfHomeAppViewController setAppViewController:];
```
