# `FBSProcessWatchdogPolicy`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 2 instance variables, 6 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSString" _name;
@"NSArray" _provisions;
```

## Properties

```
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSArray",C,N,V_provisions) provisions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSProcessWatchdogPolicy policyWithProvisions:];
+[FBSProcessWatchdogPolicy policyWithName:forProvisions:];
```

## Instance methods

```
-[FBSProcessWatchdogPolicy setProvisions:];
-[FBSProcessWatchdogPolicy succinctDescriptionBuilder];
-[FBSProcessWatchdogPolicy provisions];
-[FBSProcessWatchdogPolicy descriptionWithMultilinePrefix:];
-[FBSProcessWatchdogPolicy succinctDescription];
-[FBSProcessWatchdogPolicy description];
-[FBSProcessWatchdogPolicy setName:];
-[FBSProcessWatchdogPolicy copyWithZone:];
-[FBSProcessWatchdogPolicy name];
-[FBSProcessWatchdogPolicy descriptionBuilderWithMultilinePrefix:];
```
