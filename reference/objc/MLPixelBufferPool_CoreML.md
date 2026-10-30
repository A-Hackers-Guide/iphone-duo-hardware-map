# `MLPixelBufferPool`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cacheLock;
@"NSMutableDictionary" _pixelBufferPoolCache;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_pixelBufferPoolCache) pixelBufferPoolCache;
```

## Instance methods

```
-[MLPixelBufferPool init];
-[MLPixelBufferPool _pixelBufferPoolWithSize:pixelFormatType:error:];
-[MLPixelBufferPool pixelBufferPoolCache];
-[MLPixelBufferPool createPixelBufferWithSize:pixelFormatType:error:];
```
