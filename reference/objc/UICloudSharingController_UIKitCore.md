# `UICloudSharingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UISharingPublicController`, `UIActionSheetPresentationControllerDelegate`, `_UIRemoteViewControllerContaining`
- 27 instance variables, 30 properties, 87 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" _viewServiceValidSema;
B _shareNeedsDeletion;
B _allowShareUpgrade;
B _primaryAuxiliarySwitchState;
B _secondaryAuxiliarySwitchState;
B _displayedShareIsOwnRoot;
@"<UICloudSharingControllerDelegate>" _delegate;
@"CKShare" _share;
Q _availablePermissions;
@"UIActivityViewController" _activityViewController;
@"_UIResilientRemoteViewContainerViewController" _childViewController;
@"_UIShareInvitationRemoteViewController" _remoteViewController;
@"CKContainer" _container;
@"CKContainerSetupInfo" _containerSetupInfo;
@"NSDictionary" _participantDetails;
@? _preparationHandler;
@"UIViewController" _originalPresentingViewController;
@"UIViewController" _strongReferenceToOurself;
@"NSString" _sectionTitleForAuxiliarySwitches;
@"NSString" _primaryAuxiliarySwitchTitle;
@"NSString" _secondaryAuxiliarySwitchTitle;
@"NSString" _rootFolderTitle;
@"NSString" _folderSubitemName;
@"UIImage" _headerPrimaryImage;
@"UIImage" _headerSecondaryImage;
@"CKSystemSharingUIObserver" _systemSharingUIObserver;
@"<_UICloudSharingControllerDelegate_Internal>" _internalDelegate;
```

## Properties

```
@property (T@"UIActivityViewController",&,N,G_activityViewController,S_setActivityViewController:,V_activityViewController) activityViewController;
@property (T@"_UIResilientRemoteViewContainerViewController",&,N,G_childViewController,S_setChildViewController:,V_childViewController) childViewController;
@property (T@"_UIShareInvitationRemoteViewController",R,N,G_remoteViewController,V_remoteViewController) remoteViewController;
@property (T@"CKShare",&,N,V_share) share;
@property (T@"CKContainer",&,N,V_container) container;
@property (T@"CKContainerSetupInfo",&,N,V_containerSetupInfo) containerSetupInfo;
@property (T@"NSDictionary",&,N,G_participantDetails,S_setParticipantDetails:,V_participantDetails) participantDetails;
@property (T@?,C,N,V_preparationHandler) preparationHandler;
@property (TB,N,G_allowShareUpgrade,S_setAllowShareUpgrade:,V_allowShareUpgrade) allowShareUpgrade;
@property (T@"UIViewController",W,N,G_originalPresentingViewController,S_setOriginalPresentingViewController:,V_originalPresentingViewController) originalPresentingViewController;
@property (T@"UIViewController",&,N,G_strongReferenceToOurself,S_setStrongReferenceToOurself:,V_strongReferenceToOurself) strongReferenceToOurself;
@property (T@"NSString",&,N,G_sectionTitleForAuxiliarySwitches,S_setSectionTitleForAuxiliarySwitches:,V_sectionTitleForAuxiliarySwitches) sectionTitleForAuxiliarySwitches;
@property (T@"NSString",&,N,G_primaryAuxiliarySwitchTitle,S_setPrimaryAuxiliarySwitchTitle:,V_primaryAuxiliarySwitchTitle) primaryAuxiliarySwitchTitle;
@property (TB,N,G_primaryAuxiliarySwitchState,S_setPrimaryAuxiliarySwitchState:,V_primaryAuxiliarySwitchState) primaryAuxiliarySwitchState;
@property (T@"NSString",&,N,G_secondaryAuxiliarySwitchTitle,S_setSecondaryAuxiliarySwitchTitle:,V_secondaryAuxiliarySwitchTitle) secondaryAuxiliarySwitchTitle;
@property (TB,N,G_secondaryAuxiliarySwitchState,S_setSecondaryAuxiliarySwitchState:,V_secondaryAuxiliarySwitchState) secondaryAuxiliarySwitchState;
@property (T@"NSString",&,N,G_rootFolderTitle,S_setRootFolderTitle:,V_rootFolderTitle) rootFolderTitle;
@property (T@"NSString",&,N,G_folderSubitemName,S_setFolderSubitemName:,V_folderSubitemName) folderSubitemName;
@property (TB,N,G_displayedShareIsOwnRoot,S_setDisplayedShareIsOwnRoot:,V_displayedShareIsOwnRoot) displayedShareIsOwnRoot;
@property (T@"UIImage",&,N,G_headerPrimaryImage,S_setHeaderPrimaryImage:,V_headerPrimaryImage) headerPrimaryImage;
@property (T@"UIImage",&,N,G_headerSecondaryImage,S_setHeaderSecondaryImage:,V_headerSecondaryImage) headerSecondaryImage;
@property (T@"CKSystemSharingUIObserver",&,N,G_systemSharingUIObserver,S_setSystemSharingUIObserver:,V_systemSharingUIObserver) systemSharingUIObserver;
@property (T@"<_UICloudSharingControllerDelegate_Internal>",W,N,V_internalDelegate) internalDelegate;
@property (T@"<UICloudSharingControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,N,V_availablePermissions) availablePermissions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIRemoteViewController",R,N) _containedRemoteViewController;
```

## Class methods

```
+[UICloudSharingController allowedSharingOptionsFromPermissions:];
```

## Instance methods

```
-[UICloudSharingController setShare:];
-[UICloudSharingController excludedActivityTypes];
-[UICloudSharingController internalDelegate];
-[UICloudSharingController _containedRemoteViewController];
-[UICloudSharingController dealloc];
-[UICloudSharingController share];
-[UICloudSharingController setContainer:];
-[UICloudSharingController setInternalDelegate:];
-[UICloudSharingController setDelegate:];
-[UICloudSharingController __viewControllerWillBePresented:];
-[UICloudSharingController _didDismiss];
-[UICloudSharingController delegate];
-[UICloudSharingController modalPresentationStyle];
-[UICloudSharingController container];
-[UICloudSharingController addResizingChildViewController:];
-[UICloudSharingController _activityViewController];
-[UICloudSharingController _allowShareUpgrade];
-[UICloudSharingController _callPreparationHandler:];
-[UICloudSharingController _childViewController];
-[UICloudSharingController _cloudSharingControllerDidActivateAddPeopleWithRemoteSourceX:y:width:height:];
-[UICloudSharingController _cloudSharingControllerDidActivateAddPeopleWithRemoteSourceX:y:width:height:allowedSharingOptions:];
-[UICloudSharingController _cloudSharingControllerDidActivateShowActivityController];
-[UICloudSharingController _cloudSharingControllerDidActivateShowSharedFolder];
-[UICloudSharingController _cloudSharingControllerDidChooseTransport:];
-[UICloudSharingController _cloudSharingControllerDidModifyPrimarySwitch:];
-[UICloudSharingController _cloudSharingControllerDidModifySecondarySwitch:];
-[UICloudSharingController _cloudSharingControllerDidUpdateRootFolderURL:];
-[UICloudSharingController _customPresentationControllerForPresentedController:presentingController:sourceController:];
-[UICloudSharingController _deleteShareAfterDismissalWithoutSave:];
-[UICloudSharingController _dismissForActivityRepresentation:];
-[UICloudSharingController _dismissViewControllerWithError:];
-[UICloudSharingController _displayedShareIsOwnRoot];
-[UICloudSharingController _folderSubitemName];
-[UICloudSharingController _headerPrimaryImage];
-[UICloudSharingController _headerSecondaryImage];
-[UICloudSharingController _originalPresentingViewController];
-[UICloudSharingController _participantDetails];
-[UICloudSharingController _performAuxiliaryActionWithCompletion:];
-[UICloudSharingController _performHeaderActionWithCompletion:];
-[UICloudSharingController _primaryAuxiliarySwitchState];
-[UICloudSharingController _primaryAuxiliarySwitchTitle];
-[UICloudSharingController _remoteViewController];
-[UICloudSharingController _representFullscreenAfterActivityDismissal:];
-[UICloudSharingController _requestSavedShareWithCompletion:];
-[UICloudSharingController _requiresCustomPresentationController];
-[UICloudSharingController _rootFolderTitle];
-[UICloudSharingController _secondaryAuxiliarySwitchState];
-[UICloudSharingController _secondaryAuxiliarySwitchTitle];
-[UICloudSharingController _sectionTitleForAuxiliarySwitches];
-[UICloudSharingController _sendDidStopSharingDelegate];
-[UICloudSharingController _setActivityViewController:];
-[UICloudSharingController _setAllowShareUpgrade:];
-[UICloudSharingController _setChildViewController:];
-[UICloudSharingController _setCloudKitShare:container:];
-[UICloudSharingController _setDisplayedShareIsOwnRoot:];
-[UICloudSharingController _setFolderSubitemName:];
-[UICloudSharingController _setHeaderPrimaryImage:];
-[UICloudSharingController _setHeaderSecondaryImage:];
-[UICloudSharingController _setOriginalPresentingViewController:];
-[UICloudSharingController _setParticipantDetails:];
-[UICloudSharingController _setPrimaryAuxiliarySwitchState:];
-[UICloudSharingController _setPrimaryAuxiliarySwitchTitle:];
-[UICloudSharingController _setRootFolderTitle:];
-[UICloudSharingController _setSecondaryAuxiliarySwitchState:];
-[UICloudSharingController _setSecondaryAuxiliarySwitchTitle:];
-[UICloudSharingController _setSectionTitleForAuxiliarySwitches:];
-[UICloudSharingController _setStrongReferenceToOurself:];
-[UICloudSharingController _setSystemSharingUIObserver:];
-[UICloudSharingController _shareDidChange:];
-[UICloudSharingController _shareWasMadePrivate];
-[UICloudSharingController _sharingViewPresentationController];
-[UICloudSharingController _strongReferenceToOurself];
-[UICloudSharingController _systemSharingUIObserver];
-[UICloudSharingController _upgradeShare];
-[UICloudSharingController activityItemSource];
-[UICloudSharingController availablePermissions];
-[UICloudSharingController containerSetupInfo];
-[UICloudSharingController createActivityLinkMetadata];
-[UICloudSharingController initWithAncestorShare:];
-[UICloudSharingController initWithAncestorShare:container:];
-[UICloudSharingController initWithPreparationHandler:];
-[UICloudSharingController initWithShare:container:];
-[UICloudSharingController initWithShare:preparationHandler:];
-[UICloudSharingController preparationHandler];
-[UICloudSharingController setAvailablePermissions:];
-[UICloudSharingController setContainerSetupInfo:];
-[UICloudSharingController setPreparationHandler:];
```
