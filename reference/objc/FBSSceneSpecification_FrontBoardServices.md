# `FBSSceneSpecification`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionProviding`
- 0 instance variables, 11 properties, 18 instance methods, 1 class methods

## Properties

```
@property (T#,R,N) hostAgentClass;
@property (T#,R,N) clientAgentClass;
@property (T#,R,N) settingsClass;
@property (T#,R,N) clientSettingsClass;
@property (T#,R,N) transitionContextClass;
@property (T@"NSArray",R,C,N) defaultExtensions;
@property (TB,R,N) disablesClientBatching;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneSpecification specification];
```

## Instance methods

```
-[FBSSceneSpecification disablesClientBatching];
-[FBSSceneSpecification succinctDescriptionBuilder];
-[FBSSceneSpecification init];
-[FBSSceneSpecification transitionContextClass];
-[FBSSceneSpecification descriptionWithMultilinePrefix:];
-[FBSSceneSpecification succinctDescription];
-[FBSSceneSpecification isValid];
-[FBSSceneSpecification hash];
-[FBSSceneSpecification settingsClass];
-[FBSSceneSpecification description];
-[FBSSceneSpecification copyWithZone:];
-[FBSSceneSpecification isEqual:];
-[FBSSceneSpecification clientSettingsClass];
-[FBSSceneSpecification defaultExtensions];
-[FBSSceneSpecification descriptionBuilderWithMultilinePrefix:];
-[FBSSceneSpecification clientAgentClass];
-[FBSSceneSpecification hostAgentClass];
-[FBSSceneSpecification _isSignificantTransitionContext:];
```
