# `CABackdropLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 1 instance variables, 24 properties, 51 instance methods, 3 class methods

## Instance variables

```
B _disablesOccludedBackdropBlurs;
```

## Properties

```
@property (TB,GisEnabled) enabled;
@property (T@"NSString",C) groupName;
@property (TB) usesGlobalGroupNamespace;
@property (T@"NSString",C) groupNamespace;
@property (Td) scale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}}) backdropRect;
@property (Td) marginWidth;
@property (TB,V_disablesOccludedBackdropBlurs) disablesOccludedBackdropBlurs;
@property (TB) captureOnly;
@property (TB) allowsInPlaceFiltering;
@property (TB) reducesCaptureBitDepth;
@property (TB) ignoresScreenClip;
@property (TB) preallocatesScreenArea;
@property (TB,GisInverseMeshed) inverseMeshed;
@property (Td) zoom;
@property (TB) disableFilterCache;
@property (TB) sourceSublayerDefinesBounds;
@property (Td) updateRate;
@property (TB) tracksLuma;
@property (TB) tracksLumaWhileHidden;
@property (Td) lumaUpdateRate;
@property (TB) allowsFilteredLuma;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}}) lumaSubrect;
@property (T@"<CABackdropLayerDelegate><CALayerDelegate>",W,D) delegate;
```

## Class methods

```
+[CABackdropLayer defaultValueForKey:];
+[CABackdropLayer _hasRenderLayerSubclass];
+[CABackdropLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CABackdropLayer setZoom:];
-[CABackdropLayer didChangeValueForKey:];
-[CABackdropLayer ignoresScreenClip];
-[CABackdropLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CABackdropLayer setCaptureOnly:];
-[CABackdropLayer _renderLayerDefinesProperty:];
-[CABackdropLayer _renderLayerPropertyAnimationFlags:];
-[CABackdropLayer setGroupName:];
-[CABackdropLayer setDisablesOccludedBackdropBlurs:];
-[CABackdropLayer setScale:];
-[CABackdropLayer isEnabled];
-[CABackdropLayer zoom];
-[CABackdropLayer scale];
-[CABackdropLayer disablesOccludedBackdropBlurs];
-[CABackdropLayer layerDidBecomeVisible:];
-[CABackdropLayer setEnabled:];
-[CABackdropLayer groupName];
-[CABackdropLayer setIgnoresScreenClip:];
-[CABackdropLayer setGroupNamespace:];
-[CABackdropLayer groupNamespace];
-[CABackdropLayer isInverseMeshed];
-[CABackdropLayer setLumaSubrect:];
-[CABackdropLayer setMarginWidth:];
-[CABackdropLayer setSourceSublayerDefinesBounds:];
-[CABackdropLayer allowsFilteredLuma];
-[CABackdropLayer allowsInPlaceFiltering];
-[CABackdropLayer backdropRect];
-[CABackdropLayer captureOnly];
-[CABackdropLayer disableFilterCache];
-[CABackdropLayer lumaSubrect];
-[CABackdropLayer lumaUpdateRate];
-[CABackdropLayer marginWidth];
-[CABackdropLayer preallocatesScreenArea];
-[CABackdropLayer reducesCaptureBitDepth];
-[CABackdropLayer setAllowsFilteredLuma:];
-[CABackdropLayer setAllowsInPlaceFiltering:];
-[CABackdropLayer setBackdropRect:];
-[CABackdropLayer setDisableFilterCache:];
-[CABackdropLayer setInverseMeshed:];
-[CABackdropLayer setLumaUpdateRate:];
-[CABackdropLayer setPreallocatesScreenArea:];
-[CABackdropLayer setReducesCaptureBitDepth:];
-[CABackdropLayer setTracksLuma:];
-[CABackdropLayer setTracksLumaWhileHidden:];
-[CABackdropLayer setUpdateRate:];
-[CABackdropLayer setUsesGlobalGroupNamespace:];
-[CABackdropLayer sourceSublayerDefinesBounds];
-[CABackdropLayer tracksLuma];
-[CABackdropLayer tracksLumaWhileHidden];
-[CABackdropLayer updateRate];
-[CABackdropLayer usesGlobalGroupNamespace];
```
