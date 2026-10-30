# `_SBPIPEndStashTabSuppressionGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _targets;
@"UITapGestureRecognizer" _singleTapRecognizer;
@"UITapGestureRecognizer" _doubleTapRecognizer;
@"SBSystemGestureManager" _systemGestureManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBPIPEndStashTabSuppressionGestureManager _removeGestureRecognizers];
-[_SBPIPEndStashTabSuppressionGestureManager dealloc];
-[_SBPIPEndStashTabSuppressionGestureManager initWithSystemGestureManager:];
-[_SBPIPEndStashTabSuppressionGestureManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_SBPIPEndStashTabSuppressionGestureManager removeTarget:action:];
-[_SBPIPEndStashTabSuppressionGestureManager addTarget:action:];
-[_SBPIPEndStashTabSuppressionGestureManager _addSystemRecognizers];
```
