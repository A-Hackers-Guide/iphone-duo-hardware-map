# `SBTransientOverlayDefaultTransitionContextProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTransientOverlayTransitionContextProviding`
- 6 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _didPerformAlongsideTransitions;
B _isCompleted;
@"NSMutableArray" _transitionBlocks;
@"NSMutableArray" _transitionCompletionBlocks;
B _transitionCompletedSuccessfully;
B animated;
```

## Properties

```
@property (TB,N,GisAnimated,Vanimated) animated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTransientOverlayDefaultTransitionContextProvider isAnimated];
-[SBTransientOverlayDefaultTransitionContextProvider completeTransition:];
-[SBTransientOverlayDefaultTransitionContextProvider setAnimated:];
-[SBTransientOverlayDefaultTransitionContextProvider performAlongsideTransitions];
-[SBTransientOverlayDefaultTransitionContextProvider transitionAlongsideUsingBlock:completion:];
```
