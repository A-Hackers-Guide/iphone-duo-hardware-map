# `SBCompanionScenePresentationContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`
- 4 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"FBSSceneParameters" _parameters;
@"NSSet" _lifecycleConstraints;
@"FBSScene" _parentScene;
@"_UISceneAccessoryContainerSpecification" _sceneSpecification;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",R,C,N) displayConfiguration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T@"_UISceneAccessoryContainerSpecification",R,C,N,V_sceneSpecification) sceneSpecification;
@property (T@"FBSSceneParameters",R,C,N) parameters;
@property (T@"NSSet",R,C,N) lifecycleConstraints;
@property (T@"FBSScene",R,N) parentScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCompanionScenePresentationContext defaultLifecycleConstraints];
```

## Instance methods

```
-[SBCompanionScenePresentationContext sceneSpecification];
-[SBCompanionScenePresentationContext parameters];
-[SBCompanionScenePresentationContext displayConfiguration];
-[SBCompanionScenePresentationContext mutableCopyWithZone:];
-[SBCompanionScenePresentationContext hash];
-[SBCompanionScenePresentationContext description];
-[SBCompanionScenePresentationContext appendDescriptionToStream:];
-[SBCompanionScenePresentationContext copyWithZone:];
-[SBCompanionScenePresentationContext isEqual:];
-[SBCompanionScenePresentationContext frame];
-[SBCompanionScenePresentationContext parentScene];
-[SBCompanionScenePresentationContext initWithSceneParameters:];
-[SBCompanionScenePresentationContext initWithSceneSpecification:parameters:];
-[SBCompanionScenePresentationContext lifecycleConstraints];
```
