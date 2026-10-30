# `SDUDisplayRegionBlankingCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`](../userland/System__Library__PrivateFrameworks__SystemUIDisplayUtilities.framework__SystemUIDisplayUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SDUDisplayRegionBlankingControllerDelegate`, `PTSettingsKeyPathObserver`
- 9 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SDUDisplayRegionBlankingServiceServer" _server;
@"SDUDisplayRegionBlankingPrototypeSettings" _prototypeSettings;
@"NSHashTable" _observers;
@"NSMutableDictionary" _regionIdentifierToWindowScene;
@"NSMutableDictionary" _regionIdentifierToBlankingCoordinatorWindow;
@"NSMutableDictionary" _regionIdentifierToBlankingController;
@"NSMutableDictionary" _regionIdentifierToBlankingRenderer;
@"<SDUDisplayRegionBlankingCoordinatorDelegate>" _delegate;
@"<SDUDisplayRegionBlankingRenderer>" _blankingRenderer;
```

## Properties

```
@property (T@"<SDUDisplayRegionBlankingCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (T@"<SDUDisplayRegionBlankingRenderer>",W,N,V_blankingRenderer) blankingRenderer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SDUDisplayRegionBlankingCoordinator removeObserver:];
-[SDUDisplayRegionBlankingCoordinator init];
-[SDUDisplayRegionBlankingCoordinator windowSceneDidDisconnect:];
-[SDUDisplayRegionBlankingCoordinator dealloc];
-[SDUDisplayRegionBlankingCoordinator addObserver:];
-[SDUDisplayRegionBlankingCoordinator setDelegate:];
-[SDUDisplayRegionBlankingCoordinator delegate];
-[SDUDisplayRegionBlankingCoordinator windowSceneDidConnect:];
-[SDUDisplayRegionBlankingCoordinator settings:changedValueForKeyPath:];
-[SDUDisplayRegionBlankingCoordinator blankingControllerForDisplayRegion:];
-[SDUDisplayRegionBlankingCoordinator blankingRenderer];
-[SDUDisplayRegionBlankingCoordinator blankingStateUpdated:];
-[SDUDisplayRegionBlankingCoordinator canBlankDisplayRegion:forBundleIDs:];
-[SDUDisplayRegionBlankingCoordinator setBlankingRenderer:];
```
