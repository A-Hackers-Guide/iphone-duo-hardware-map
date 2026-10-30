# `CAPortalLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 1 instance variables, 14 properties, 32 instance methods, 3 class methods

## Instance variables

```
B _excludeSeparated;
```

## Properties

```
@property (T@"CALayer",W) sourceLayer;
@property (TQ) sourceLayerRenderId;
@property (TI) sourceContextId;
@property (TB) hidesSourceLayer;
@property (Tf) sourceLayerOpacityScale;
@property (TB) matchesOpacity;
@property (TB) matchesPosition;
@property (TB) matchesTransform;
@property (TB) allowsBackdropGroups;
@property (TB) crossDisplay;
@property (TB,V_excludeSeparated) excludeSeparated;
@property (TB) allowedInContextTransform;
@property (T@"NSDictionary",C) overrides;
@property (TB) hidesSourceLayerInOtherPortals;
```

## Class methods

```
+[CAPortalLayer defaultValueForKey:];
+[CAPortalLayer _hasRenderLayerSubclass];
+[CAPortalLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAPortalLayer setSourceLayer:];
-[CAPortalLayer setOverrides:];
-[CAPortalLayer setSourceContextId:];
-[CAPortalLayer sourceLayer];
-[CAPortalLayer matchesTransform];
-[CAPortalLayer sourceContextId];
-[CAPortalLayer overrides];
-[CAPortalLayer didChangeValueForKey:];
-[CAPortalLayer setMatchesTransform:];
-[CAPortalLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CAPortalLayer crossDisplay];
-[CAPortalLayer setSourceLayerOpacityScale:];
-[CAPortalLayer _renderLayerDefinesProperty:];
-[CAPortalLayer setAllowedInContextTransform:];
-[CAPortalLayer setMatchesOpacity:];
-[CAPortalLayer excludeSeparated];
-[CAPortalLayer allowedInContextTransform];
-[CAPortalLayer matchesPosition];
-[CAPortalLayer hidesSourceLayer];
-[CAPortalLayer setCrossDisplay:];
-[CAPortalLayer matchesOpacity];
-[CAPortalLayer layerDidBecomeVisible:];
-[CAPortalLayer setHidesSourceLayerInOtherPortals:];
-[CAPortalLayer sourceLayerRenderId];
-[CAPortalLayer setHidesSourceLayer:];
-[CAPortalLayer setSourceLayerRenderId:];
-[CAPortalLayer allowsBackdropGroups];
-[CAPortalLayer hidesSourceLayerInOtherPortals];
-[CAPortalLayer setMatchesPosition:];
-[CAPortalLayer setAllowsBackdropGroups:];
-[CAPortalLayer sourceLayerOpacityScale];
-[CAPortalLayer setExcludeSeparated:];
```
