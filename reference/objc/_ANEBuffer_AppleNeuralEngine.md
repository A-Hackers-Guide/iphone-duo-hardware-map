# `_ANEBuffer`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"_ANEIOSurfaceObject" _ioSurfaceObject;
@"NSNumber" _symbolIndex;
q _source;
```

## Properties

```
@property (T@"_ANEIOSurfaceObject",R,N,V_ioSurfaceObject) ioSurfaceObject;
@property (T@"NSNumber",R,N,V_symbolIndex) symbolIndex;
@property (Tq,R,N,V_source) source;
```

## Class methods

```
+[_ANEBuffer supportsSecureCoding];
+[_ANEBuffer new];
+[_ANEBuffer bufferWithIOSurfaceObject:symbolIndex:source:];
```

## Instance methods

```
-[_ANEBuffer init];
-[_ANEBuffer encodeWithCoder:];
-[_ANEBuffer description];
-[_ANEBuffer initWithCoder:];
-[_ANEBuffer symbolIndex];
-[_ANEBuffer source];
-[_ANEBuffer ioSurfaceObject];
-[_ANEBuffer initWithIOSurfaceObject:symbolIndex:source:];
```
