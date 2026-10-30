# `FBSSceneActivitySession`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 10 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _identifier;
@"<FBSSceneHandle>" _scene;
@"FBSProcessExecutionPolicy" _executionPolicy;
@? _errorHandler;
B _open;
B _invalidated;
@"<FBSProcess>" _process;
@"FBSProcessAssertion" _assertion;
@"FBSProcessWatchdog" _watchdog;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"<FBSSceneHandle>",W,N,V_scene) scene;
@property (T@"FBSProcessExecutionPolicy",C,N,V_executionPolicy) executionPolicy;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (TB,R,N,GisOpen,V_open) open;
@property (TB,R,N,GisInvalidated,V_invalidated) invalidated;
@property (T@?,C,D,N) errorHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSSceneActivitySession _isValid];
-[FBSSceneActivitySession open];
-[FBSSceneActivitySession close];
-[FBSSceneActivitySession identifier];
-[FBSSceneActivitySession succinctDescriptionBuilder];
-[FBSSceneActivitySession setScene:];
-[FBSSceneActivitySession dealloc];
-[FBSSceneActivitySession descriptionWithMultilinePrefix:];
-[FBSSceneActivitySession isInvalidated];
-[FBSSceneActivitySession succinctDescription];
-[FBSSceneActivitySession invalidate];
-[FBSSceneActivitySession scene];
-[FBSSceneActivitySession description];
-[FBSSceneActivitySession setName:];
-[FBSSceneActivitySession setErrorHandler:];
-[FBSSceneActivitySession name];
-[FBSSceneActivitySession errorHandler];
-[FBSSceneActivitySession isOpen];
-[FBSSceneActivitySession descriptionBuilderWithMultilinePrefix:];
-[FBSSceneActivitySession executionPolicy];
-[FBSSceneActivitySession initWithName:scene:executionPolicy:];
-[FBSSceneActivitySession setExecutionPolicy:];
```
