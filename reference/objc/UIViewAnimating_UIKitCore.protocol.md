# `UIViewAnimating` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) state;
@property (TB,R,N,GisRunning) running;
@property (TB,N,GisReversed) reversed;
@property (Td,N) fractionComplete;
```

## Instance methods

```
-[UIViewAnimating setReversed:];
-[UIViewAnimating setFractionComplete:];
-[UIViewAnimating isRunning];
-[UIViewAnimating fractionComplete];
-[UIViewAnimating pauseAnimation];
-[UIViewAnimating isReversed];
-[UIViewAnimating startAnimation];
-[UIViewAnimating stopAnimation:];
-[UIViewAnimating finishAnimationAtPosition:];
-[UIViewAnimating startAnimationAfterDelay:];
-[UIViewAnimating state];
```
