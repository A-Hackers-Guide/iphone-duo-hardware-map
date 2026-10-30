# `UIDocumentSharingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIActionSheetPresentationControllerDelegate`, `_UIRemoteViewControllerContaining`, `_UISharingPublicController`
- 21 instance variables, 30 properties, 71 instance methods, 0 class methods

## Instance variables

```
B _collaborationUIEnabled;
B _showOnlyAddPeople;
B _showRootFolder;
B _legacyAppearance;
@"_UIResilientRemoteViewContainerViewController" _childViewController;
@"UIViewController" _originalPresentingViewController;
@"UIViewController" _strongReferenceToOurself;
@"UIActivityViewController" _activityViewController;
@"NSURL" _url;
@"NSURL" _rootFolderURL;
@ _delegate;
@"UIImage" _thumbnail;
@"NSString" _auxiliaryActionTitle;
@"NSString" _mailTemplate;
@"NSString" _messageTemplate;
@"NSString" _mailSubject;
@"NSString" _initialHeaderSubtitle;
@"NSString" _headerSubtitle;
@"NSString" _headerActionTitle;
@"NSString" _appName;
@"<_UIDocumentSharingControllerDelegate_Private>" __privateDelegate;
```

## Properties

```
@property (T@"_UIResilientRemoteViewContainerViewController",&,N,G_childViewController,S_setChildViewController:,V_childViewController) childViewController;
@property (T@"_UIShareInvitationRemoteViewController",R,N,G_remoteViewController) remoteViewController;
@property (T@"UIViewController",W,N,G_originalPresentingViewController,S_setOriginalPresentingViewController:,V_originalPresentingViewController) originalPresentingViewController;
@property (T@"UIViewController",&,N,G_strongReferenceToOurself,S_setStrongReferenceToOurself:,V_strongReferenceToOurself) strongReferenceToOurself;
@property (T@"UIActivityViewController",&,N,V_activityViewController) activityViewController;
@property (T@"NSURL",&,N,V_url) url;
@property (T@"NSURL",&,N,V_rootFolderURL) rootFolderURL;
@property (T@,W,N,V_delegate) delegate;
@property (T@"UIImage",C,N,G_thumbnail,S_setThumbnail:,V_thumbnail) thumbnail;
@property (T@"NSString",C,N,G_auxiliaryActionTitle,S_setAuxiliaryActionTitle:,V_auxiliaryActionTitle) auxiliaryActionTitle;
@property (T@"NSString",C,N,G_mailTemplate,S_setMailTemplate:,V_mailTemplate) mailTemplate;
@property (T@"NSString",C,N,G_messageTemplate,S_setMessageTemplate:,V_messageTemplate) messageTemplate;
@property (T@"NSString",C,N,G_mailSubject,S_setMailSubject:,V_mailSubject) mailSubject;
@property (TB,N,G_collaborationUIEnabled,S_setCollaborationUIEnabled:,V_collaborationUIEnabled) collaborationUIEnabled;
@property (TB,N,G_showOnlyAddPeople,S_setShowOnlyAddPeople:,V_showOnlyAddPeople) showOnlyAddPeople;
@property (TB,N,G_showRootFolder,S_setShowRootFolder:,V_showRootFolder) showRootFolder;
@property (T@"NSString",C,N,G_initialHeaderSubtitle,S_setInitialHeaderSubtitle:,V_initialHeaderSubtitle) initialHeaderSubtitle;
@property (T@"NSString",C,N,G_headerSubtitle,S_setHeaderSubtitle:,V_headerSubtitle) headerSubtitle;
@property (T@"NSString",C,N,G_headerActionTitle,S_setHeaderActionTitle:,V_headerActionTitle) headerActionTitle;
@property (T@"NSString",C,N,G_appName,S_setAppName:,V_appName) appName;
@property (T@"<_UIDocumentSharingControllerDelegate_Private>",W,N,G_privateDelegate,S_setPrivateDelegate:,V__privateDelegate) _privateDelegate;
@property (TB,N,G_legacyAppearance,S_setLegacyAppearance:,V_legacyAppearance) legacyAppearance;
@property (T@,W,N) delegate;
@property (T@"<_UIDocumentSharingControllerDelegate_Private>",W,N,G_privateDelegate,S_setPrivateDelegate:) _privateDelegate;
@property (TB,N,G_legacyAppearance,S_setLegacyAppearance:) legacyAppearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIRemoteViewController",R,N) _containedRemoteViewController;
```

## Instance methods

```
-[UIDocumentSharingController _setMailSubject:];
-[UIDocumentSharingController initWithFileURL:error:];
-[UIDocumentSharingController initWithFileURL:];
-[UIDocumentSharingController activityViewController];
-[UIDocumentSharingController _containedRemoteViewController];
-[UIDocumentSharingController dealloc];
-[UIDocumentSharingController setActivityViewController:];
-[UIDocumentSharingController _privateDelegate];
-[UIDocumentSharingController setDelegate:];
-[UIDocumentSharingController _didDismiss];
-[UIDocumentSharingController delegate];
-[UIDocumentSharingController setUrl:];
-[UIDocumentSharingController url];
-[UIDocumentSharingController _headerSubtitle];
-[UIDocumentSharingController _showRootFolder];
-[UIDocumentSharingController _addResizingChildViewController:];
-[UIDocumentSharingController _appName];
-[UIDocumentSharingController _auxiliaryActionTitle];
-[UIDocumentSharingController _childViewController];
-[UIDocumentSharingController _cloudSharingControllerDidActivateAddPeopleWithRemoteSourceX:y:width:height:];
-[UIDocumentSharingController _cloudSharingControllerDidActivateAddPeopleWithRemoteSourceX:y:width:height:allowedSharingOptions:];
-[UIDocumentSharingController _cloudSharingControllerDidActivateShowActivityController];
-[UIDocumentSharingController _cloudSharingControllerDidActivateShowSharedFolder];
-[UIDocumentSharingController _cloudSharingControllerDidChooseTransport:];
-[UIDocumentSharingController _cloudSharingControllerDidModifyPrimarySwitch:];
-[UIDocumentSharingController _cloudSharingControllerDidModifySecondarySwitch:];
-[UIDocumentSharingController _cloudSharingControllerDidUpdateRootFolderURL:];
-[UIDocumentSharingController _collaborationUIEnabled];
-[UIDocumentSharingController _customPresentationControllerForPresentedController:presentingController:sourceController:];
-[UIDocumentSharingController _dismissForActivityRepresentation:];
-[UIDocumentSharingController _dismissViewControllerWithError:];
-[UIDocumentSharingController _headerActionTitle];
-[UIDocumentSharingController _initialHeaderSubtitle];
-[UIDocumentSharingController _legacyAppearance];
-[UIDocumentSharingController _mailSubject];
-[UIDocumentSharingController _mailTemplate];
-[UIDocumentSharingController _messageTemplate];
-[UIDocumentSharingController _originalPresentingViewController];
-[UIDocumentSharingController _performAuxiliaryActionWithCompletion:];
-[UIDocumentSharingController _performHeaderActionWithCompletion:];
-[UIDocumentSharingController _presentationControllerDidDismiss:];
-[UIDocumentSharingController _remoteViewController];
-[UIDocumentSharingController _representFullscreenAfterActivityDismissal:];
-[UIDocumentSharingController _requestSavedShareWithCompletion:];
-[UIDocumentSharingController _requiresCustomPresentationController];
-[UIDocumentSharingController _setAppName:];
-[UIDocumentSharingController _setAuxiliaryActionTitle:];
-[UIDocumentSharingController _setChildViewController:];
-[UIDocumentSharingController _setCollaborationUIEnabled:];
-[UIDocumentSharingController _setHeaderActionTitle:];
-[UIDocumentSharingController _setHeaderSubtitle:];
-[UIDocumentSharingController _setInitialHeaderSubtitle:];
-[UIDocumentSharingController _setLegacyAppearance:];
-[UIDocumentSharingController _setMailSubject:template:];
-[UIDocumentSharingController _setMailTemplate:];
-[UIDocumentSharingController _setMessageTemplate:];
-[UIDocumentSharingController _setOriginalPresentingViewController:];
-[UIDocumentSharingController _setPrivateDelegate:];
-[UIDocumentSharingController _setShowOnlyAddPeople:];
-[UIDocumentSharingController _setShowRootFolder:];
-[UIDocumentSharingController _setStrongReferenceToOurself:];
-[UIDocumentSharingController _setThumbnail:];
-[UIDocumentSharingController _shareDidChange:];
-[UIDocumentSharingController _shareWasMadePrivate];
-[UIDocumentSharingController _sharingViewPresentationController];
-[UIDocumentSharingController _showOnlyAddPeople];
-[UIDocumentSharingController _strongReferenceToOurself];
-[UIDocumentSharingController _thumbnail];
-[UIDocumentSharingController _updatePresentationStyleForLegacyAppearance];
-[UIDocumentSharingController rootFolderURL];
-[UIDocumentSharingController setRootFolderURL:];
```
