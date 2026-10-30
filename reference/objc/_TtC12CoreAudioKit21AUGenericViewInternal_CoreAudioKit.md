# `_TtC12CoreAudioKit21AUGenericViewInternal`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDelegate`
- 11 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
_$sSo11AUAudioUnitCSg auAudioUnit;
_$sSo16UIViewControllerCSg owningController;
UIKit.UICollectionViewDiffableDataSource _$sySS CoreAudioKit.AUGenericViewInternal.ParamItem ? dataSource;
_$sSo16UICollectionViewCSg collectionView;
Swift.Bool hasGroups;
_$sSa -> Foundation.IndexPath pathsNeedingPeriodicUpdates;
_$sSo7NSTimerCSg scheduledUpdatesTimer;
_$sSvSg paramObserverToken;
_$sSiSg showSingleClumpIndex;
_$sSD -> Swift.UInt64 _$sSo20UICollectionViewCellC paramDictionary;
_$sSa -> CoreAudioKit.AUGenericViewInternal.labelWidthInfo widthInfo;
```

## Properties

```
@property (T@"AUAudioUnit",N,&,VauAudioUnit) auAudioUnit;
@property (T@"UIViewController",N,&,VowningController) owningController;
@property (T^v,N,VparamObserverToken) paramObserverToken;
```

## Instance methods

```
-[_TtC12CoreAudioKit21AUGenericViewInternal collectionView:willDisplayCell:forItemAtIndexPath:];
-[_TtC12CoreAudioKit21AUGenericViewInternal removeFromSuperview];
-[_TtC12CoreAudioKit21AUGenericViewInternal initWithCoder:];
-[_TtC12CoreAudioKit21AUGenericViewInternal traitCollectionDidChange:];
-[_TtC12CoreAudioKit21AUGenericViewInternal collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:];
-[_TtC12CoreAudioKit21AUGenericViewInternal initWithFrame:];
-[_TtC12CoreAudioKit21AUGenericViewInternal setAuAudioUnit:];
-[_TtC12CoreAudioKit21AUGenericViewInternal auAudioUnit];
-[_TtC12CoreAudioKit21AUGenericViewInternal owningController];
-[_TtC12CoreAudioKit21AUGenericViewInternal paramObserverToken];
-[_TtC12CoreAudioKit21AUGenericViewInternal removeScheduledUpdatesTimer];
-[_TtC12CoreAudioKit21AUGenericViewInternal setOwningController:];
-[_TtC12CoreAudioKit21AUGenericViewInternal setParamObserverToken:];
```
