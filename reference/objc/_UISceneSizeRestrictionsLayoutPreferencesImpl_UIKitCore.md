# `_UISceneSizeRestrictionsLayoutPreferencesImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneLayoutPreferencesControllerObserver`, `_UISceneSizeRestrictionsImpl`
- 6 instance variables, 7 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"<_UISceneLayoutPreferencesControlling>" _prefsController;
{CGSize="width"d"height"d} _preferredMinimumSize;
{CGSize="width"d"height"d} _preferredMaximumSize;
B _allowsFullScreen;
{CGSize="width"d"height"d} _effectiveMinimumSize;
{CGSize="width"d"height"d} _effectiveMaximumSize;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGSize=dd},N,V_effectiveMinimumSize) minimumSize;
@property (T{CGSize=dd},N,V_effectiveMaximumSize) maximumSize;
@property (TB,N,V_allowsFullScreen) allowsFullScreen;
```

## Class methods

```
+[_UISceneSizeRestrictionsLayoutPreferencesImpl implementationForScene:];
+[_UISceneSizeRestrictionsLayoutPreferencesImpl scenePredicate];
```

## Instance methods

```
-[_UISceneSizeRestrictionsLayoutPreferencesImpl setMaximumSize:];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl maximumSize];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl setMinimumSize:];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl minimumSize];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl allowsFullScreen];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl initWithLayoutPreferencesController:];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl layoutPreferencesControllerDidUpdate:transitionContext:];
-[_UISceneSizeRestrictionsLayoutPreferencesImpl setAllowsFullScreen:];
```
