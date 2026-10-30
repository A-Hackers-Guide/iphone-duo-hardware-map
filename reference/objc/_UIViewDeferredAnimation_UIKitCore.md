# `_UIViewDeferredAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _finalized;
B _autoreverses;
@"NSString" _key;
d _duration;
@ _initialValue;
d _repeatCount;
```

## Properties

```
@property (TB,R,N,GisEmpty) empty;
@property (T@"NSString",C,N,V_key) key;
@property (TB,R,N,GisFinalized,V_finalized) finalized;
@property (Td,N,V_duration) duration;
@property (T@,&,N,V_initialValue) initialValue;
@property (T@"NSArray",R,N) animationFrames;
@property (Td,N,V_repeatCount) repeatCount;
@property (TB,N,V_autoreverses) autoreverses;
```

## Instance methods

```
-[_UIViewDeferredAnimation setAutoreverses:];
-[_UIViewDeferredAnimation animateFrameAtIndex:animations:];
-[_UIViewDeferredAnimation setRepeatCount:];
-[_UIViewDeferredAnimation repeatCount];
-[_UIViewDeferredAnimation _finalize];
-[_UIViewDeferredAnimation autoreverses];
-[_UIViewDeferredAnimation setKey:];
-[_UIViewDeferredAnimation duration];
-[_UIViewDeferredAnimation setInitialValue:];
-[_UIViewDeferredAnimation _enumerateAnimationFramesForKeyframes:];
-[_UIViewDeferredAnimation addAnimationFrameForValue:];
-[_UIViewDeferredAnimation isEmpty];
-[_UIViewDeferredAnimation _animationFrames];
-[_UIViewDeferredAnimation description];
-[_UIViewDeferredAnimation initialValue];
-[_UIViewDeferredAnimation calculateFrameValues:frameTimes:valueTransformer:];
-[_UIViewDeferredAnimation setDuration:];
-[_UIViewDeferredAnimation animationFrames];
-[_UIViewDeferredAnimation isFinalized];
-[_UIViewDeferredAnimation key];
```
