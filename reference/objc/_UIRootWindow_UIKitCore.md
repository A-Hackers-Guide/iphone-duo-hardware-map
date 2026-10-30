# `_UIRootWindow`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindow`
- 11 instance variables, 2 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayIdentity" _currentDisplayIdentity;
d _scale;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _visibilityLock;
B _visibilityLock_enabled;
@"NSString" _visibilityLock_environment;
@"NSString" _visibilityLock_identifier;
B _visibilityLock_updateEnqueued;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _visibilityProcessingLock;
@"NSString" _visibilityProcessingLock_identifier;
@"RBSAssertion" _visibilityProcessingLock_assertion;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _additionalRootLayerAffineTransform;
```

## Properties

```
@property (T{CGAffineTransform=dddddd},N,G_additionalRootLayerAffineTransform,S_setAdditionalRootLayerAffineTransform:,V_additionalRootLayerAffineTransform) additionalRootLayerAffineTransform;
@property (T@"NSString",R,C,N) visibilityEnvironment;
```

## Class methods

```
+[_UIRootWindow _needsPassthroughInteraction];
```

## Instance methods

```
-[_UIRootWindow initWithScreen:];
-[_UIRootWindow _updateVisibility];
-[_UIRootWindow initWithDisplay:];
-[_UIRootWindow _configureRootLayer:sceneTransformLayer:transformLayer:];
-[_UIRootWindow setHidden:];
-[_UIRootWindow _extendsScreenSceneLifetime];
-[_UIRootWindow dealloc];
-[_UIRootWindow _additionalRootLayerAffineTransform];
-[_UIRootWindow _bindingDescription];
-[_UIRootWindow _context];
-[_UIRootWindow _didMoveFromScene:toScene:];
-[_UIRootWindow _didMoveFromScreen:toScreen:];
-[_UIRootWindow _isWindowServerHostingManaged];
-[_UIRootWindow _layerForCoordinateSpaceConversion];
-[_UIRootWindow _noteScreenDidChangeMode:];
-[_UIRootWindow _prepareHierarchyForWindowHostingSceneRemoval];
-[_UIRootWindow _setAdditionalRootLayerAffineTransform:];
-[_UIRootWindow _transformLayerIncludesScreenRotation];
-[_UIRootWindow _visibilityLock_enqueueUpdateIfNecessary];
-[_UIRootWindow _visibilityLock_enqueueUpdateIfNecessary_body];
-[_UIRootWindow _visibilityLock_environment];
-[_UIRootWindow _wantsSceneAssociation];
-[_UIRootWindow setVisibilityIdentifier:];
-[_UIRootWindow visibilityEnvironment];
```
