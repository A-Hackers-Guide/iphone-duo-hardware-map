# `UIKBRenderFactoryLayoutSegment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
i _rectCount;
[10{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}] _rects;
[10Q] _triangleCorners;
i _edgeCount;
[10Q] _edges;
[10@"NSString"] _cachedKeyNames;
B _requireAllMatches;
i _states;
@"UIKBRenderTraits" _traits;
```

## Properties

```
@property (T@"UIKBRenderTraits",R,N,V_traits) traits;
@property (Ti,N,V_states) keyStates;
@property (TB,N,V_requireAllMatches) requireAllMatches;
```

## Class methods

```
+[UIKBRenderFactoryLayoutSegment segmentWithTraits:];
```

## Instance methods

```
-[UIKBRenderFactoryLayoutSegment initWithTraits:];
-[UIKBRenderFactoryLayoutSegment traits];
-[UIKBRenderFactoryLayoutSegment addRelativeLayoutRectFromEdge:ofCachedKey:];
-[UIKBRenderFactoryLayoutSegment containsPoint:inRect:withKeyplane:];
-[UIKBRenderFactoryLayoutSegment keyStates];
-[UIKBRenderFactoryLayoutSegment shouldOverlayTraitsForKey:];
-[UIKBRenderFactoryLayoutSegment setKeyStates:];
-[UIKBRenderFactoryLayoutSegment requireAllMatches];
-[UIKBRenderFactoryLayoutSegment setRequireAllMatches:];
-[UIKBRenderFactoryLayoutSegment addLayoutRect:asTriangle:];
```
