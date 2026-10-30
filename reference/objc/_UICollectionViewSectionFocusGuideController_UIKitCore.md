# `_UICollectionViewSectionFocusGuideController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"UICollectionView" _collectionView;
@"NSMapTable" _focusGuideFromSectionMap;
@"NSMapTable" _focusGuideToSectionMap;
@"NSUUID" _lastUpdateIdentifier;
@"NSIndexPath" _focusedIndexPath;
q _pivotSection;
```

## Properties

```
@property (T@"UICollectionView",W,N,V_collectionView) collectionView;
@property (T@"NSMapTable",&,N,V_focusGuideFromSectionMap) focusGuideFromSectionMap;
@property (T@"NSMapTable",&,N,V_focusGuideToSectionMap) focusGuideToSectionMap;
@property (T@"NSUUID",&,N,V_lastUpdateIdentifier) lastUpdateIdentifier;
@property (T@"NSIndexPath",&,N,V_focusedIndexPath) focusedIndexPath;
@property (Tq,N,V_pivotSection) pivotSection;
```

## Instance methods

```
-[_UICollectionViewSectionFocusGuideController initWithCollectionView:];
-[_UICollectionViewSectionFocusGuideController _createOrUpdateSectionFocusGuidePackageForSection:];
-[_UICollectionViewSectionFocusGuideController _updatePivotSection];
-[_UICollectionViewSectionFocusGuideController setPivotSection:];
-[_UICollectionViewSectionFocusGuideController collectionView];
-[_UICollectionViewSectionFocusGuideController _focusGuides];
-[_UICollectionViewSectionFocusGuideController updateFocusedIndexPath:];
-[_UICollectionViewSectionFocusGuideController focusGuideFromSectionMap];
-[_UICollectionViewSectionFocusGuideController setCollectionView:];
-[_UICollectionViewSectionFocusGuideController setFocusGuideToSectionMap:];
-[_UICollectionViewSectionFocusGuideController focusGuideToSectionMap];
-[_UICollectionViewSectionFocusGuideController performLayout];
-[_UICollectionViewSectionFocusGuideController pivotSection];
-[_UICollectionViewSectionFocusGuideController focusedIndexPath];
-[_UICollectionViewSectionFocusGuideController lastUpdateIdentifier];
-[_UICollectionViewSectionFocusGuideController _sectionEndFrameForSection:layout:];
-[_UICollectionViewSectionFocusGuideController _sectionFocusGuidePackageForSection:];
-[_UICollectionViewSectionFocusGuideController setFocusGuideFromSectionMap:];
-[_UICollectionViewSectionFocusGuideController _sectionsToLoad];
-[_UICollectionViewSectionFocusGuideController setFocusedIndexPath:];
-[_UICollectionViewSectionFocusGuideController _sectionFrameForSection:layout:];
-[_UICollectionViewSectionFocusGuideController reloadSectionFocusGuides];
-[_UICollectionViewSectionFocusGuideController cleanupSectionFocusGuides];
-[_UICollectionViewSectionFocusGuideController _layoutSectionFocusGuide:forSection:withFrame:];
-[_UICollectionViewSectionFocusGuideController setLastUpdateIdentifier:];
-[_UICollectionViewSectionFocusGuideController _layoutSectionFocusGuide:forSection:inLayout:];
-[_UICollectionViewSectionFocusGuideController updateFocusedIndexPath:immediatelyReevaluatePivotIndex:];
-[_UICollectionViewSectionFocusGuideController _removeSectionFocusGuidesForSection:];
-[_UICollectionViewSectionFocusGuideController _updateSectionEndFocusGuideForSection:inPackage:layout:];
```
