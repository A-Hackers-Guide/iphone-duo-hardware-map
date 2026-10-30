# `AVSemanticStyle`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 2 class methods

## Instance variables

```
f _toneBias;
f _warmthBias;
Q _hash;
f _subjectBias;
```

## Properties

```
@property (Tf,R,N,V_subjectBias) subjectBias;
@property (Tf,R,N,V_toneBias) toneBias;
@property (Tf,R,N) sceneBias;
@property (Tf,R,N,V_warmthBias) warmthBias;
```

## Class methods

```
+[AVSemanticStyle identityStyle];
+[AVSemanticStyle semanticStyleWithToneBias:warmthBias:];
```

## Instance methods

```
-[AVSemanticStyle debugDescription];
-[AVSemanticStyle hash];
-[AVSemanticStyle description];
-[AVSemanticStyle toneBias];
-[AVSemanticStyle isEqual:];
-[AVSemanticStyle _initWithToneBias:warmthBias:];
-[AVSemanticStyle sceneBias];
-[AVSemanticStyle subjectBias];
-[AVSemanticStyle warmthBias];
```
