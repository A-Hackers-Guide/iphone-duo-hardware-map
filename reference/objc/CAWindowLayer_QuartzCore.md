# `CAWindowLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 1 instance variables, 8 properties, 20 instance methods, 3 class methods

## Instance variables

```
B _windowFlattened;
```

## Properties

```
@property (TB,N,V_windowFlattened) windowFlattened;
@property (Td) postCommitDuration;
@property (TB) ignoreAnimations;
@property (TB) fullyOccluded;
@property (T@"NSString",C) flattenMode;
@property (TB) flattenBackdrops;
@property (TI) contextId;
@property (T@"<CAWindowLayerDelegate><CALayerDelegate>",W,D) delegate;
```

## Class methods

```
+[CAWindowLayer defaultValueForKey:];
+[CAWindowLayer _hasRenderLayerSubclass];
+[CAWindowLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAWindowLayer contextId];
-[CAWindowLayer setFlattenMode:];
-[CAWindowLayer didChangeValueForKey:];
-[CAWindowLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CAWindowLayer setContextId:];
-[CAWindowLayer setWindowFlattened:];
-[CAWindowLayer postCommitDuration];
-[CAWindowLayer init];
-[CAWindowLayer _renderLayerDefinesProperty:];
-[CAWindowLayer dealloc];
-[CAWindowLayer setIgnoreAnimations:];
-[CAWindowLayer setFullyOccluded:];
-[CAWindowLayer windowFlattened];
-[CAWindowLayer setDelegate:];
-[CAWindowLayer ignoreAnimations];
-[CAWindowLayer flattenBackdrops];
-[CAWindowLayer setPostCommitDuration:];
-[CAWindowLayer setFlattenBackdrops:];
-[CAWindowLayer fullyOccluded];
-[CAWindowLayer flattenMode];
```
