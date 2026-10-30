# `_UICollectionViewAnimationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionViewAnimationContext`
- 10 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _appearingAttributesDict;
@"NSMutableDictionary" _disappearingAttributesDict;
@"NSArray" _updates;
@"UICollectionViewLayout" _layout;
@"<_UICollectionViewUpdateTranslating>" _dataSourceTranslator;
@"NSDictionary" _appearingAnimations;
@"NSDictionary" _disappearingAnimations;
@"NSDictionary" _animationsForOnScreenViews;
@"NSArray" _previouslyVisibleItemIndexPaths;
@"NSArray" _currentlyVisibleItemIndexPaths;
```

## Properties

```
@property (T@"UICollectionViewLayout",R,N,V_layout) layout;
@property (T@"NSArray",R,N,V_updates) updates;
@property (T@"NSArray",C,N) appearingAttributes;
@property (T@"NSArray",C,N) disappearingAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewAnimationContext updates];
-[_UICollectionViewAnimationContext initalSectionGlobalItemRangeForSection:];
-[_UICollectionViewAnimationContext finalIndexPathForSupplementaryElementOfKind:forInitialIndexPath:];
-[_UICollectionViewAnimationContext finalSectionIndexForInitialSectionIndex:];
-[_UICollectionViewAnimationContext finalGlobalIndexForInitialGlobalIndex:];
-[_UICollectionViewAnimationContext initialGlobalIndexForFinalGlobalIndex:];
-[_UICollectionViewAnimationContext finalSectionGlobalItemRangeForSection:];
-[_UICollectionViewAnimationContext initialSectionCount];
-[_UICollectionViewAnimationContext initialIndexPathForSupplementaryElementOfKind:forFinalIndexPath:];
-[_UICollectionViewAnimationContext finalIndexPathForInitialIndexPath:];
-[_UICollectionViewAnimationContext finalSectionCount];
-[_UICollectionViewAnimationContext layout];
-[_UICollectionViewAnimationContext initialIndexPathForFinalIndexPath:];
-[_UICollectionViewAnimationContext initialSectionIndexForFinalSectionIndex:];
-[_UICollectionViewAnimationContext appearingAttributes];
-[_UICollectionViewAnimationContext disappearingAttributes];
-[_UICollectionViewAnimationContext setAppearingAttributes:];
-[_UICollectionViewAnimationContext setDisappearingAttributes:];
```
