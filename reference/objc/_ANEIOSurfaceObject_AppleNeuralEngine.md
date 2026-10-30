# `_ANEIOSurfaceObject`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 6 class methods

## Instance variables

```
^{__IOSurface=} _ioSurface;
@"NSNumber" _startOffset;
```

## Properties

```
@property (T^{__IOSurface=},R,N,V_ioSurface) ioSurface;
@property (T@"NSNumber",R,N,V_startOffset) startOffset;
```

## Class methods

```
+[_ANEIOSurfaceObject supportsSecureCoding];
+[_ANEIOSurfaceObject new];
+[_ANEIOSurfaceObject objectWithIOSurface:];
+[_ANEIOSurfaceObject createIOSurfaceWithWidth:pixel_size:height:];
+[_ANEIOSurfaceObject createIOSurfaceWithWidth:pixel_size:height:bytesPerElement:];
+[_ANEIOSurfaceObject objectWithIOSurface:startOffset:];
```

## Instance methods

```
-[_ANEIOSurfaceObject init];
-[_ANEIOSurfaceObject dealloc];
-[_ANEIOSurfaceObject ioSurface];
-[_ANEIOSurfaceObject startOffset];
-[_ANEIOSurfaceObject encodeWithCoder:];
-[_ANEIOSurfaceObject initWithIOSurface:startOffset:shouldRetain:];
-[_ANEIOSurfaceObject description];
-[_ANEIOSurfaceObject initWithCoder:];
```
