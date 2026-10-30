# `SBWindowingStateModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowingStateModel`
- 8 instance variables, 12 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBWindowingStrip" strip;
@"SBAppsRegionModel" appsRegionModel;
@"SBDeckRegionModel" deckRegionModel;
@"NSArray" spacesBeforeAppsRegion;
@"NSArray" spacesAfterAppsRegion;
@"SBAppLayout" arcSwipeInitialAppLayout;
@"SBDisplayItem" arcSwipeNextDisplayItem;
@"SBDisplayItem" arcSwipePreviousDisplayItem;
```

## Properties

```
@property (T@"SBWindowingStrip",C,N,Vstrip) strip;
@property (T@"SBAppsRegionModel",C,N,VappsRegionModel) appsRegionModel;
@property (T@"SBDeckRegionModel",C,N,VdeckRegionModel) deckRegionModel;
@property (T@"NSArray",C,N,VspacesBeforeAppsRegion) spacesBeforeAppsRegion;
@property (T@"NSArray",C,N,VspacesAfterAppsRegion) spacesAfterAppsRegion;
@property (T@"SBAppLayout",&,N,VarcSwipeInitialAppLayout) arcSwipeInitialAppLayout;
@property (T@"SBDisplayItem",&,N,VarcSwipeNextDisplayItem) arcSwipeNextDisplayItem;
@property (T@"SBDisplayItem",&,N,VarcSwipePreviousDisplayItem) arcSwipePreviousDisplayItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowingStateModel init];
-[SBWindowingStateModel strip];
-[SBWindowingStateModel deckRegionModel];
-[SBWindowingStateModel setArcSwipePreviousDisplayItem:];
-[SBWindowingStateModel appsRegionModel];
-[SBWindowingStateModel arcSwipeInitialAppLayout];
-[SBWindowingStateModel arcSwipeNextDisplayItem];
-[SBWindowingStateModel arcSwipePreviousDisplayItem];
-[SBWindowingStateModel setAppsRegionModel:];
-[SBWindowingStateModel setArcSwipeInitialAppLayout:];
-[SBWindowingStateModel setArcSwipeNextDisplayItem:];
-[SBWindowingStateModel setDeckRegionModel:];
-[SBWindowingStateModel setSpacesAfterAppsRegion:];
-[SBWindowingStateModel setSpacesBeforeAppsRegion:];
-[SBWindowingStateModel setStrip:];
-[SBWindowingStateModel spacesAfterAppsRegion];
-[SBWindowingStateModel spacesBeforeAppsRegion];
```
