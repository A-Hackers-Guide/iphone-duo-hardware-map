# `_UIResilientRemoteViewContainerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 7 instance variables, 7 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"UIViewController" _remoteViewController;
B _delayingDisplayOfRemoteView;
@"NSExtension" _extension;
@"<NSCopying>" _extensionRequestIdentifier;
@"UIViewController" _containedViewController;
@"_UIWaitingForRemoteViewContainerViewController" _waitingController;
@"UIViewController" _errorViewController;
```

## Properties

```
@property (T@"NSExtension",&,N,V_extension) extension;
@property (T@"<NSCopying>",C,N,V_extensionRequestIdentifier) extensionRequestIdentifier;
@property (T@"UIViewController",&,N,V_containedViewController) containedViewController;
@property (T@"_UIWaitingForRemoteViewContainerViewController",&,N,V_waitingController) waitingController;
@property (T@"UIViewController",&,N,V_errorViewController) errorViewController;
@property (TB,N,V_delayingDisplayOfRemoteView) delayingDisplayOfRemoteView;
@property (T@,R,N,V_remoteViewController) remoteViewController;
```

## Class methods

```
+[_UIResilientRemoteViewContainerViewController instantiateWithExtension:completion:];
```

## Instance methods

```
-[_UIResilientRemoteViewContainerViewController preferredContentSizeDidChangeForChildContentContainer:];
-[_UIResilientRemoteViewContainerViewController dealloc];
-[_UIResilientRemoteViewContainerViewController remoteViewController];
-[_UIResilientRemoteViewContainerViewController invalidate];
-[_UIResilientRemoteViewContainerViewController viewDidAppear:];
-[_UIResilientRemoteViewContainerViewController viewWillLayoutSubviews];
-[_UIResilientRemoteViewContainerViewController extension];
-[_UIResilientRemoteViewContainerViewController _defaultInitialViewFrame];
-[_UIResilientRemoteViewContainerViewController setExtension:];
-[_UIResilientRemoteViewContainerViewController setDelayingDisplayOfRemoteView:];
-[_UIResilientRemoteViewContainerViewController _displayError:];
-[_UIResilientRemoteViewContainerViewController _displayRemoteViewController];
-[_UIResilientRemoteViewContainerViewController containedViewController];
-[_UIResilientRemoteViewContainerViewController delayDisplayOfRemoteController];
-[_UIResilientRemoteViewContainerViewController delayingDisplayOfRemoteView];
-[_UIResilientRemoteViewContainerViewController endDelayingDisplayOfRemoteController];
-[_UIResilientRemoteViewContainerViewController errorViewController];
-[_UIResilientRemoteViewContainerViewController extensionRequestIdentifier];
-[_UIResilientRemoteViewContainerViewController initWithExtension:completion:];
-[_UIResilientRemoteViewContainerViewController setContainedViewController:];
-[_UIResilientRemoteViewContainerViewController setErrorViewController:];
-[_UIResilientRemoteViewContainerViewController setExtensionRequestIdentifier:];
-[_UIResilientRemoteViewContainerViewController setWaitingController:];
-[_UIResilientRemoteViewContainerViewController waitingController];
```
