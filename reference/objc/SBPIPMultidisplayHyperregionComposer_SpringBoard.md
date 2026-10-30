# `SBPIPMultidisplayHyperregionComposer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBPIPPositionHyperregionComposing`
- 3 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _connectedWindowScenes;
@"<SBPIPPositionHyperregionComposerDelegate>" _delegate;
@"NSMutableDictionary" _sceneIdentifiersToComposers;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_sceneIdentifiersToComposers) sceneIdentifiersToComposers;
@property (T@"<SBPIPPositionHyperregionComposerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",?,C,N,V_connectedWindowScenes) connectedWindowScenes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPMultidisplayHyperregionComposer init];
-[SBPIPMultidisplayHyperregionComposer connectedWindowScenes];
-[SBPIPMultidisplayHyperregionComposer invalidate];
-[SBPIPMultidisplayHyperregionComposer setDelegate:];
-[SBPIPMultidisplayHyperregionComposer delegate];
-[SBPIPMultidisplayHyperregionComposer mergeMutableRegionsMap:withMap:];
-[SBPIPMultidisplayHyperregionComposer _adjustGeometryContextIfNeeded:forComposer:];
-[SBPIPMultidisplayHyperregionComposer _composerForWindowScene:];
-[SBPIPMultidisplayHyperregionComposer _identifierForScene:];
-[SBPIPMultidisplayHyperregionComposer canonicalPositionForPoint:proposedPosition:geometry:interaction:];
-[SBPIPMultidisplayHyperregionComposer defaultCornerPositionForLayoutSettingsPosition:proposedCenter:geometry:interaction:];
-[SBPIPMultidisplayHyperregionComposer mutableRegionMapForScene:geometry:interaction:];
-[SBPIPMultidisplayHyperregionComposer positionRegionsForRegions:geometry:interaction:];
-[SBPIPMultidisplayHyperregionComposer sceneIdentifiersToComposers];
-[SBPIPMultidisplayHyperregionComposer setConnectedWindowScenes:];
```
