# `_UIPointerArbiter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPointerArbitrating`
- 1 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"<_UIPointerArbitrating>" _core;
```

## Properties

```
@property (Tq,R,N) pointerState;
@property (T@"_UIPointerLensView",R,N) lensView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPointerArbiter sharedArbiter];
```

## Instance methods

```
-[_UIPointerArbiter pointerState];
-[_UIPointerArbiter init];
-[_UIPointerArbiter endScrollingWithRegion:];
-[_UIPointerArbiter obtainPointerUpdatePauseAssertion];
-[_UIPointerArbiter applyStyle:forRegion:effectSourceHandler:completion:];
-[_UIPointerArbiter beginScrollingWithRegion:];
-[_UIPointerArbiter exitRegion:removeStyle:completion:];
-[_UIPointerArbiter lensView];
```
