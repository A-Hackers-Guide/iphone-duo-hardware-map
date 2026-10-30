# `IOSurfaceMemoryPool`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _poolId;
I _poolPort;
```

## Properties

```
@property (TQ,R) poolId;
```

## Instance methods

```
-[IOSurfaceMemoryPool initWithProperties:];
-[IOSurfaceMemoryPool dealloc];
-[IOSurfaceMemoryPool flush:];
-[IOSurfaceMemoryPool copyDebugInfo];
-[IOSurfaceMemoryPool ensureMemory:];
-[IOSurfaceMemoryPool poolId];
```
