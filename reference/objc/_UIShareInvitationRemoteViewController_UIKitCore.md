# `_UIShareInvitationRemoteViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- Protocols: `_UIShareInvitationViewControllerHost`
- 1 instance variables, 5 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"UIViewController<_UISharingPublicController>" _publicController;
```

## Properties

```
@property (T@"UIViewController<_UISharingPublicController>",W,N,V_publicController) publicController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIShareInvitationRemoteViewController exportedInterface];
+[_UIShareInvitationRemoteViewController serviceViewControllerInterface];
```

## Instance methods

```
-[_UIShareInvitationRemoteViewController viewServiceDidTerminateWithError:];
-[_UIShareInvitationRemoteViewController viewDidLoad];
-[_UIShareInvitationRemoteViewController viewWillLayoutSubviews];
-[_UIShareInvitationRemoteViewController didMoveToParentViewController:];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidActivateAddPeopleWithRemoteSourceX:y:width:height:];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidActivateAddPeopleWithRemoteSourceX:y:width:height:allowedSharingOptions:];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidActivateShowActivityController];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidActivateShowSharedFolder];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidChooseTransport:];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidModifyPrimarySwitch:];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidModifySecondarySwitch:];
-[_UIShareInvitationRemoteViewController _cloudSharingControllerDidUpdateRootFolderURL:];
-[_UIShareInvitationRemoteViewController _dismissAndRepresentForActivity:];
-[_UIShareInvitationRemoteViewController _dismissForActivityRepresentation:];
-[_UIShareInvitationRemoteViewController _dismissViewController];
-[_UIShareInvitationRemoteViewController _dismissViewControllerWithError:];
-[_UIShareInvitationRemoteViewController _performAuxiliaryActionWithCompletion:];
-[_UIShareInvitationRemoteViewController _performHeaderActionWithCompletion:];
-[_UIShareInvitationRemoteViewController _representFullscreenAfterActivityDismissal:];
-[_UIShareInvitationRemoteViewController _requestContentSize:];
-[_UIShareInvitationRemoteViewController _requestSavedShareWithCompletion:];
-[_UIShareInvitationRemoteViewController _shareDidChange:];
-[_UIShareInvitationRemoteViewController _shareWasMadePrivate];
-[_UIShareInvitationRemoteViewController _tintColorDidChangeToColor:];
-[_UIShareInvitationRemoteViewController _updateTraitCollectionForPopoverStatus];
-[_UIShareInvitationRemoteViewController _upgradeShare];
-[_UIShareInvitationRemoteViewController publicController];
-[_UIShareInvitationRemoteViewController setPublicController:];
```
