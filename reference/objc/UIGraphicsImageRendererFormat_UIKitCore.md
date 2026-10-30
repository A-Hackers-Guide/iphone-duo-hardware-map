# `UIGraphicsImageRendererFormat`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGraphicsRendererFormat`
- 5 instance variables, 10 properties, 21 instance methods, 3 class methods

## Instance variables

```
^{CGColorSpace=} _overrideColorSpace;
B _opaque;
q _overrideBitsPerComponent;
d _scale;
q _preferredRange;
```

## Properties

```
@property (T^{CGColorSpace=},N,G_overrideColorSpace,S_setOverrideColorSpace:) _overrideColorSpace;
@property (Tq,N,G_overrideBitsPerComponent,S_setOverrideBitsPerComponent:,V_overrideBitsPerComponent) _overrideBitsPerComponent;
@property (Td,R,N,G_contextScale) _contextScale;
@property (TB,N,G_wantsAlphaMask,S_setWantsAlphaMask:) _wantsAlphaMask;
@property (TB,N,G_grayscale,S_setGrayscale:) _grayscale;
@property (Td,N,V_scale) scale;
@property (TB,N,V_opaque) opaque;
@property (TB,N) prefersExtendedRange;
@property (TB,R,N) supportsHighDynamicRange;
@property (Tq,N,V_preferredRange) preferredRange;
```

## Class methods

```
+[UIGraphicsImageRendererFormat preferredFormat];
+[UIGraphicsImageRendererFormat formatForTraitCollection:];
+[UIGraphicsImageRendererFormat defaultFormat];
```

## Instance methods

```
-[UIGraphicsImageRendererFormat _setGrayscale:];
-[UIGraphicsImageRendererFormat _overrideColorSpace];
-[UIGraphicsImageRendererFormat opaque];
-[UIGraphicsImageRendererFormat _contextScale];
-[UIGraphicsImageRendererFormat _setOverrideBitsPerComponent:];
-[UIGraphicsImageRendererFormat init];
-[UIGraphicsImageRendererFormat dealloc];
-[UIGraphicsImageRendererFormat preferredRange];
-[UIGraphicsImageRendererFormat setOpaque:];
-[UIGraphicsImageRendererFormat setScale:];
-[UIGraphicsImageRendererFormat _setOverrideColorSpace:];
-[UIGraphicsImageRendererFormat prefersExtendedRange];
-[UIGraphicsImageRendererFormat supportsHighDynamicRange];
-[UIGraphicsImageRendererFormat scale];
-[UIGraphicsImageRendererFormat setPreferredRange:];
-[UIGraphicsImageRendererFormat _grayscale];
-[UIGraphicsImageRendererFormat _wantsAlphaMask];
-[UIGraphicsImageRendererFormat _setWantsAlphaMask:];
-[UIGraphicsImageRendererFormat copyWithZone:];
-[UIGraphicsImageRendererFormat _overrideBitsPerComponent];
-[UIGraphicsImageRendererFormat setPrefersExtendedRange:];
```
