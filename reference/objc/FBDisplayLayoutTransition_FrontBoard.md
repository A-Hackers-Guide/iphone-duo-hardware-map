# `FBDisplayLayoutTransition`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"FBMainDisplayLayoutPublisher" _publisher;
@"NSString" _name;
@"NSString" _transitionReason;
q _displayType;
@"<BSInvalidatable>" _transition;
q _interfaceOrientation;
q _backlightLevel;
```

## Properties

```
@property (Tq,R,N,V_displayType) displayType;
@property (T@"NSString",R,C,N,V_name) name;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"NSString",C,N,V_transitionReason) transitionReason;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (Tq,N,V_backlightLevel) backlightLevel;
```

## Class methods

```
+[FBDisplayLayoutTransition flushLayoutForDisplayType:];
+[FBDisplayLayoutTransition layoutForDisplayType:];
```

## Instance methods

```
-[FBDisplayLayoutTransition beginTransition];
-[FBDisplayLayoutTransition interfaceOrientation];
-[FBDisplayLayoutTransition setBacklightLevel:];
-[FBDisplayLayoutTransition displayType];
-[FBDisplayLayoutTransition backlightLevel];
-[FBDisplayLayoutTransition setInterfaceOrientation:];
-[FBDisplayLayoutTransition init];
-[FBDisplayLayoutTransition isTransitioning];
-[FBDisplayLayoutTransition dealloc];
-[FBDisplayLayoutTransition endTransition];
-[FBDisplayLayoutTransition transitionReason];
-[FBDisplayLayoutTransition description];
-[FBDisplayLayoutTransition name];
-[FBDisplayLayoutTransition initWithDisplayType:name:];
-[FBDisplayLayoutTransition setTransitionReason:];
```
