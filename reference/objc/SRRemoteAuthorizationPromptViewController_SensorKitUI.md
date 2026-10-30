# `SRRemoteAuthorizationPromptViewController`

- Image: [`/System/Library/PrivateFrameworks/SensorKitUI.framework/SensorKitUI`](../userland/System__Library__PrivateFrameworks__SensorKitUI.framework__SensorKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- Protocols: `SRAuthorizationPromptClientInterface`, `SRRemoteAuthorizationPromptViewController`
- 3 instance variables, 7 properties, 24 instance methods, 4 class methods

## Instance variables

```
@"<SRRemoteAuthorizationPromptViewControllerDelegate>" _delegate;
@"<NSCopying>" _request;
@"NSExtension" _weakExtension;
```

## Properties

```
@property (T@"<SRRemoteAuthorizationPromptViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<NSCopying>",&,N,V_request) request;
@property (T@"NSExtension",W,N,V_weakExtension) weakExtension;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRRemoteAuthorizationPromptViewController requestViewControllerWithCompletionHandler:];
+[SRRemoteAuthorizationPromptViewController initialize];
+[SRRemoteAuthorizationPromptViewController exportedInterface];
+[SRRemoteAuthorizationPromptViewController serviceViewControllerInterface];
```

## Instance methods

```
-[SRRemoteAuthorizationPromptViewController viewWillDisappear:];
-[SRRemoteAuthorizationPromptViewController viewServiceDidTerminateWithError:];
-[SRRemoteAuthorizationPromptViewController dealloc];
-[SRRemoteAuthorizationPromptViewController request];
-[SRRemoteAuthorizationPromptViewController invalidate];
-[SRRemoteAuthorizationPromptViewController setDelegate:];
-[SRRemoteAuthorizationPromptViewController delegate];
-[SRRemoteAuthorizationPromptViewController viewDidDisappear:];
-[SRRemoteAuthorizationPromptViewController setWeakExtension:];
-[SRRemoteAuthorizationPromptViewController weakExtension];
-[SRRemoteAuthorizationPromptViewController setRequest:];
-[SRRemoteAuthorizationPromptViewController serviceViewControllerProxy];
-[SRRemoteAuthorizationPromptViewController authorizationRequestCompleted];
-[SRRemoteAuthorizationPromptViewController authorizationRequestDidDisappear];
-[SRRemoteAuthorizationPromptViewController authorizationRequestFailedWithError:];
-[SRRemoteAuthorizationPromptViewController authorizationRequestWillDisappear];
-[SRRemoteAuthorizationPromptViewController authorizationUIReadyForDisplayModally:];
-[SRRemoteAuthorizationPromptViewController deleteAllSamples];
-[SRRemoteAuthorizationPromptViewController requestAuthorizationForBundle:services:];
-[SRRemoteAuthorizationPromptViewController requestAuthorizationMigrationForBundle:services:];
-[SRRemoteAuthorizationPromptViewController showAppsAndStudies];
-[SRRemoteAuthorizationPromptViewController showFirstRunOnboarding];
-[SRRemoteAuthorizationPromptViewController showResearchData];
-[SRRemoteAuthorizationPromptViewController showStudyAuthorizationForBundlePath:];
```
