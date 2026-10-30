# `_UIPreviewPresentationAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
d _duration;
@"CAMediaTimingFunction" _mediaTimingFunction;
d _startMediaTime;
@? _advanceBlock;
@"CADisplayLink" _displayLink;
```

## Properties

```
@property (Td,N,V_duration) duration;
@property (T@"CAMediaTimingFunction",&,N,V_mediaTimingFunction) mediaTimingFunction;
@property (Td,N,V_startMediaTime) startMediaTime;
@property (T@?,C,N,V_advanceBlock) advanceBlock;
@property (T@"CADisplayLink",W,N,V_displayLink) displayLink;
```

## Instance methods

```
-[_UIPreviewPresentationAnimator displayLink];
-[_UIPreviewPresentationAnimator init];
-[_UIPreviewPresentationAnimator duration];
-[_UIPreviewPresentationAnimator setDisplayLink:];
-[_UIPreviewPresentationAnimator setDuration:];
-[_UIPreviewPresentationAnimator _advanceFromDisplayLink:];
-[_UIPreviewPresentationAnimator advanceBlock];
-[_UIPreviewPresentationAnimator initWithDuration:advanceBlock:];
-[_UIPreviewPresentationAnimator mediaTimingFunction];
-[_UIPreviewPresentationAnimator setAdvanceBlock:];
-[_UIPreviewPresentationAnimator setMediaTimingFunction:];
-[_UIPreviewPresentationAnimator setStartMediaTime:];
-[_UIPreviewPresentationAnimator startMediaTime];
-[_UIPreviewPresentationAnimator stopAnimation];
```
