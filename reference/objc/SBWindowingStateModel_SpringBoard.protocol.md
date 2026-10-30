# `SBWindowingStateModel` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"SBWindowingStrip",C,N) strip;
@property (T@"SBAppsRegionModel",C,N) appsRegionModel;
@property (T@"SBDeckRegionModel",C,N) deckRegionModel;
@property (T@"NSArray",C,N) spacesBeforeAppsRegion;
@property (T@"NSArray",C,N) spacesAfterAppsRegion;
@property (T@"SBAppLayout",&,N) arcSwipeInitialAppLayout;
@property (T@"SBDisplayItem",&,N) arcSwipeNextDisplayItem;
@property (T@"SBDisplayItem",&,N) arcSwipePreviousDisplayItem;
```

## Instance methods

```
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
