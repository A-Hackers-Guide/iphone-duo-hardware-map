# `SBSABasePreferencesProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAStackablePreferencesProviding`
- 3 instance variables, 7 properties, 19 instance methods, 4 class methods

## Instance variables

```
@"NSMutableArray" _childProviders;
@"<SBSAStackablePreferencesProviding>" _parentProvider;
@"<SBSAStackablePreferencesProviding>" _childProvider;
```

## Properties

```
@property (T@"SBSystemApertureTransitionSettings",R,C,N) defaultTransitionSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBSAStackablePreferencesProviding>",R,W,N,V_parentProvider) parentProvider;
@property (T@"<SBSAStackablePreferencesProviding>",&,N,V_childProvider) childProvider;
```

## Class methods

```
+[SBSABasePreferencesProvider initialize];
+[SBSABasePreferencesProvider settings];
+[SBSABasePreferencesProvider newAnimatedTransitionDescriptionWithBehaviorSettings:];
+[SBSABasePreferencesProvider newUnanimatedTransitionDescription];
```

## Instance methods

```
-[SBSABasePreferencesProvider defaultTransitionSettings];
-[SBSABasePreferencesProvider init];
-[SBSABasePreferencesProvider encodeWithCoder:];
-[SBSABasePreferencesProvider description];
-[SBSABasePreferencesProvider membersForCoder];
-[SBSABasePreferencesProvider behaviorSettingsForProperty:];
-[SBSABasePreferencesProvider childProvider];
-[SBSABasePreferencesProvider descriptionForStackDepiction];
-[SBSABasePreferencesProvider firstChildPreferenceProviderOfClass:];
-[SBSABasePreferencesProvider firstChildPreferenceProviderPassingTest:];
-[SBSABasePreferencesProvider firstChildPreferenceProviderRespondingToSelector:];
-[SBSABasePreferencesProvider initWithParentProvider:];
-[SBSABasePreferencesProvider newAnimatedTransitionDescriptionForProperty:];
-[SBSABasePreferencesProvider newAnimatedTransitionDescriptionForProperty:animated:];
-[SBSABasePreferencesProvider parentProvider];
-[SBSABasePreferencesProvider preferencesFromContext:];
-[SBSABasePreferencesProvider removeFromParentProvider];
-[SBSABasePreferencesProvider setChildProvider:];
-[SBSABasePreferencesProvider stackDepiction];
```
