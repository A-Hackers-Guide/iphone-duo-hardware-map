# `FBSProcessAssertion`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 6 instance variables, 11 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"<FBSProcess>" _process;
@"FBSProcessExecutionPolicy" _policy;
Q _activationCount;
B _invalidated;
@"BKSProcessAssertion" _assertion;
```

## Properties

```
@property (T@"BKSProcessAssertion",R,N,V_assertion) assertion;
@property (TQ,R,N,V_activationCount) activationCount;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"<FBSProcess>",R,W,N,V_process) process;
@property (T@"FBSProcessExecutionPolicy",R,N,V_policy) policy;
@property (TB,R,N,GisActivated) activated;
@property (TB,R,N,GisInvalidated,V_invalidated) invalidated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSProcessAssertion isActivated];
-[FBSProcessAssertion assertion];
-[FBSProcessAssertion deactivate];
-[FBSProcessAssertion succinctDescriptionBuilder];
-[FBSProcessAssertion process];
-[FBSProcessAssertion dealloc];
-[FBSProcessAssertion descriptionWithMultilinePrefix:];
-[FBSProcessAssertion isInvalidated];
-[FBSProcessAssertion succinctDescription];
-[FBSProcessAssertion invalidate];
-[FBSProcessAssertion activate];
-[FBSProcessAssertion description];
-[FBSProcessAssertion initWithName:process:policy:];
-[FBSProcessAssertion name];
-[FBSProcessAssertion descriptionBuilderWithMultilinePrefix:];
-[FBSProcessAssertion policy];
-[FBSProcessAssertion activationCount];
```
