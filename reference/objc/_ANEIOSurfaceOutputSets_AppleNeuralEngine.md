# `_ANEIOSurfaceOutputSets`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
^{__IOSurface=} _statsSurRef;
@"NSArray" _outputBuffer;
```

## Properties

```
@property (T^{__IOSurface=},R,N,V_statsSurRef) statsSurRef;
@property (T@"NSArray",R,N,V_outputBuffer) outputBuffer;
```

## Class methods

```
+[_ANEIOSurfaceOutputSets supportsSecureCoding];
+[_ANEIOSurfaceOutputSets new];
+[_ANEIOSurfaceOutputSets objectWithstatsSurRef:outputBuffer:];
```

## Instance methods

```
-[_ANEIOSurfaceOutputSets init];
-[_ANEIOSurfaceOutputSets dealloc];
-[_ANEIOSurfaceOutputSets encodeWithCoder:];
-[_ANEIOSurfaceOutputSets outputBuffer];
-[_ANEIOSurfaceOutputSets description];
-[_ANEIOSurfaceOutputSets initWithCoder:];
-[_ANEIOSurfaceOutputSets initWithstatsSurRef:outputBuffer:];
-[_ANEIOSurfaceOutputSets statsSurRef];
```
