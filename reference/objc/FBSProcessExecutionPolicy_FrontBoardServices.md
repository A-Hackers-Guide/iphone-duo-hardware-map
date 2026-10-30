# `FBSProcessExecutionPolicy`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 2 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"FBSProcessExecutionStrategy" _strategy;
@"NSArray" _provisions;
```

## Properties

```
@property (T@"FBSProcessExecutionStrategy",C,N,V_strategy) strategy;
@property (T@"NSArray",C,N,V_provisions) provisions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSProcessExecutionPolicy policyForStrategy:withProvisions:];
```

## Instance methods

```
-[FBSProcessExecutionPolicy setProvisions:];
-[FBSProcessExecutionPolicy succinctDescriptionBuilder];
-[FBSProcessExecutionPolicy provisions];
-[FBSProcessExecutionPolicy descriptionWithMultilinePrefix:];
-[FBSProcessExecutionPolicy succinctDescription];
-[FBSProcessExecutionPolicy setStrategy:];
-[FBSProcessExecutionPolicy description];
-[FBSProcessExecutionPolicy strategy];
-[FBSProcessExecutionPolicy copyWithZone:];
-[FBSProcessExecutionPolicy descriptionBuilderWithMultilinePrefix:];
```
