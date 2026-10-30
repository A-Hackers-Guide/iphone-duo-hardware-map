# `_UIViewLayoutEngineRelativeAlignmentRectOriginCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _cachedOrigin;
@"UIView" _delegate;
@"NSISEngine" _cacheEngine;
Q _variableChangeCount;
```

## Properties

```
@property (T@"NSISEngine",W,N,V_cacheEngine) cacheEngine;
@property (TQ,N,V_variableChangeCount) variableChangeCount;
@property (T{CGPoint=dd},R,N) origin;
@property (TB,R,N) isValid;
@property (T@"UIView",R,W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache initWithDelegate:];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache origin];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache setVariableChangeCount:];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache isValid];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache delegate];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache setCacheEngine:];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache variableChangeCount];
-[_UIViewLayoutEngineRelativeAlignmentRectOriginCache cacheEngine];
```
