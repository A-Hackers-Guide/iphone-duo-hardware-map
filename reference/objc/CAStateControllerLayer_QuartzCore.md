# `CAStateControllerLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CALayer" _layer;
@"CAState" _currentState;
@"CAStateControllerUndo" _undoStack;
@"NSMutableArray" _transitions;
@"NSTimer" _nextTimer;
@"CAState" _nextState;
f _nextSpeed;
```

## Properties

```
@property (T@"CALayer",R,V_layer) layer;
@property (T@"CAState",&,N,V_currentState) currentState;
@property (T@"CAStateControllerUndo",R,V_undoStack) undoStack;
```

## Instance methods

```
-[CAStateControllerLayer layer];
-[CAStateControllerLayer addTransition:];
-[CAStateControllerLayer dealloc];
-[CAStateControllerLayer initWithLayer:];
-[CAStateControllerLayer invalidate];
-[CAStateControllerLayer setCurrentState:];
-[CAStateControllerLayer currentState];
-[CAStateControllerLayer removeTransition:];
-[CAStateControllerLayer undoStack];
```
