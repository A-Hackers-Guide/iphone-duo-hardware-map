# `SBSystemApertureFakeDisplayOffTestRecipe`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTestRecipe`
- 8 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CAContext" _underInfiniteHighLevelContext;
@"CALayer" _underInfiniteHighLevelRootLayer;
@"CALayer" _blueLayer;
@"CALayer" _redLayer;
@"CAPortalLayer" _recordingIndicatorPortalLayer;
@"CALayer<SBRecordingIndicatorLayering>" _matchMovedRecordingIndicatorLayer;
@"CALayer<SBRecordingIndicatorLayering>" _recordingIndicatorLayer;
B _parentSourceIndicatorOnMainLayer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureFakeDisplayOffTestRecipe title];
-[SBSystemApertureFakeDisplayOffTestRecipe _changeBlueLayerVisibility:];
-[SBSystemApertureFakeDisplayOffTestRecipe _changeMatchMovedIndicatorVisiblity:];
-[SBSystemApertureFakeDisplayOffTestRecipe _changeRecordingIndicatorLayerVisibility:];
-[SBSystemApertureFakeDisplayOffTestRecipe _changeRecordingIndicatorPortalLayerVisibility:];
-[SBSystemApertureFakeDisplayOffTestRecipe _changeRedLayerVisibility:];
-[SBSystemApertureFakeDisplayOffTestRecipe _setupContext];
-[SBSystemApertureFakeDisplayOffTestRecipe domainClass];
-[SBSystemApertureFakeDisplayOffTestRecipe handleVolumeDecrease];
-[SBSystemApertureFakeDisplayOffTestRecipe handleVolumeIncrease];
```
