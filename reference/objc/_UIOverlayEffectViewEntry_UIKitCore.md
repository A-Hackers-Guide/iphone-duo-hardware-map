# `_UIOverlayEffectViewEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIVisualEffectViewEntry`
- 4 instance variables, 4 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSString" _filterType;
@"UIColor" _color;
@"UIImage" _image;
d _alpha;
```

## Properties

```
@property (T@"NSString",C,N,V_filterType) filterType;
@property (T@"UIColor",C,N,V_color) color;
@property (T@"UIImage",&,N,V_image) image;
@property (Td,N,V_alpha) alpha;
```

## Class methods

```
+[_UIOverlayEffectViewEntry newEntryWithFilterType:color:alpha:];
+[_UIOverlayEffectViewEntry newEntryWithFilterType:image:alpha:];
```

## Instance methods

```
-[_UIOverlayEffectViewEntry setColor:];
-[_UIOverlayEffectViewEntry filterType];
-[_UIOverlayEffectViewEntry applyRequestedEffectToView:];
-[_UIOverlayEffectViewEntry color];
-[_UIOverlayEffectViewEntry setAlpha:];
-[_UIOverlayEffectViewEntry addEffectToView:];
-[_UIOverlayEffectViewEntry description];
-[_UIOverlayEffectViewEntry alpha];
-[_UIOverlayEffectViewEntry canTransitionToEffect:];
-[_UIOverlayEffectViewEntry image];
-[_UIOverlayEffectViewEntry removeEffectFromView:];
-[_UIOverlayEffectViewEntry setFilterType:];
-[_UIOverlayEffectViewEntry applyIdentityEffectToView:];
-[_UIOverlayEffectViewEntry setImage:];
```
