# `BWTrackedSurface`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{__IOSurface=} _surface;
@? _handler;
i _clientUseCount;
B _owningPixelBufferDeallocated;
```

## Properties

```
@property (T^{__IOSurface=},R,N,V_surface) surface;
@property (T@?,R,N,V_handler) handler;
@property (Ti,N,V_clientUseCount) clientUseCount;
@property (TB,N,V_owningPixelBufferDeallocated) owningPixelBufferDeallocated;
```

## Instance methods

```
-[BWTrackedSurface surface];
-[BWTrackedSurface dealloc];
-[BWTrackedSurface handler];
-[BWTrackedSurface clientUseCount];
-[BWTrackedSurface initWithSurface:handler:];
-[BWTrackedSurface owningPixelBufferDeallocated];
-[BWTrackedSurface setClientUseCount:];
-[BWTrackedSurface setOwningPixelBufferDeallocated:];
```
