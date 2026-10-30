# `NEBitVector`

- Image: [`/usr/lib/libnetworkextension.dylib`](../userland/usr__lib__libnetworkextension.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 3 class methods

## Instance variables

```
I _bitmapSize;
I _bitCount;
* _bitmap;
```

## Class methods

```
+[NEBitVector getBitAtIndexWithBitmap:bitCount:index:];
+[NEBitVector getByteCount:];
+[NEBitVector setBitAtIndexWithBitmap:bitCount:index:toValue:];
```

## Instance methods

```
-[NEBitVector clearAllBits];
-[NEBitVector getBitAtIndex:];
-[NEBitVector initWithBitMap:bitmapSize:bitCount:];
-[NEBitVector printBits];
-[NEBitVector setBitAtIndex:toValue:];
```
