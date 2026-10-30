# `_UIBoundingPathBitmap`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 1 properties, 11 instance methods, 1 class methods

## Instance variables

```
{_UIBoundingPathBitmapData="width"Q"height"Q"skipRegion"{_UIBoundingPathBitmapDataSkipRegion="y"Q"height"Q}"nodeCount"Q"maximumNodesPerRow"Q"rows"^S} _bitmapData;
```

## Properties

```
@property (T{_UIBoundingPathBitmapData=QQ{_UIBoundingPathBitmapDataSkipRegion=QQ}QQ^S},R,N,V_bitmapData) bitmapData;
```

## Class methods

```
+[_UIBoundingPathBitmap supportsSecureCoding];
```

## Instance methods

```
-[_UIBoundingPathBitmap bitmapData];
-[_UIBoundingPathBitmap debugQuickLookObject];
-[_UIBoundingPathBitmap initWithSize:containsPoint:];
-[_UIBoundingPathBitmap boundingPathBitmapWithRect:];
-[_UIBoundingPathBitmap dealloc];
-[_UIBoundingPathBitmap initWithBitmapData:];
-[_UIBoundingPathBitmap encodeWithCoder:];
-[_UIBoundingPathBitmap _imageRepresentation];
-[_UIBoundingPathBitmap description];
-[_UIBoundingPathBitmap initWithCoder:];
-[_UIBoundingPathBitmap boundingPathBitmapWithRect:cornerRadii:];
```
