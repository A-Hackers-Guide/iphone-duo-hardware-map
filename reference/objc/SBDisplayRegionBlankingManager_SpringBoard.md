# `SBDisplayRegionBlankingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayBlankingRegionElementDelegate`, `SDUDisplayRegionBlankingCoordinatorDelegate`, `SDUDisplayRegionBlankingObserver`, `SDUDisplayRegionBlankingRenderer`
- 6 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _elementByRegionIdentifier;
@"NSMutableDictionary" _elementAssertionByRegionIdentifier;
@"NSMutableDictionary" _showHandlersByRegionIdentifier;
@"NSMutableDictionary" _hideHandlersByRegionIdentifier;
@"NSMutableDictionary" _pendingShowHandlersByRegionIdentifier;
@"NSMutableDictionary" _pendingUpdateHandlersByRegionIdentifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDisplayRegionBlankingManager supportsDisplayRegionBlanking];
```

## Instance methods

```
-[SBDisplayRegionBlankingManager init];
-[SBDisplayRegionBlankingManager blankingStateDidChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SBDisplayRegionBlankingManager blankingStateWillChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SBDisplayRegionBlankingManager canBlankDisplayRegion:onWindowScene:forBundleIDs:];
-[SBDisplayRegionBlankingManager hideBlankingViewForRegion:onWindowScene:forBundleIDs:withWillBeginHandler:completionHandler:];
-[SBDisplayRegionBlankingManager showBlankingViewForRegion:onWindowScene:forBundleIDs:withWillBeginHandler:completionHandler:];
-[SBDisplayRegionBlankingManager updateBundleIDsOfBlankingViewForRegion:onWindowScene:forBundleIDs:withHandler:];
-[SBDisplayRegionBlankingManager _createElementForRegion:windowScene:];
-[SBDisplayRegionBlankingManager _showRegion:withHandlers:];
-[SBDisplayRegionBlankingManager _tearDownElementForRegion:];
-[SBDisplayRegionBlankingManager blankingRegionElement:visibilityDidChange:canceled:];
-[SBDisplayRegionBlankingManager blankingRegionElement:visibilityWillChange:];
```
