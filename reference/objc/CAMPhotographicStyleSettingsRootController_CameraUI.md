# `CAMPhotographicStyleSettingsRootController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_TtP8CameraUI48CAMPhotographicStylesSetupViewControllerDelegate_`, `CAMSmartStyleSettingsPickerViewControllerDelegate`, `CAMSmartStyleSettingsResourceLoadingManagerDelegate`
- 7 instance variables, 13 properties, 36 instance methods, 1 class methods

## Instance variables

```
B __isOnboarding;
@? _completionBlock;
@"NSArray" __selectedAssetIdentifiers;
@"CAMSmartStyleSettingsResourceLoadingManager" __resourceLoadingManager;
@"CAMSmartStyleSettingsPickerViewController" __pickerViewController;
@"CAMSmartStylePreviewGridView" __previewGridView;
@"_TtC8CameraUI40CAMPhotographicStylesSetupViewController" __setupViewController;
```

## Properties

```
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (TB,R,N,V__isOnboarding) _isOnboarding;
@property (TB,R,N) _allowPhotoPicker;
@property (T@"NSArray",R,N,V__selectedAssetIdentifiers) _selectedAssetIdentifiers;
@property (T@"NSArray",R,N) _assetIdentifiersToDisplay;
@property (T@"CAMSmartStyleSettingsResourceLoadingManager",R,N,V__resourceLoadingManager) _resourceLoadingManager;
@property (T@"CAMSmartStyleSettingsPickerViewController",R,N,V__pickerViewController) _pickerViewController;
@property (T@"CAMSmartStylePreviewGridView",R,N,V__previewGridView) _previewGridView;
@property (T@"_TtC8CameraUI40CAMPhotographicStylesSetupViewController",R,N,V__setupViewController) _setupViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMPhotographicStyleSettingsRootController _stockAssetIdentifiers];
```

## Instance methods

```
-[CAMPhotographicStyleSettingsRootController speedUpFadeInAnimations];
-[CAMPhotographicStyleSettingsRootController _dismissFromCancelAction:];
-[CAMPhotographicStyleSettingsRootController _didFinishPickingFromPicker:];
-[CAMPhotographicStyleSettingsRootController smartStyleSettingsPickerDidUpdateSelectedAssetIdentifiers:];
-[CAMPhotographicStyleSettingsRootController _validateIsCurrentPicker:];
-[CAMPhotographicStyleSettingsRootController setCompletionBlock:];
-[CAMPhotographicStyleSettingsRootController completionBlock];
-[CAMPhotographicStyleSettingsRootController _pickerDidCancel];
-[CAMPhotographicStyleSettingsRootController _presentPicker];
-[CAMPhotographicStyleSettingsRootController _assetIdentifiersToDisplay];
-[CAMPhotographicStyleSettingsRootController viewDidLoad];
-[CAMPhotographicStyleSettingsRootController _readSelectedAssetIdentifiers];
-[CAMPhotographicStyleSettingsRootController _readSystemStyleFromDefaultsWritesDefaultStyle:];
-[CAMPhotographicStyleSettingsRootController _pickerViewController];
-[CAMPhotographicStyleSettingsRootController _canShowWhileLocked];
-[CAMPhotographicStyleSettingsRootController _persistSystemStyle:];
-[CAMPhotographicStyleSettingsRootController viewDidAppear:];
-[CAMPhotographicStyleSettingsRootController _setupViewController];
-[CAMPhotographicStyleSettingsRootController _writeSelectedAssetIdentifiers:];
-[CAMPhotographicStyleSettingsRootController smartStyleSettingsPickerDidConfirmSelection:];
-[CAMPhotographicStyleSettingsRootController smartStyleSettingsResourceLoadingManager:didFinishLoadingForAssetIdentifier:];
-[CAMPhotographicStyleSettingsRootController _cancelButtonItem];
-[CAMPhotographicStyleSettingsRootController _dismissPicker];
-[CAMPhotographicStyleSettingsRootController _resourceLoadingManager];
-[CAMPhotographicStyleSettingsRootController _selectedAssetIdentifiers];
-[CAMPhotographicStyleSettingsRootController smartStyleSettingsPickerDidCancelSelection:];
-[CAMPhotographicStyleSettingsRootController _allowPhotoPicker];
-[CAMPhotographicStyleSettingsRootController _isOnboarding];
-[CAMPhotographicStyleSettingsRootController _persistSystemTextureStyle:];
-[CAMPhotographicStyleSettingsRootController _photoPickerButtonItem];
-[CAMPhotographicStyleSettingsRootController _previewGridView];
-[CAMPhotographicStyleSettingsRootController _readSystemTextureStyleFromDefaultsWrites];
-[CAMPhotographicStyleSettingsRootController _updatePreviewViewsWithLoadResults];
-[CAMPhotographicStyleSettingsRootController initForOnboarding:];
-[CAMPhotographicStyleSettingsRootController photographicStylesSetupViewController:didConfirmPhotographicStyle:];
-[CAMPhotographicStyleSettingsRootController photographicStylesSetupViewControllerDidLeaveIntroMode:];
```
