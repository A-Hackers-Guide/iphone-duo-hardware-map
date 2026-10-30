# `_UICampoPresentedViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIPassthroughScrollInteractionDelegate`, `_UISceneHostingControllerDelegate`
- 8 instance variables, 12 properties, 33 instance methods, 3 class methods

## Instance variables

```
@"_UIPassthroughScrollInteraction" _paddingDismissalInteraction;
B _isCampoSceneConnected;
B __reroutesTransparentTouchesToPopoverSourceView;
@"_UISceneHostingController" _hostingController;
@ _hostingTokenWrapper;
@"<_UICampoPresentedViewControllerDelegate>" _campoDelegate;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __intelligentAssistantPadding;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __lastOverflowScenePadding;
```

## Properties

```
@property (TB,N,R) _overflowScenePlatterHosting;
@property (T@"_UISceneHostingController",&,N,V_hostingController) hostingController;
@property (T@,&,N,V_hostingTokenWrapper) hostingTokenWrapper;
@property (T@"<_UICampoPresentedViewControllerDelegate>",W,N,V_campoDelegate) campoDelegate;
@property (TB,N,S_setReroutesTransparentTouchesToPopoverSourceView:,V__reroutesTransparentTouchesToPopoverSourceView) _reroutesTransparentTouchesToPopoverSourceView;
@property (T{UIEdgeInsets=dddd},N,S_setIntelligentAssistantPadding:,V__intelligentAssistantPadding) _intelligentAssistantPadding;
@property (TB,N,S_setCampoSceneConnected:,V_isCampoSceneConnected) _isCampoSceneConnected;
@property (T{UIEdgeInsets=dddd},N,V__lastOverflowScenePadding) _lastOverflowScenePadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UICampoPresentedViewController _campoAssistantFieldPreferredContentSizeExcludesPaddingPreference];
+[_UICampoPresentedViewController _campoServicesObservesPaddingChanges];
+[_UICampoPresentedViewController _childPreferredContentSizeIncludesPadding];
```

## Instance methods

```
-[_UICampoPresentedViewController preferredContentSizeDidChangeForChildContentContainer:];
-[_UICampoPresentedViewController viewDidLoad];
-[_UICampoPresentedViewController viewDidLayoutSubviews];
-[_UICampoPresentedViewController passthroughScrollInteractionDidRecognize:atLocation:];
-[_UICampoPresentedViewController viewWillAppear:];
-[_UICampoPresentedViewController hostingController];
-[_UICampoPresentedViewController _canShowWhileLocked];
-[_UICampoPresentedViewController passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UICampoPresentedViewController setupSceneHosting];
-[_UICampoPresentedViewController loadView];
-[_UICampoPresentedViewController setHostingController:];
-[_UICampoPresentedViewController _beginDelayingPresentationUntilSceneSized];
-[_UICampoPresentedViewController _installPaddingDismissalInteraction];
-[_UICampoPresentedViewController _intelligentAssistantPadding];
-[_UICampoPresentedViewController _isCampoSceneConnected];
-[_UICampoPresentedViewController _lastOverflowScenePadding];
-[_UICampoPresentedViewController _layoutOverflowSceneIfNeeded];
-[_UICampoPresentedViewController _overflowScenePlatterHosting];
-[_UICampoPresentedViewController _requiresEarlyInstallationInPopover];
-[_UICampoPresentedViewController _reroutesTransparentTouchesToPopoverSourceView];
-[_UICampoPresentedViewController _setCampoSceneConnected:];
-[_UICampoPresentedViewController _setIntelligentAssistantPadding:];
-[_UICampoPresentedViewController _setLightweightRequestedState:];
-[_UICampoPresentedViewController _setReroutesTransparentTouchesToPopoverSourceView:];
-[_UICampoPresentedViewController _showcaseView];
-[_UICampoPresentedViewController _updateIntelligentAssistantPadding:];
-[_UICampoPresentedViewController campoDelegate];
-[_UICampoPresentedViewController campoDidFinishPresentation];
-[_UICampoPresentedViewController campoDidShowPresentation];
-[_UICampoPresentedViewController hostingTokenWrapper];
-[_UICampoPresentedViewController setCampoDelegate:];
-[_UICampoPresentedViewController setHostingTokenWrapper:];
-[_UICampoPresentedViewController set_lastOverflowScenePadding:];
```
