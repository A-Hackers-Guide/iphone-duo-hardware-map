# `CAStateControllerUndo`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAStateRecorder`
- 4 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CAStateControllerUndo" _next;
@"CAState" _state;
@"NSMutableArray" _elements;
@"NSMutableArray" _transitions;
```

## Properties

```
@property (T@"CAStateControllerUndo",R,V_next) next;
@property (T@"CAState",&,N,V_state) state;
@property (T@"NSMutableArray",&,N,V_elements) elements;
@property (T@"NSMutableArray",&,N,V_transitions) transitions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAStateControllerUndo setElements:];
-[CAStateControllerUndo transitions];
-[CAStateControllerUndo next];
-[CAStateControllerUndo setState:];
-[CAStateControllerUndo addElement:];
-[CAStateControllerUndo elements];
-[CAStateControllerUndo addTransition:];
-[CAStateControllerUndo dealloc];
-[CAStateControllerUndo setTransitions:];
-[CAStateControllerUndo willAddLayer:];
-[CAStateControllerUndo state];
```
