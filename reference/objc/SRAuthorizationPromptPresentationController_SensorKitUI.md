# `SRAuthorizationPromptPresentationController`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRRemoteAuthorizationPromptViewControllerDelegate`
- 6 instance variables, 10 properties, 31 instance methods, 2 class methods

## Instance variables

```
B _presenting;
B _hostNavigationBarHidden;
@"UIViewController<SRRemoteAuthorizationPromptViewController>" _viewController;
@? _completionHandler;
@"NSError" _error;
q _reason;
```

## Properties

```
@property (T@"UIViewController<SRRemoteAuthorizationPromptViewController>",&,N,V_viewController) viewController;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TB,N,GisPresenting,V_presenting) presenting;
@property (TB,N,V_hostNavigationBarHidden) hostNavigationBarHidden;
@property (T@"NSError",&,N,V_error) error;
@property (Tq,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRAuthorizationPromptPresentationController sharedInstance];
+[SRAuthorizationPromptPresentationController initialize];
```

## Instance methods

```
-[SRAuthorizationPromptPresentationController setViewController:];
-[SRAuthorizationPromptPresentationController setError:];
-[SRAuthorizationPromptPresentationController setCompletionHandler:];
-[SRAuthorizationPromptPresentationController completionHandler];
-[SRAuthorizationPromptPresentationController dealloc];
-[SRAuthorizationPromptPresentationController setReason:];
-[SRAuthorizationPromptPresentationController error];
-[SRAuthorizationPromptPresentationController viewController];
-[SRAuthorizationPromptPresentationController reason];
-[SRAuthorizationPromptPresentationController isPresenting];
-[SRAuthorizationPromptPresentationController setPresenting:];
-[SRAuthorizationPromptPresentationController presentationAnchor];
-[SRAuthorizationPromptPresentationController presentAppsAndStudiesPromptViewController:completionHandler:];
-[SRAuthorizationPromptPresentationController presentFirstRunOnboardingViewController:completionHandler:];
-[SRAuthorizationPromptPresentationController presentMigrationPromptViewController:withDesiredServices:bundleIdentifier:completionHandler:];
-[SRAuthorizationPromptPresentationController presentPromptViewController:withDesiredServices:bundleIdentifier:completionHandler:];
-[SRAuthorizationPromptPresentationController presentResearchDataViewController:completionHandler:];
-[SRAuthorizationPromptPresentationController presentStudyAuthorizationPromptViewController:bundlePath:completionHandler:];
-[SRAuthorizationPromptPresentationController authorizationRequestCompleted];
-[SRAuthorizationPromptPresentationController authorizationRequestDidDisappear];
-[SRAuthorizationPromptPresentationController authorizationRequestFailedWithError:];
-[SRAuthorizationPromptPresentationController authorizationRequestWillDisappear];
-[SRAuthorizationPromptPresentationController authorizationUIReadyForDisplayModally:];
-[SRAuthorizationPromptPresentationController completePromptWithError:];
-[SRAuthorizationPromptPresentationController hostNavigationBarHidden];
-[SRAuthorizationPromptPresentationController isViewControllerPresentedModally];
-[SRAuthorizationPromptPresentationController navigationControllerFromRoot:];
-[SRAuthorizationPromptPresentationController presentAnyViewController:reason:completionHandler:];
-[SRAuthorizationPromptPresentationController presentingViewControllerFromRoot:];
-[SRAuthorizationPromptPresentationController setHostNavigationBarHidden:];
-[SRAuthorizationPromptPresentationController viewControllerCleanUp];
```
