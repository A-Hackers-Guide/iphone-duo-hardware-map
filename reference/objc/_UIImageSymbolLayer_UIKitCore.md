# `_UIImageSymbolLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 12 instance methods, 5 class methods

## Instance variables

```
@"UIColor" _color;
d _scaleFactor;
@"UIImageAsset" _asset;
@"_UIImageCUIVectorGlyphContent" _content;
{CGPoint="x"d"y"d} _offset;
```

## Properties

```
@property (T@"UIImageAsset",&,N,V_asset) asset;
@property (T@"_UIImageCUIVectorGlyphContent",&,N,V_content) content;
@property (T@"UIColor",&,N,V_color) color;
@property (T{CGPoint=dd},N,V_offset) offset;
@property (Td,N,V_scaleFactor) scaleFactor;
@property (T@"NSString",R,N) name;
@property (TB,R,N,GisSystemImage) systemImage;
```

## Class methods

```
+[_UIImageSymbolLayer _symbolLayerWithImage:color:offset:scaleFactor:];
+[_UIImageSymbolLayer _symbolLayerWithName:color:];
+[_UIImageSymbolLayer _symbolLayerWithName:color:offset:scaleFactor:];
+[_UIImageSymbolLayer _symbolLayerWithSystemName:color:];
+[_UIImageSymbolLayer _symbolLayerWithSystemName:color:offset:scaleFactor:];
```

## Instance methods

```
-[_UIImageSymbolLayer setColor:];
-[_UIImageSymbolLayer asset];
-[_UIImageSymbolLayer setContent:];
-[_UIImageSymbolLayer setAsset:];
-[_UIImageSymbolLayer content];
-[_UIImageSymbolLayer setScaleFactor:];
-[_UIImageSymbolLayer isSystemImage];
-[_UIImageSymbolLayer color];
-[_UIImageSymbolLayer scaleFactor];
-[_UIImageSymbolLayer setOffset:];
-[_UIImageSymbolLayer name];
-[_UIImageSymbolLayer offset];
```
