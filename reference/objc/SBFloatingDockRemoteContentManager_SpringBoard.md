# `SBFloatingDockRemoteContentManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneHostingControllerDelegate`, `_UISceneHostingReconnectingActivationControllerDelegate`, `SBUISFloatingDockRemoteContentHostComponentDelegate`, `SBIconListModelObserver`, `SBLeafIconObserver`, `SBIconViewDropDelegate`, `SBHFileStackIconImageProviderOverrideDataSourceDelegate`, `SBApplicationRestrictionObserver`
- 15 instance variables, 20 properties, 108 instance methods, 0 class methods

## Instance variables

```
@"<SBFloatingDockRemoteContentManagerDelegate>" _delegate;
@"_UISceneHostingController" _sceneHostingController;
@"UIView" _sceneView;
@"UIView" _parentOfSceneView;
@"_UISceneHostingReconnectingActivationController" _reconnectingController;
@"SBFloatingDockRootViewController" _floatingDockRootViewController;
@"SBWindowScene" _windowScene;
@"NSMutableDictionary" _fileStackIconThumbnails;
@"NSMutableDictionary" _fileStackIconOpenIndicators;
@"SBHFileStackIcon" _openedFileStackIcon;
@"SBHFileStackIcon" _closingFileStackIcon;
@"SBUniqueDefaultIconModelStore" _fileStackURLSourceDataStore;
@"NSMutableDictionary" _dragAndDropTempDirsToDelete;
@"NSMutableArray" _hiddenRestorableFileStackIcons;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _remoteContentOverlayFrame;
```

## Properties

```
@property (T@"_UISceneHostingController",R,N,V_sceneHostingController) sceneHostingController;
@property (T@"UIView",R,N,V_sceneView) sceneView;
@property (T@"UIView",R,N,V_parentOfSceneView) parentOfSceneView;
@property (T@"_UISceneHostingReconnectingActivationController",R,N,V_reconnectingController) reconnectingController;
@property (T@"SBFloatingDockRootViewController",R,N,V_floatingDockRootViewController) floatingDockRootViewController;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"NSArray",R,N) fileStackIconsInDock;
@property (T@"NSMutableDictionary",&,N,V_fileStackIconThumbnails) fileStackIconThumbnails;
@property (T@"NSMutableDictionary",&,N,V_fileStackIconOpenIndicators) fileStackIconOpenIndicators;
@property (T@"SBHFileStackIcon",&,N,V_openedFileStackIcon) openedFileStackIcon;
@property (T@"SBHFileStackIcon",&,N,V_closingFileStackIcon) closingFileStackIcon;
@property (T@"SBUniqueDefaultIconModelStore",&,N,V_fileStackURLSourceDataStore) fileStackURLSourceDataStore;
@property (T@"NSMutableDictionary",&,N,V_dragAndDropTempDirsToDelete) dragAndDropTempDirsToDelete;
@property (T@"NSMutableArray",&,N,V_hiddenRestorableFileStackIcons) hiddenRestorableFileStackIcons;
@property (T@"<SBFloatingDockRemoteContentManagerDelegate>",W,N,V_delegate) delegate;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_remoteContentOverlayFrame) remoteContentOverlayFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFloatingDockRemoteContentManager applicationRestrictionController:didUpdateVisibleTags:hiddenTags:];
-[SBFloatingDockRemoteContentManager clientIsReady];
-[SBFloatingDockRemoteContentManager dealloc];
-[SBFloatingDockRemoteContentManager sceneView];
-[SBFloatingDockRemoteContentManager _cleanUpConnectionIfNeeded];
-[SBFloatingDockRemoteContentManager iconArchivableStateDidChange:];
-[SBFloatingDockRemoteContentManager _iconViewForIcon:];
-[SBFloatingDockRemoteContentManager setDelegate:];
-[SBFloatingDockRemoteContentManager delegate];
-[SBFloatingDockRemoteContentManager iconList:didAddIcon:];
-[SBFloatingDockRemoteContentManager windowScene];
-[SBFloatingDockRemoteContentManager iconList:didRemoveIcon:];
-[SBFloatingDockRemoteContentManager clientDidConnect:];
-[SBFloatingDockRemoteContentManager clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:];
-[SBFloatingDockRemoteContentManager clientRequestToAcknowledgeDidFinishAnimatingFor:withFileStackIcon:];
-[SBFloatingDockRemoteContentManager clientRequestToCloseFileStackIcon:];
-[SBFloatingDockRemoteContentManager clientRequestToDeleteDragAndDropTempDirsWithSessionID:];
-[SBFloatingDockRemoteContentManager clientRequestToInsertFileStackIcon:];
-[SBFloatingDockRemoteContentManager clientRequestToRemoveFileStackIcon:];
-[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:contentOverlayFrame:];
-[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:preferredDisplayName:];
-[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:toUrl:];
-[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:withThumbnail:];
-[SBFloatingDockRemoteContentManager clientWillDeactivateWithContext:];
-[SBFloatingDockRemoteContentManager completeContextRequestUpdateFromHost:withError:];
-[SBFloatingDockRemoteContentManager iconView:performDrop:];
-[SBFloatingDockRemoteContentManager iconImageWithInfo:traitCollection:options:forFileStackIcon:];
-[SBFloatingDockRemoteContentManager _floatingDockUtilitiesListModel];
-[SBFloatingDockRemoteContentManager _validateFloatingDockListModel:];
-[SBFloatingDockRemoteContentManager setDragAndDropTempDirsToDelete:];
-[SBFloatingDockRemoteContentManager setFileStackIconOpenIndicators:];
-[SBFloatingDockRemoteContentManager _openedIconView];
-[SBFloatingDockRemoteContentManager setFileStackURLSourceDataStore:];
-[SBFloatingDockRemoteContentManager _anchorFrameForfileStackIconView:];
-[SBFloatingDockRemoteContentManager _cleanUpOpenIndicatorView];
-[SBFloatingDockRemoteContentManager _cleanUpURLSourceDataStore];
-[SBFloatingDockRemoteContentManager _clientBundleIdentifier];
-[SBFloatingDockRemoteContentManager _closeFileStackForIconView:];
-[SBFloatingDockRemoteContentManager _closeFileStackForIconView:animated:];
-[SBFloatingDockRemoteContentManager _createFileStackIconURLSourceDataStore];
-[SBFloatingDockRemoteContentManager _defaultProcessIdentity];
-[SBFloatingDockRemoteContentManager _deleteFileStackIcon:];
-[SBFloatingDockRemoteContentManager _deleteFileStackIconURLSourceFromDisk:];
-[SBFloatingDockRemoteContentManager _deleteFileStackIconURLSourceFromDisk:withError:];
-[SBFloatingDockRemoteContentManager _fileStackIconsFromFloatingDock:];
-[SBFloatingDockRemoteContentManager _floatingDockUserListFolder];
-[SBFloatingDockRemoteContentManager _floatingDockUserListModel];
-[SBFloatingDockRemoteContentManager _floatingDockUserListView];
-[SBFloatingDockRemoteContentManager _floatingDockUtilitiesListFolder];
-[SBFloatingDockRemoteContentManager _floatingDockUtilitiesListView];
-[SBFloatingDockRemoteContentManager _hostComponent];
-[SBFloatingDockRemoteContentManager _iconImageFrameForIconView:];
-[SBFloatingDockRemoteContentManager _isAllowedClientBundleIdentifier:];
-[SBFloatingDockRemoteContentManager _notifyClientConfigurationDidChangeOnFileStackIcon:];
-[SBFloatingDockRemoteContentManager _notifyClientToPrewarmFileStackIconAssociatedFoldersAndOpenIndicators];
-[SBFloatingDockRemoteContentManager _openFileStackForIconView:];
-[SBFloatingDockRemoteContentManager _persistFileStackIconURLSourceToDisk:];
-[SBFloatingDockRemoteContentManager _persistFileStackIconURLSourceToDisk:withError:];
-[SBFloatingDockRemoteContentManager _saveCurrentFileStackURLSourceState:];
-[SBFloatingDockRemoteContentManager _setSecurityScopedURLReadFromBookmarkDataOnFileStackIcon:];
-[SBFloatingDockRemoteContentManager _setupRemoteContentScene];
-[SBFloatingDockRemoteContentManager _setupRemoteContentSceneView];
-[SBFloatingDockRemoteContentManager _shouldInsertDownloadsFolderAfterFirstDownload];
-[SBFloatingDockRemoteContentManager _updateRemoteContentOverlayFrame:];
-[SBFloatingDockRemoteContentManager _urlForFileStackIconDataSourceUniqueIdentifierFromURLSourceDataStore:];
-[SBFloatingDockRemoteContentManager _urlForFileStackIconFromURLSourceDataStore:];
-[SBFloatingDockRemoteContentManager addSceneHostingViewMatchMoveAnimationWithIcon:];
-[SBFloatingDockRemoteContentManager closeFileStackIconIfNeeded];
-[SBFloatingDockRemoteContentManager closingFileStackIcon];
-[SBFloatingDockRemoteContentManager configureIconViewForFinishDownloadAnimationDidFinish:];
-[SBFloatingDockRemoteContentManager configureIconViewForFinishDownloadAnimationWillBegin:];
-[SBFloatingDockRemoteContentManager createOpenIndicatorViewForFileStackIcon:];
-[SBFloatingDockRemoteContentManager deactivateSceneView];
-[SBFloatingDockRemoteContentManager deleteFileStackIcon:];
-[SBFloatingDockRemoteContentManager dragAndDropTempDirsToDelete];
-[SBFloatingDockRemoteContentManager fileStackIconOpenIndicators];
-[SBFloatingDockRemoteContentManager fileStackIconThumbnails];
-[SBFloatingDockRemoteContentManager fileStackIconsInDock];
-[SBFloatingDockRemoteContentManager fileStackURLSourceDataStore];
-[SBFloatingDockRemoteContentManager floatingDockRootViewController];
-[SBFloatingDockRemoteContentManager handleDownloadCompleted:];
-[SBFloatingDockRemoteContentManager handleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:];
-[SBFloatingDockRemoteContentManager handleFloatingDockFrameDidChange:];
-[SBFloatingDockRemoteContentManager handleIconModelDidLayout:];
-[SBFloatingDockRemoteContentManager handleIconModelWillLayout:];
-[SBFloatingDockRemoteContentManager handleInstalledAppsDidChange:];
-[SBFloatingDockRemoteContentManager hiddenRestorableFileStackIcons];
-[SBFloatingDockRemoteContentManager hideAllOpenIndicatorViews];
-[SBFloatingDockRemoteContentManager hideRemoteContent:];
-[SBFloatingDockRemoteContentManager initWithFloatingDockRootViewController:windowScene:];
-[SBFloatingDockRemoteContentManager isRemoteContentPresenting];
-[SBFloatingDockRemoteContentManager openedFileStackIcon];
-[SBFloatingDockRemoteContentManager parentOfSceneView];
-[SBFloatingDockRemoteContentManager reactivateSceneView];
-[SBFloatingDockRemoteContentManager reconnectHostingClient];
-[SBFloatingDockRemoteContentManager reconnectingController];
-[SBFloatingDockRemoteContentManager remoteContentOverlayFrame];
-[SBFloatingDockRemoteContentManager removeOpenIndicatorViewForFileStackIcon:];
-[SBFloatingDockRemoteContentManager removeOpenIndicatorViewForIconUniqueIdentifier:];
-[SBFloatingDockRemoteContentManager removeSceneHostingViewMatchMoveAnimation];
-[SBFloatingDockRemoteContentManager repositionRemoteContent];
-[SBFloatingDockRemoteContentManager sceneHostingController];
-[SBFloatingDockRemoteContentManager setClosingFileStackIcon:];
-[SBFloatingDockRemoteContentManager setFileStackIconThumbnails:];
-[SBFloatingDockRemoteContentManager setHiddenRestorableFileStackIcons:];
-[SBFloatingDockRemoteContentManager setOpenedFileStackIcon:];
-[SBFloatingDockRemoteContentManager showAllOpenIndicatorViews];
-[SBFloatingDockRemoteContentManager tapFileStackIconView:];
```
