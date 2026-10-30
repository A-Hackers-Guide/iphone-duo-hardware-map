# `FBSSceneUpdate`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSMutableCopying`, `NSCopying`
- 9 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"FBSSettings" _settings;
@"FBSSettings<FBSMutableSettings>" _mutableSettings;
@"FBSSettings" _previousSettings;
@"FBSSettingsDiff" _diff;
@"FBSSceneTransitionContext" _context;
@"FBSSceneUpdate" _instigatingUpdate;
@"NSArray" _updateCompletions;
B _haveCompletionsBeenTaken;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSSceneUpdate settingsDiff];
-[FBSSceneUpdate mutableCopyWithZone:];
-[FBSSceneUpdate debugDescription];
-[FBSSceneUpdate succinctDescriptionBuilder];
-[FBSSceneUpdate transitionContext];
-[FBSSceneUpdate init];
-[FBSSceneUpdate settings];
-[FBSSceneUpdate dealloc];
-[FBSSceneUpdate descriptionWithMultilinePrefix:];
-[FBSSceneUpdate succinctDescription];
-[FBSSceneUpdate description];
-[FBSSceneUpdate copyWithZone:];
-[FBSSceneUpdate descriptionBuilderWithMultilinePrefix:];
-[FBSSceneUpdate mutableSettings];
-[FBSSceneUpdate addUpdateCompletion:];
-[FBSSceneUpdate inspect:];
-[FBSSceneUpdate parentUpdate];
-[FBSSceneUpdate previousSettings];
-[FBSSceneUpdate takeUpdateCompletions];
-[FBSSceneUpdate updateCompletionsCount];
```
