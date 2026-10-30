# `CFXEffectPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CFXEffectPickerViewDelegate`, `CFXEffectPickerViewDataSource`
- 7 instance variables, 11 properties, 36 instance methods, 1 class methods

## Instance variables

```
B _previewing;
@"UIImage" _previewBackgroundImage;
@"CFXEffectType" _effectType;
@"CFXEffectPickerView" _pickerView;
@"<CFXEffectPickerViewControllerDelegate>" _delegate;
@"NSArray" _effects;
@"NSObject<OS_dispatch_queue>" _effectLoadingQueue;
```

## Properties

```
@property (T@"NSArray",&,N,V_effects) effects;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_effectLoadingQueue) effectLoadingQueue;
@property (T@"CFXEffectPickerView",&,N,V_pickerView) pickerView;
@property (TB,N,GisPreviewing,V_previewing) previewing;
@property (T@"UIImage",&,N,V_previewBackgroundImage) previewBackgroundImage;
@property (T@"CFXEffectType",&,N,V_effectType) effectType;
@property (T@"<CFXEffectPickerViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXEffectPickerViewController effectPickerViewController];
```

## Instance methods

```
-[CFXEffectPickerViewController effects];
-[CFXEffectPickerViewController viewWillDisappear:];
-[CFXEffectPickerViewController willMoveToParentViewController:];
-[CFXEffectPickerViewController viewDidLoad];
-[CFXEffectPickerViewController viewWillAppear:];
-[CFXEffectPickerViewController setEffects:];
-[CFXEffectPickerViewController setDelegate:];
-[CFXEffectPickerViewController setEffectType:];
-[CFXEffectPickerViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[CFXEffectPickerViewController delegate];
-[CFXEffectPickerViewController effectType];
-[CFXEffectPickerViewController isPreviewing];
-[CFXEffectPickerViewController setPreviewing:];
-[CFXEffectPickerViewController pickerView];
-[CFXEffectPickerViewController setPickerView:];
-[CFXEffectPickerViewController startPreviewing];
-[CFXEffectPickerViewController stopPreviewing];
-[CFXEffectPickerViewController CFX_configureEffect:previewSizeInPixels:];
-[CFXEffectPickerViewController CFX_restartPreviewing];
-[CFXEffectPickerViewController CFX_createPickerViewForEffectType:];
-[CFXEffectPickerViewController CFX_indexForEffectIdentifier:];
-[CFXEffectPickerViewController CFX_loadEffectsForType:completion:];
-[CFXEffectPickerViewController CFX_stopPreviewing];
-[CFXEffectPickerViewController effectPickerView:effectAtIndex:];
-[CFXEffectPickerViewController effectLoadingQueue];
-[CFXEffectPickerViewController effectPickerView:didPickEffectAtIndex:];
-[CFXEffectPickerViewController effectPickerView:effectAtIndex:forPreviewingAtSizeInPixels:completionBlock:];
-[CFXEffectPickerViewController effectPickerView:effectIdentifierAtIndex:];
-[CFXEffectPickerViewController effectPickerView:effectTitleAtIndex:];
-[CFXEffectPickerViewController effectPickerView:indexForEffectID:];
-[CFXEffectPickerViewController effectPickerViewDidScroll:];
-[CFXEffectPickerViewController numberOfEffectsInPickerView:];
-[CFXEffectPickerViewController previewBackgroundImage];
-[CFXEffectPickerViewController setEffectLoadingQueue:];
-[CFXEffectPickerViewController setPreviewBackgroundImage:];
-[CFXEffectPickerViewController shouldRotateCellsForDeviceOrientation];
```
