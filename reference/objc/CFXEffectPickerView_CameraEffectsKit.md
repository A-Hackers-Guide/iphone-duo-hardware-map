# `CFXEffectPickerView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDataSource`, `JFXEffectPreviewManagerDelegate`, `UICollectionViewDelegateFlowLayout`
- 10 instance variables, 14 properties, 52 instance methods, 0 class methods

## Instance variables

```
B _continuousPreviewEnabled;
B _useCameraForContinuousPreview;
B _previewingIsWaitingForConfiguration;
@"UIImage" _previewBackgroundImage;
@"<CFXEffectPickerViewDataSource>" _dataSource;
@"<CFXEffectPickerViewDelegate>" _delegate;
@"JFXEffectStaticPreviewOptions" _staticPreviewOptions;
@"JFXEffectPreviewManager" _previewManager;
{CGSize="width"d"height"d} _cellSize;
{CGSize="width"d"height"d} _thumbnailSize;
```

## Properties

```
@property (T@"JFXEffectStaticPreviewOptions",&,N,V_staticPreviewOptions) staticPreviewOptions;
@property (TB,N,V_previewingIsWaitingForConfiguration) previewingIsWaitingForConfiguration;
@property (T@"JFXEffectPreviewManager",&,N,V_previewManager) previewManager;
@property (T{CGSize=dd},N,V_cellSize) cellSize;
@property (T{CGSize=dd},N,V_thumbnailSize) thumbnailSize;
@property (TB,N,GisContinuousPreviewEnabled,V_continuousPreviewEnabled) continuousPreviewEnabled;
@property (T@"UIImage",&,N,V_previewBackgroundImage) previewBackgroundImage;
@property (TB,N,GisUsingCameraForContinuousPreview,V_useCameraForContinuousPreview) useCameraForContinuousPreview;
@property (T@"<CFXEffectPickerViewDataSource>",W,N,V_dataSource) dataSource;
@property (T@"<CFXEffectPickerViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CFXEffectPickerView setThumbnailSize:];
-[CFXEffectPickerView collectionView:numberOfItemsInSection:];
-[CFXEffectPickerView thumbnailSize];
-[CFXEffectPickerView collectionView:didSelectItemAtIndexPath:];
-[CFXEffectPickerView collectionView:cellForItemAtIndexPath:];
-[CFXEffectPickerView collectionView];
-[CFXEffectPickerView collectionViewLayout];
-[CFXEffectPickerView setDataSource:];
-[CFXEffectPickerView collectionView:layout:sizeForItemAtIndexPath:];
-[CFXEffectPickerView reloadData];
-[CFXEffectPickerView setDelegate:];
-[CFXEffectPickerView dataSource];
-[CFXEffectPickerView contentView];
-[CFXEffectPickerView delegate];
-[CFXEffectPickerView sharedInit];
-[CFXEffectPickerView initWithCoder:];
-[CFXEffectPickerView initWithFrame:];
-[CFXEffectPickerView scrollViewDidScroll:];
-[CFXEffectPickerView cellSize];
-[CFXEffectPickerView configureCell:];
-[CFXEffectPickerView setCellSize:];
-[CFXEffectPickerView startPreviewing];
-[CFXEffectPickerView stopPreviewing];
-[CFXEffectPickerView effectPickerCellReuseIdentifier];
-[CFXEffectPickerView subviewsDidLoad];
-[CFXEffectPickerView applyEffectAtCellIndex:];
-[CFXEffectPickerView collectionView:didResize:];
-[CFXEffectPickerView didResizeCollectionViewToSize:];
-[CFXEffectPickerView didScrollCollectionView];
-[CFXEffectPickerView didSelectItemAtCellIndex:];
-[CFXEffectPickerView effectDidLoadForCell:effect:];
-[CFXEffectPickerView effectIndexForCellIndex:];
-[CFXEffectPickerView effectPickerCellNibName];
-[CFXEffectPickerView effectPickerNibName];
-[CFXEffectPickerView effectPreviewManager:didUpdateContinousPreviewsForEffectIDs:];
-[CFXEffectPickerView isContinuousPreviewEnabled];
-[CFXEffectPickerView isUsingCameraForContinuousPreview];
-[CFXEffectPickerView numberOfCollectionViewItems];
-[CFXEffectPickerView orientationDidChange];
-[CFXEffectPickerView previewBackgroundImage];
-[CFXEffectPickerView previewManager];
-[CFXEffectPickerView previewSizeInPixels];
-[CFXEffectPickerView previewingIsWaitingForConfiguration];
-[CFXEffectPickerView setContinuousPreviewEnabled:];
-[CFXEffectPickerView setPreviewBackgroundImage:];
-[CFXEffectPickerView setPreviewManager:];
-[CFXEffectPickerView setPreviewingIsWaitingForConfiguration:];
-[CFXEffectPickerView setStaticPreviewOptions:];
-[CFXEffectPickerView setUseCameraForContinuousPreview:];
-[CFXEffectPickerView staticPreviewOptions];
-[CFXEffectPickerView updatePreviewEffects];
-[CFXEffectPickerView updatePreviewEffectsWhenReloadComplete];
```
