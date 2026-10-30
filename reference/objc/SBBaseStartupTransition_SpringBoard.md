# `SBBaseStartupTransition`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransaction`
- Protocols: `SBStartupTransition`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _destination;
@"SBStartupTransitionContext" _context;
@"SBMainWorkspace" _mainWorkspace;
```

## Properties

```
@property (T@"SBMainWorkspace",R,N,V_mainWorkspace) mainWorkspace;
@property (T@"SBStartupTransitionContext",R,N,V_context) context;
@property (TQ,R,N,V_destination) destination;
```

## Instance methods

```
-[SBBaseStartupTransition _begin];
-[SBBaseStartupTransition destination];
-[SBBaseStartupTransition mainWorkspace];
-[SBBaseStartupTransition context];
-[SBBaseStartupTransition initWithDestination:context:];
-[SBBaseStartupTransition performTransitionWithCompletionBlock:];
```
