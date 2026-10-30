# `CAMSmartStyleSettingsRootController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CAMSmartStyleSettingsViewDelegate`, `CAMSmartStylePreviewViewControllerDelegate`, `CAMSmartStyleSettingsPickerViewControllerDelegate`, `CAMSmartStyleSettingsResourceLoadingManagerDelegate`
- 7 instance variables, 12 properties, 47 instance methods, 0 class methods

## Instance variables

```
@"CAMSmartStyleSettingsView" __settingsView;
@? _completionBlock;
@"NSArray" __selectedAssetIdentifiers;
@"CAMSmartStyleSettingsResourceLoadingManager" __resourceLoadingManager;
q __currentStylePreset;
@"NSMutableDictionary" __cachedStyles;
@"CAMSmartStyleSettingsPickerViewController" __pickerViewController;
```

## Properties

```
@property (T@"CAMSmartStyleSettingsView",R,N,V__settingsView) _settingsView;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"NSArray",R,N,V__selectedAssetIdentifiers) _selectedAssetIdentifiers;
@property (T@"NSArray",R,N) _assetIdentifiersToDisplay;
@property (T@"CAMSmartStyleSettingsResourceLoadingManager",R,N,V__resourceLoadingManager) _resourceLoadingManager;
@property (Tq,N,V__currentStylePreset) _currentStylePreset;
@property (T@"NSMutableDictionary",R,N,V__cachedStyles) _cachedStyles;
@property (T@"CAMSmartStyleSettingsPickerViewController",R,N,V__pickerViewController) _pickerViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSmartStyleSettingsRootController _applicationDidEnterBackground];
-[CAMSmartStyleSettingsRootController speedUpFadeInAnimations];
-[CAMSmartStyleSettingsRootController addChildViewController:toView:];
-[CAMSmartStyleSettingsRootController _dismissFromCancelAction:];
-[CAMSmartStyleSettingsRootController _didFinishPickingFromPicker:];
-[CAMSmartStyleSettingsRootController smartStyleSettingsPickerDidUpdateSelectedAssetIdentifiers:];
-[CAMSmartStyleSettingsRootController _cachedStyles];
-[CAMSmartStyleSettingsRootController _validateIsCurrentPicker:];
-[CAMSmartStyleSettingsRootController setCompletionBlock:];
-[CAMSmartStyleSettingsRootController completionBlock];
-[CAMSmartStyleSettingsRootController _styleForPresetType:];
-[CAMSmartStyleSettingsRootController settingsViewRequestsUserAssetSelection:];
-[CAMSmartStyleSettingsRootController _settingsView];
-[CAMSmartStyleSettingsRootController _pickerDidCancel];
-[CAMSmartStyleSettingsRootController settingsViewDidConfirmStyle:];
-[CAMSmartStyleSettingsRootController settingsView:requestsViewControllerForPresetType:pageIndex:parentViewController:];
-[CAMSmartStyleSettingsRootController previewViewController:didChangeAnimatingGrid:];
-[CAMSmartStyleSettingsRootController _presentPicker];
-[CAMSmartStyleSettingsRootController previewViewController:requestsLoadResultForGridIndex:];
-[CAMSmartStyleSettingsRootController settingsView:didUpdateStyle:forPresetType:];
-[CAMSmartStyleSettingsRootController settingsView:requestsTitle:showDoneButton:];
-[CAMSmartStyleSettingsRootController _assetIdentifiersToDisplay];
-[CAMSmartStyleSettingsRootController _readSelectedAssetIdentifiers];
-[CAMSmartStyleSettingsRootController _readSystemStyleFromDefaultsWritesDefaultStyle:];
-[CAMSmartStyleSettingsRootController _currentStylePreset];
-[CAMSmartStyleSettingsRootController _doneButtonItem];
-[CAMSmartStyleSettingsRootController _pickerViewController];
-[CAMSmartStyleSettingsRootController _confirmCurrentStyle];
-[CAMSmartStyleSettingsRootController _canShowWhileLocked];
-[CAMSmartStyleSettingsRootController _persistSystemStyle:];
-[CAMSmartStyleSettingsRootController viewDidAppear:];
-[CAMSmartStyleSettingsRootController set_currentStylePreset:];
-[CAMSmartStyleSettingsRootController loadView];
-[CAMSmartStyleSettingsRootController settingsViewRequestsDismiss:completion:];
-[CAMSmartStyleSettingsRootController _writeSelectedAssetIdentifiers:];
-[CAMSmartStyleSettingsRootController settingsView:requestsStyleForPresetType:];
-[CAMSmartStyleSettingsRootController previewViewControllerDidFinishRendering:];
-[CAMSmartStyleSettingsRootController _stockAssetIdentifiers];
-[CAMSmartStyleSettingsRootController _dismissFromCancelAction:withCompletion:];
-[CAMSmartStyleSettingsRootController smartStyleSettingsPickerDidConfirmSelection:];
-[CAMSmartStyleSettingsRootController smartStyleSettingsResourceLoadingManager:didFinishLoadingForAssetIdentifier:];
-[CAMSmartStyleSettingsRootController settingsView:didChangeToStylePreset:];
-[CAMSmartStyleSettingsRootController _cancelButtonItem];
-[CAMSmartStyleSettingsRootController _dismissPicker];
-[CAMSmartStyleSettingsRootController _resourceLoadingManager];
-[CAMSmartStyleSettingsRootController _selectedAssetIdentifiers];
-[CAMSmartStyleSettingsRootController smartStyleSettingsPickerDidCancelSelection:];
```
