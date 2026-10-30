# `CFXEffectBrowserViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `AVTAvatarPickerDelegate`, `CFXEffectPickerViewControllerDelegate`, `IMADockViewControllerDelegate`, `CFXMemojiPickerViewControllerDelegate`
- 20 instance variables, 28 properties, 77 instance methods, 2 class methods

## Instance variables

```
@"<CFXEffectBrowserContentPresenterDelegate>" _contentPresenterDelegate;
@"NSString" _selectedAppIdentifier;
@"<CFXEffectBrowserViewControllerDelegate>" _delegate;
@"CFXEffectPickerViewController" _effectPickerViewController;
@"UIView" _messagesAppsDockContainerView;
@"IMADockViewController" _messagesAppsDockViewController;
@"CFXMemojiPickerViewController" _memojiPicker;
@"NSObject<OS_dispatch_semaphore>" _animatedPreviewWritingSemaphore;
@"NSObject<OS_dispatch_queue>" _animatedPreviewWritingQueue;
@"NSObject<OS_dispatch_group>" _animatedPreviewProcessingGroup;
@"UIViewController" _contentPresenter;
@"NSLayoutConstraint" _madWidthConstraint;
@"NSLayoutConstraint" _madHeightConstraint;
@"NSLayoutConstraint" _madLeadingConstraint;
@"NSLayoutConstraint" _madTrailingConstraint;
@"NSLayoutConstraint" _madTopConstraint;
@"NSLayoutConstraint" _madBottomConstraint;
@"NSLayoutConstraint" _madExpandedAppButtonsHeightConstraint;
@"NSObject<OS_dispatch_queue>" _animojiLoadingQueue;
@"NSString" _compactDetentIdentifier;
```

## Properties

```
@property (T@"<CFXEffectBrowserViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"CFXEffectPickerViewController",&,N,V_effectPickerViewController) effectPickerViewController;
@property (T@"UIView",&,N,V_messagesAppsDockContainerView) messagesAppsDockContainerView;
@property (T@"IMADockViewController",&,N,V_messagesAppsDockViewController) messagesAppsDockViewController;
@property (T@"CFXMemojiPickerViewController",&,N,V_memojiPicker) memojiPicker;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_animatedPreviewWritingSemaphore) animatedPreviewWritingSemaphore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_animatedPreviewWritingQueue) animatedPreviewWritingQueue;
@property (T@"NSObject<OS_dispatch_group>",&,N,V_animatedPreviewProcessingGroup) animatedPreviewProcessingGroup;
@property (T@"UIViewController",W,N,V_contentPresenter) contentPresenter;
@property (T@"NSLayoutConstraint",&,N,V_madWidthConstraint) madWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_madHeightConstraint) madHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_madLeadingConstraint) madLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_madTrailingConstraint) madTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_madTopConstraint) madTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_madBottomConstraint) madBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_madExpandedAppButtonsHeightConstraint) madExpandedAppButtonsHeightConstraint;
@property (T@"NSString",&,N,V_selectedAppIdentifier) selectedAppIdentifier;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_animojiLoadingQueue) animojiLoadingQueue;
@property (T@"NSString",&,N,V_compactDetentIdentifier) compactDetentIdentifier;
@property (T@"<CFXEffectBrowserContentPresenterDelegate>",W,N,V_contentPresenterDelegate) contentPresenterDelegate;
@property (TB,N) showAppIconBorders;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIViewController",R,N) dockPresentationViewController;
@property (TB,?,R,N) expandedAppShouldDismissOnDragSuccess;
@property (T{CGSize=dd},?,R,N) expandedAppViewControllerSize;
```

## Class methods

```
+[CFXEffectBrowserViewController CFX_droppedSizeForSticker:dropTarget:];
+[CFXEffectBrowserViewController CFX_sizeOfImageAtURL:];
```

## Instance methods

```
-[CFXEffectBrowserViewController dealloc];
-[CFXEffectBrowserViewController viewDidLoad];
-[CFXEffectBrowserViewController viewDidLayoutSubviews];
-[CFXEffectBrowserViewController setDelegate:];
-[CFXEffectBrowserViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[CFXEffectBrowserViewController loadView];
-[CFXEffectBrowserViewController delegate];
-[CFXEffectBrowserViewController avatarPickerWillStartCameraSession:];
-[CFXEffectBrowserViewController avatarPicker:didSelectAvatarRecord:];
-[CFXEffectBrowserViewController avatarPickerDidEndCameraSession:];
-[CFXEffectBrowserViewController effectPickerViewController];
-[CFXEffectBrowserViewController setEffectPickerViewController:];
-[CFXEffectBrowserViewController addSticker:];
-[CFXEffectBrowserViewController contentPresenter];
-[CFXEffectBrowserViewController setContentPresenter:];
-[CFXEffectBrowserViewController hideBrowserAnimated:completion:];
-[CFXEffectBrowserViewController initWithDelegate:contentPresenter:];
-[CFXEffectBrowserViewController setContentPresenterDelegate:];
-[CFXEffectBrowserViewController showMemojiPicker:];
-[CFXEffectBrowserViewController didSelectAppWithBundleIdentifier:];
-[CFXEffectBrowserViewController CFX_addSticker:atDropTarget:];
-[CFXEffectBrowserViewController dockDidMagnify:];
-[CFXEffectBrowserViewController CFX_updateAVTAvatarPickerforViewController:];
-[CFXEffectBrowserViewController animatedPreviewWritingSemaphore];
-[CFXEffectBrowserViewController setAnimatedPreviewWritingQueue:];
-[CFXEffectBrowserViewController addSticker:atDropTarget:];
-[CFXEffectBrowserViewController animatedPreviewProcessingGroup];
-[CFXEffectBrowserViewController animatedPreviewWritingQueue];
-[CFXEffectBrowserViewController animojiLoadingQueue];
-[CFXEffectBrowserViewController commitAnimatedLayoutChanges];
-[CFXEffectBrowserViewController compactCurrentMessagesApp];
-[CFXEffectBrowserViewController compactDetentIdentifier];
-[CFXEffectBrowserViewController configureUIForOrientation];
-[CFXEffectBrowserViewController contentPresenterDelegate];
-[CFXEffectBrowserViewController didDismissMemojiPicker];
-[CFXEffectBrowserViewController dismissExpandedAppViewController:animated:completion:];
-[CFXEffectBrowserViewController displayPickerForEffectTypeIdentifier:messagesAppViewController:embedInMessageAppViewController:];
-[CFXEffectBrowserViewController dockPresentationViewController];
-[CFXEffectBrowserViewController effectPickerViewController:didPickEffect:];
-[CFXEffectBrowserViewController expandedAppShouldDismissOnDragSuccess];
-[CFXEffectBrowserViewController expandedAppViewControllerSize];
-[CFXEffectBrowserViewController initMessagesAppsDockViewController];
-[CFXEffectBrowserViewController localizedPromptForHidingAnimojiForEffectBrowserViewController:];
-[CFXEffectBrowserViewController madBottomConstraint];
-[CFXEffectBrowserViewController madExpandedAppButtonsHeightConstraint];
-[CFXEffectBrowserViewController madHeightConstraint];
-[CFXEffectBrowserViewController madLeadingConstraint];
-[CFXEffectBrowserViewController madTopConstraint];
-[CFXEffectBrowserViewController madTrailingConstraint];
-[CFXEffectBrowserViewController madWidthConstraint];
-[CFXEffectBrowserViewController memojiPicker];
-[CFXEffectBrowserViewController messagesAppsDockContainerView];
-[CFXEffectBrowserViewController messagesAppsDockViewController];
-[CFXEffectBrowserViewController presentExpandedAppViewController:animated:completion:];
-[CFXEffectBrowserViewController refreshEffectBrowserForCameraFlip];
-[CFXEffectBrowserViewController removeEffectPickerViewController];
-[CFXEffectBrowserViewController selectedAnimojiIdentifierForEffectBrowserViewController:];
-[CFXEffectBrowserViewController selectedAppIdentifier];
-[CFXEffectBrowserViewController selectedFilterIdentifierForEffectPickerViewController:];
-[CFXEffectBrowserViewController setAnimatedPreviewProcessingGroup:];
-[CFXEffectBrowserViewController setAnimatedPreviewWritingSemaphore:];
-[CFXEffectBrowserViewController setAnimojiLoadingQueue:];
-[CFXEffectBrowserViewController setCompactDetentIdentifier:];
-[CFXEffectBrowserViewController setMadBottomConstraint:];
-[CFXEffectBrowserViewController setMadExpandedAppButtonsHeightConstraint:];
-[CFXEffectBrowserViewController setMadHeightConstraint:];
-[CFXEffectBrowserViewController setMadLeadingConstraint:];
-[CFXEffectBrowserViewController setMadTopConstraint:];
-[CFXEffectBrowserViewController setMadTrailingConstraint:];
-[CFXEffectBrowserViewController setMadWidthConstraint:];
-[CFXEffectBrowserViewController setMemojiPicker:];
-[CFXEffectBrowserViewController setMessagesAppsDockContainerView:];
-[CFXEffectBrowserViewController setMessagesAppsDockViewController:];
-[CFXEffectBrowserViewController setSelectedAppIdentifier:];
-[CFXEffectBrowserViewController setShowAppIconBorders:];
-[CFXEffectBrowserViewController shouldRotateCellsForDeviceOrientation];
-[CFXEffectBrowserViewController showAppIconBorders];
```
