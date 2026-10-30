# `SBZStackResolverTestRecipe`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBTestRecipe`
- 3 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _wantsHomeGesture;
@"SBFZStackParticipant" _participant;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBFZStackParticipant",&,N,V_participant) participant;
@property (TB,N,V_wantsHomeGesture) wantsHomeGesture;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBZStackResolverTestRecipe setWantsHomeGesture:];
-[SBZStackResolverTestRecipe setWindowScene:];
-[SBZStackResolverTestRecipe participant];
-[SBZStackResolverTestRecipe zStackParticipant:updatePreferences:];
-[SBZStackResolverTestRecipe zStackParticipantDidChange:];
-[SBZStackResolverTestRecipe title];
-[SBZStackResolverTestRecipe windowScene];
-[SBZStackResolverTestRecipe setParticipant:];
-[SBZStackResolverTestRecipe wantsHomeGesture];
-[SBZStackResolverTestRecipe handleVolumeDecrease];
-[SBZStackResolverTestRecipe handleVolumeIncrease];
-[SBZStackResolverTestRecipe windowSceneDidUpdate:];
```
